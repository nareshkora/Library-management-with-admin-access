

from django.db import models



# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.course_name


class Books(models.Model):
    book_name = models.CharField(max_length=60)
    author_name = models.CharField(max_length=80)
    course_name = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book_name}'


class Student(models.Model):
    stud_name = models.CharField(max_length=50, default=None)
    stud_password = models.CharField(max_length=50, default='12345')
    stud_phno = models.BigIntegerField(default=None)
    stud_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    stud_semester = models.IntegerField(default=None)

    def __str__(self):
        return f'{self.stud_name}'


class issue_book(models.Model):
    stud_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    book_name = models.ForeignKey(Books, on_delete=models.CASCADE)
    start_date = models.DateField(default=None)
    end_date = models.DateField(default=None)





