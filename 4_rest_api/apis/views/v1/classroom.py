from rest_framework.viewsets import ModelViewSet
from apis.models import Classroom
from apis.serializers import ClassroomSerializer


class ClassroomViewSet(ModelViewSet):
    queryset = Classroom.objects.prefetch_related("teachers", "students").order_by("pk")
    serializer_class = ClassroomSerializer
    filterset_fields = ("school",)
