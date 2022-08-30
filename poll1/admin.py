from django.contrib import admin
from . models import *
# Register your models here.
class stu(admin.ModelAdmin):
    list_display = ('user_name','question_text','pub_date','ch1','ch2','ch3','ch4','vote1','vote2','vote3','vote4')
admin.site.register(ques,stu)