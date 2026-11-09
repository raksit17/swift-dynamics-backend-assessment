from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from apis.filters import SchoolFilter
from apis.models import School
from apis.serializers import SchoolSerializer


class SchoolViewSet(ModelViewSet):
    queryset = School.objects.order_by("pk")
    serializer_class = SchoolSerializer
    filterset_class = SchoolFilter

    def get_queryset(self):
        schools = super().get_queryset()
        if self.action == "retrieve":
            return schools.annotate(classroom_count=Count("classrooms", distinct=True),
                                    student_count=Count("classrooms__students", distinct=True),
                                    teacher_count=Count("classrooms__teachers", distinct=True))
        return schools
