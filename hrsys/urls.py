#coding:utf-8
"""hrsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #登入
    url(r'^accounts/login/$', 'system.views.login'),
    #登出
    url(r'^accounts/logout/$', 'system.views.logout'),
    
    url(r'^base/$', 'system.views.base'),
    #个人信息
    url(r'^selfInfo/$', 'system.views.SelfInfo'),
    #所有员工信息,修改，删除
    url(r'^allInfo/$', 'system.views.AllInfo'),
    #部门员工信息
    url(r'^departInfo/$', 'system.views.DepartInfo'),
    #更改密码
    url(r'^changePass/$', 'system.views.ChangePass'),
    
    url(r'^password/$', 'system.views.Password'),
    #添加员工+ 打印资料
    url(r'^addClerk/$', 'system.views.AddClerk'),  
    #安全管理
    url(r'^administrator/$', 'system.views.Administrator'),
    #修改资料
    url(r'^changeInfo/(\d{1,5})/$', 'system.views.ChangeInfo'),
    #历史薪资
    url(r'^showSalary/$', 'system.views.ShowSalary'),
    #考勤登记
    url(r'^checkIn/$', 'system.views.CheckIn'),
    #个人考勤信息
    url(r'^checkInfo/$', 'system.views.CheckInfo'), 
    #部门薪资
    url(r'^departmentalSal/$', 'system.views.DepartmentalSal'), 
    #部门考勤信息
    url(r'^departmentalCheck/$', 'system.views.DepartmentalCheck'), 
    #计算月工资
    url(r'^calculateSal/$', 'system.views.CalculateSal'),
    #本月工资
    url(r'^monthSalary/$', 'system.views.MonthSalary'),
    #全部员工工资
    url(r'^allSalary/$', 'system.views.AllSalary'),
    
    url(r'^deleteCheck/$', 'system.views.DeleteCheck'), 
    
    url(r'^changeCheck/(\d{1,5})/$', 'system.views.ChangeCheck'),

    
    
    #搜索部门员工
    url(r'^search/$', 'system.views.Search'), 
    #搜索全部员工
    url(r'^searchAll/$', 'system.views.SearchAll'), 
    url(r'^sql/$', 'system.views.SQL'),
    
    
]
from django.conf import settings
if not settings.DEBUG:
    from django.views import static
    urlpatterns += [
                    url(r'^static/(?P<path>.*)$', static.serve, {'document_root':settings.STATIC_ROOT}),
                    #url(r'^images/(?P<path>.*)$', static.serve, {'document_root':settings.STATIC_ROOT}),
                    
                    
                    
                    ]