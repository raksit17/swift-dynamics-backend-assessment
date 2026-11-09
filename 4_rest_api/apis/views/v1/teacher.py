from rest_framework.viewsets import ModelViewSet
from apis.filters import TeacherFilter
from apis.models import Teacher
from apis.serializers import TeacherSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.prefetch_related("classrooms").order_by("pk")
    serializer_class = TeacherSerializer
    filterset_class = TeacherFilter
