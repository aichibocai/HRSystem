#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from system.models import Info, Salary, Check, Department
from django.contrib import auth
from django.contrib.auth.models import User
from django.utils import timezone
from django.template import RequestContext
from django.template.context_processors import request
from django.contrib.auth.decorators import login_required, permission_required
import re


# Create your views here.
def Welcome(request):
    user =  User.objects.get(username=request.user)
    welname = ''
    if user.info:
        welname = user.info.name
    
    return welname
#登入
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/base/')
    
    if request.POST:
        
            
        username = request.POST.get('username','')
        password = request.POST.get('password','')
    
        user = auth.authenticate(username = username, password = password)
        
        if user is not None and user.is_active:
            request.session['count'] = 0
            auth.login(request, user)
            return HttpResponseRedirect('/base/')
        else:
            if 'count' in request.session:
                request.session['count'] += 1
                if request.session['count'] > 5:
                    
                    return render(request,'error.html', locals())  
            else:
                request.session['count'] = 1
              
            
            error = '用户名或密码错误'
            return render(request,'login.html', locals())
        
    return render(request,'login.html', locals())
    
#登出 
@login_required 
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login/')



#全部员工薪资信息
@login_required
@permission_required('system.HR_permission', login_url='/accounts/login/')
def AllSalary(request):
    
    welname = Welcome(request)
    #所有部门
    departments = Department.objects.all()
    #所有员工
    persons = Info.objects.all()
    
    if request.POST:
        #无条件搜索
        if request.POST['department'] == 'all' and request.POST['persons'] == 'all':
            salarys = Salary.objects.all()
        else:
            salarys = []
            #按部门搜索
            if request.POST['department'] != 'all' and request.POST['persons'] == 'all':
                department = Department.objects.filter(dno=request.POST['department'])
                infos = Info.objects.filter(department = department)
                salarys = Salary.objects.filter(info = infos)
            #按员工搜索   
            elif request.POST['department'] == 'all' and request.POST['persons'] != 'all':
                user = request.POST['persons']
                infos = Info.objects.filter(name = user)
                salarys = Salary.objects.filter(info = infos)
            #按部门和员工搜索
            else:
                department = Department.objects.filter(dno=request.POST['department'])
                user = request.POST['persons']
                infos = Info.objects.filter(name = user, department = department)
                salarys = Salary.objects.filter(info = infos)
            
    else:
        salarys = Salary.objects.all()
            
    return render(request,'allSalary.html', locals())

#更改个人密码    
@login_required
def ChangePass(request):
    
    welname = Welcome(request)
    
    if request.POST:
        if request.POST['pass'] == request.POST['password']:
            request.user.set_password(request.POST['pass'])
            request.user.save()
            return HttpResponseRedirect('/accounts/login/')
        else:
            error = "Not the same password.Please input again"
            
    return render(request,'changePass.html', locals())
    
#登入页面
@login_required    
def base(request):
    
    welname = Welcome(request)
    return render(request,'base.html',locals())

#个人信息
@login_required    
def SelfInfo(request):
    
    welname = Welcome(request)
    n = User.objects.get(username=request.user).info.id
    user = Info.objects.get(id=n)
    
    if request.POST:
        user.user.email = request.POST['email']
        user.user.save()
        user.save()
    
    return render(request,'SelfInfo.html', locals())

#全部员工信息   
@login_required
@permission_required('system.HR_permission', login_url='/accounts/login/')
def AllInfo(request):
    
    welname = Welcome(request)
    
    if request.POST:
        id = request.POST['id']
        uid = Info.objects.get(id=id).user.id
        #删除
        Info.objects.get(id=id).delete()
        User.objects.get(id=uid).delete()
        
        
    infos = Info.objects.all()
        
    return render(request,'AllInfo.html', locals())
 
#部门员工信息   
@login_required
def DepartInfo(request):
    
    welname = Welcome(request)
    department = User.objects.get(username=request.user).info.department
    infos = Info.objects.filter(department=department)
    return render(request,'DepartInfo.html', locals())
    

