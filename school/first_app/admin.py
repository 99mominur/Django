from django.contrib import admin
from first_app.models import StudentModel, StudentInfoModel, TeacherInfoModel, EmployeeModel, ManagerModel, Friend, Me, Person, Passport, Post, Student, Teacher
# Register your models here.

# admin.site.register(StudentModel)
# admin.site.register(StudentInfoModel)
# admin.site.register(TeacherInfoModel)
# # admin.site.register(EmployeeModel)
# # admin.site.register(ManagerModel)


# @admin.register(EmployeeModel)
# class EmployeeModelAdmin(admin.ModelAdmin):
#     list_display = ["id", "name", "city", "designation"]


# @admin.register(ManagerModel)
# class ManagerModelAdmin(admin.ModelAdmin):
#     list_display = ["id", "name", "city",
#                     "designation", "take_interview", "hiring"]


# @admin.register(Friend)
# class FriendModelAdmin(admin.ModelAdmin):
#     list_display = ["name", "section", "attendence"]


# @admin.register(Me)
# class MeModelAdmin(admin.ModelAdmin):
#     list_display = ["name", "section", "attendence"]


# @admin.register(Person)
# class PersonModelAdmin(admin.ModelAdmin):
#     list_display = ["id", "name", "city", "email"]


# @admin.register(Passport)
# class PassportModelAdmin(admin.ModelAdmin):
#     list_display = ["id", "user", "pass_number", "page", "validity"]


# @admin.register(Post)
# class PosttModelAdmin(admin.ModelAdmin):
#     list_display = ["id", "user", "post_cap", "post_details"]

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "class_name"]


@admin.register(Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "subject", "age", "student_list"]
