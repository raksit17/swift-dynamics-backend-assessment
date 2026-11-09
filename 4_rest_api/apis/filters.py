import django_filters as filters
from .models import School, Student, Teacher


class SchoolFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = School
        fields = ("name",)


class PersonFilter(filters.FilterSet):
    firstname = filters.CharFilter(lookup_expr="icontains")
    lastname = filters.CharFilter(lookup_expr="icontains")
    gender = filters.CharFilter(lookup_expr="iexact")


class TeacherFilter(PersonFilter):
    school = filters.NumberFilter(field_name="classrooms__school_id", distinct=True)
    classroom = filters.NumberFilter(field_name="classrooms__id")

    class Meta:
        model = Teacher
        fields = ("school", "classroom", "firstname", "lastname", "gender")


class StudentFilter(PersonFilter):
    school = filters.NumberFilter(field_name="classroom__school_id")

    class Meta:
        model = Student
        fields = ("school", "classroom", "firstname", "lastname", "gender")
