from django.contrib import admin
from libraryapp.models import Books, Course, issue_book, Student
# Register your models here.

admin.site .register(Course)
admin.site .register(Books)
admin.site .register(issue_book)
admin.site .register(Student)