#添加员工，打印信息
@login_required
@permission_required('system.HR_permission', login_url='/accounts/login/')    
def AddClerk(request):
    
    welname = Welcome(request)
    years = range(1960, 2010)
    months = range(1, 13)
    dates = range(1, 32)
    posts = ['普通员工', '部门经理', '助理']
    departments = Department.objects.all()
    if request.POST:
        #获取信息
        name = request.POST['name']
        sex = request.POST['sex']
        department = Department.objects.get(dno = request.POST['department'])
        post = request.POST['post']
        bSalary = request.POST.get('bSalary', 0)
        email = request.POST['email']
        birth = request.POST['year'] + '-' + request.POST['month'] + '-' + request.POST['date']
        
        #添加到数据库
        user = User.objects.create(email = email)
        info = Info.objects.create(user = user,name = name, sex = sex, department = department, 
                                   post = post, bSalary = bSalary, birth = birth)
        
        #分配员工ID
        id = info.id
        user.username = '211312' + str(id)
        user.set_password('12345')
        user.save()
        department.save()
        colleagues = Info.objects.filter(department = department)
        #打印报道单
        return render(request,'printInfo.html', locals())
    
    return render(request,'addClerk.html', locals())

#管理员    
@login_required
@permission_required('system.Super_permission', login_url='/accounts/login/')  
def Administrator(request):
    
    return HttpResponseRedirect('/admin/')

#更改个人信息    
@login_required   
@permission_required('system.HR_permission', login_url='/accounts/login/')
def ChangeInfo(request, id):
    
    welname = Welcome(request)
    clerk = Info.objects.get(id=id)
    departments = Department.objects.all()
    if request.POST:
        #更改相关信息属性
        clerk.name = request.POST['name']
        clerk.sex = request.POST['sex']
        clerk.birth = request.POST['birth']
        clerk.user.email = request.POST['email']
        department = Department.objects.get(dno = request.POST['department'])
        clerk.department = department
        clerk.post = request.POST['post']
        clerk.bSalary = request.POST['bSalary']
        clerk.user.save()
        clerk.save()
        department.save()
        return HttpResponseRedirect('/allInfo/')
        
        
    return render(request,'changeInfo.html', RequestContext(request, locals()))
 
#历史薪资信息   
@login_required
def ShowSalary(request):
    welname = Welcome(request)
    i =  User.objects.get(username=request.user).info
    
    years = range(2010, 2021)
    months = range(1, 13)
    dates = range(1, 32)
    if request.POST:
        #查询一段时间薪资
        btime = request.POST['byear'] + '-' + request.POST['bmonth'] + '-' + request.POST['bdate']
        etime = request.POST['eyear'] + '-' + request.POST['emonth'] + '-' + request.POST['edate']
        records = Salary.objects.filter(info = i).exclude(date__lt = btime).exclude(date__gt = etime)
    else:
        records = Salary.objects.filter(info = i)
    
    return render(request,'showSalary.html', locals())
 
#个人本月薪资及影响薪资考勤记录   
@login_required
def MonthSalary(request):
    welname = Welcome(request)
    i =  User.objects.get(username=request.user).info
    
    time = timezone.localtime(timezone.now())
    month = time.month
    year = time.year
    begintime = str(year) + '-' + str(month) + '-' + '01'
    endtime = str(year) + '-' + str(month) + '-' + '31'
    
    lates = Check.objects.filter(info = i).filter(late=1).exclude(date__lt = begintime).exclude(date__gt = endtime)
    counts = lates.count()
    if counts == 0:
        salary = i.bSalary + 3000
    elif counts <= 3:
        salary = i.bSalary + (3 - counts) * 1000
    else:
        salary = i.bSalary
    return render(request,'monthSalary.html', locals())
 
 #录入考勤信息   
