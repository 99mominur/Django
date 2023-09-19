from django.contrib import admin
from first_app.models import StudentModel, StudentInfoModel, TeacherInfoModel, Employee, Manager, Friend, Me
# Register your models here.

admin.site.register(StudentModel)
# admin.site.register(StudentInfoModel)
# admin.site.register(TeacherInfoModel)


@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'designation', 'address']


@admin.register(Manager)
class ManagerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'designation',
                    'hiring', 'take_interview', 'address']


@admin.register(Friend)
class FriendModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'attendence', 'hw']


@admin.register(Me)
class FriendModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'attendence', 'hw']
