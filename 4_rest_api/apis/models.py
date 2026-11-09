from django.db import models


class School(models.Model):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=30)
    address = models.TextField()


class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="classrooms")
    grade = models.PositiveSmallIntegerField()
    section = models.PositiveSmallIntegerField()

    class Meta:
        constraints = [models.UniqueConstraint(fields=["school", "grade", "section"],
                                                name="unique_room_in_school")]


class Person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=40)

    class Meta:
        abstract = True


class Teacher(Person):
    classrooms = models.ManyToManyField(Classroom, related_name="teachers", blank=True)


class Student(Person):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="students")