@login_required
@permission_required('system.HR_permission', login_url='/accounts/login/')
def CheckIn(request):
    
    welname = Welcome(request)
    years = range(2010, 2021)
    months = range(1, 13)
    dates = range(1, 32)
    usernames = User.objects.all()
    if request.POST:
        username = request.POST['username']
        date = request.POST['year'] + '-' + request.POST['month'] + '-' + request.POST['date']
        late = int(request.POST['late'])
        info = User.objects.get(username = username).info
        Check.objects.create(info = info, date = date, late = late)
    return render(request,'checkIn.html', locals())
    
#个人考勤信息
@login_required
def CheckInfo(request):
    
    welname = Welcome(request)
    info = User.objects.get(username=request.user).info
    years = range(2010, 2021)
    months = range(1, 13)
    dates = range(1, 32)
    
    if request.POST:
        btime = request.POST['byear'] + '-' + request.POST['bmonth'] + '-' + request.POST['bdate']
        
        etime = request.POST['eyear'] + '-' + request.POST['emonth'] + '-' + request.POST['edate']
        
        lates = Check.objects.filter(info = info).exclude(late=0).exclude(date__lt = btime).exclude(date__gt = etime)
    else:
        lates = Check.objects.filter(info = info).exclude(late=0)
    return render(request,'checkInfo.html', locals())
 
#部门薪资信息   
@login_required
@permission_required('system.department_manager', login_url='/accounts/login/')
def DepartmentalSal(request):
    
    welname = Welcome(request)
    #部门
    department = User.objects.get(username=request.user).info.department
    #部门员工
    infos = Info.objects.filter(department = department)
    salarys = []
    for i in infos:
        salarys.append(Salary.objects.filter(info=i))
    return render(request,'departmentalSal.html', locals())
    
    
 #部门考勤信息   
@login_required
@permission_required('system.department_manager', login_url='/accounts/login/')
def DepartmentalCheck(request):
    
    welname = Welcome(request)
    
    department = User.objects.get(username=request.user).info.department
    infos = Info.objects.filter(department = department)
    #统计缺勤人数
    number = 0
    checks = []
    years = range(2010, 2021)
    months = range(1, 13)
    dates = range(1, 32)
    if request.POST:
        btime = request.POST['byear'] + '-' + request.POST['bmonth'] + '-' + request.POST['bdate']
        
        etime = request.POST['eyear'] + '-' + request.POST['emonth'] + '-' + request.POST['edate']
        for i in infos:
            check = Check.objects.filter(info = i).exclude(late=0).exclude(date__lt = btime).exclude(date__gt = etime)
                
            if check:
                number += 1
                checks.append(check)
                
    else:
        for i in infos:
            check = Check.objects.filter(info = i).exclude(late=0)
            if check:
                number += 1
                checks.append(check)
                
    #按照迟到次数排序               
    checks.sort(key=lambda x: (-len(x)))
    
    
    return render(request,'departmentalCheck.html', locals())
    
        
   
#删除考勤记录
@login_required
@permission_required('system.HR_permission', login_url='/accounts/login/')
def DeleteCheck(request):
    
    if request.POST:
        Check.objects.get(id = request.POST['id']).delete()
        
    return HttpResponseRedirect('/departmentalCheck/')
    
 #更改考勤记录   
@login_required
@permission_required('system.HR_permission', login_url='/accounts/login/')
def ChangeCheck(request, id):
    
    welname = Welcome(request)
    check = Check.objects.get(id = id)
    if request.POST:
        
        check.date = request.POST['date']
        check.late = int(request.POST['late'])
        check.save()
        return HttpResponseRedirect('/departmentalCheck/')
    return render(request,'changeCheck.html', locals())
 
