from rest_framework.viewsets import ModelViewSet
from apis.filters import StudentFilter
from apis.models import Student
from apis.serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.order_by("pk")
    serializer_class = StudentSerializer
    filterset_class = StudentFilter
