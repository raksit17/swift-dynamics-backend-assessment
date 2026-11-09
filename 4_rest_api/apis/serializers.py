from rest_framework import serializers
from .models import Classroom, School, Student, Teacher


class SchoolSerializer(serializers.ModelSerializer):
    classroom_count = serializers.IntegerField(read_only=True)
    teacher_count = serializers.IntegerField(read_only=True)
    student_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = School
        fields = ("id", "name", "abbreviation", "address", "classroom_count", "teacher_count", "student_count")


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ("id", "school", "grade", "section", "teachers", "students")
        read_only_fields = ("teachers", "students")


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("id", "firstname", "lastname", "gender", "classrooms")


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "firstname", "lastname", "gender", "classroom")