#计算月工资，录入当月薪资   
@login_required
@permission_required('system.HR_permission', login_url='/accounts/login/')
def CalculateSal(request):
    
    welname = Welcome(request)
    infos = Info.objects.all()
    #当前时间
    time = timezone.localtime(timezone.now())
    month = time.month
    year = time.year
    begintime = str(year) + '-' + str(month) + '-' + '01'
    endtime = str(year) + '-' + str(month) + '-' + '31'
    messages = []
    for info in infos:
        late = Check.objects.filter(info = info).filter(late=1).exclude(date__lt = begintime).exclude(date__gt = endtime)
        count = late.count()
        #满勤奖励5000， 缺勤一次奖励2000， 缺勤两次奖励1000， 缺勤大于等于三次无奖励
        if count == 0:
            salary = info.bSalary + 5000
        elif count <= 3:
            salary = info.bSalary + (3 - count) * 1000
        else:
            salary = info.bSalary
        messages.append({'late':late, 'count':count, 'salary':salary, 'info':info})
     
    if request.POST:
        for i in messages:
            s = Salary.objects.get(info = i['info'], date = request.POST['date'])
            #薪资信息存入数据库，存在则更新
            if s:
                
                s.salary = i['salary']
                s.save()
            else:
                #不存在则写入数据库
                salary.objects.create(info = i['info'], date = request.POST['date'], salary = i['salary'])
    return render(request,'calculateSal.html', locals())

#管理员更改密码
@login_required    
@permission_required('system.Super_permission', login_url='/accounts/login/')   
def Password(request):
    
    welname = Welcome(request)
    usernames = User.objects.all()
    if request.POST:
        #两次输入是否一致
        if request.POST['pass'] == request.POST['password']:
            u = User.objects.get(username=request.POST['username'])
            u.set_password(request.POST['pass'])
            u.save()
        else:
            error = "Not the same password.Please input again"
        
        
    return render(request,'password.html', locals())

#按角色搜索，经理可看薪资       
@login_required
def Search(request):
    welname = Welcome(request)
    info =  User.objects.get(username=request.user).info
    #判断部门
    department = Department.objects.get(dno = info.department)
    infos = []
    if request.POST:
        text = request.POST.get('text','')
        user = User.objects.filter(username = text)
        if user:
            if user[0].info.department == department:
                infos = user[0].info
            
                
    return render(request,'search.html', locals())
 
    
@login_required  
@permission_required('system.HR_permission', login_url='/accounts/login/')
#模糊查询，根据员工姓名，ID搜索全部员工
def SearchAll(request):
    
    welname = Welcome(request)
    
    if request.POST:
        #选择查询条件
        choice = request.POST['choices']
        text = request.POST['text']
        if choice == 'name':
            infos = Info.objects.filter(name__contains = text)
        else:
            users = User.objects.filter(username__contains = text)
            infos = Info.objects.filter(user = users)
        
    return render(request,'searchAll.html', locals())  

@login_required
@permission_required('system.Super_permission', login_url='/accounts/login/')
def SQL(request):
    welname = Welcome(request)
    if request.POST:
        show = '合法输入'
        text = request.POST.get('text').lower()
        maybe = re.search('master..sysprocesses|select|create|insert|and|or|shutdown|update|delete|drop|from|union|count|=|--|\*|\'|\;|\"\s*\"|\'\s*\'', text)
        # 'or '' = '    'or '1' = '1
        x = re.search('\'\s*or\s*\'*\s*[0-9a-zA-z]*\'*\s*[=<>]*\s*\'*[0-9a-zA-z]*\s*-*\s*', text)
        #';drop table users;--
        y = re.search('\s*\'\s*;\s*drop\s+table\s+[^)]+;\s*-*\s*', text)
        #';shutdown with nowait;--
        z = re.search('\s*\'\s*;\s*shutdown\s+with\s+nowait\s*;\s*-*\s*', text)
        #;and (select count(*) from admin)>0
        k = re.search('\s*;?\s*and\s*\(select\s+count\(\*\)\s+from\s+[^)]+\)\s*>=?\s*\d+', text)
        if maybe:
            show = '可能存在sql注入'
            if x or y or z or k:
                show = '存在sql注入'
    return render(request,'sql.html', locals())






    