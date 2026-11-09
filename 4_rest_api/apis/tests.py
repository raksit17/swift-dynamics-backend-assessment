from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase


class SchoolDirectoryTests(APITestCase):
    def setUp(self):
        self.client.force_authenticate(get_user_model().objects.create_user("reviewer"))

    def create(self, resource, **data):
        response = self.client.post(f"/api/v1/{resource}/", data, format="json")
        self.assertEqual(response.status_code, 201, response.data)
        return response.data["id"]

    def test_directory_workflow(self):
        school = self.create("schools", name="North", abbreviation="N", address="Main St")
        rooms = [self.create("classrooms", school=school, grade=1, section=n) for n in (1, 2)]
        teacher = self.create("teachers", firstname="Ann", lastname="Lee", gender="female", classrooms=rooms)
        student = self.create("students", firstname="Sam", lastname="Tan", gender="male", classroom=rooms[0])

        school_detail = self.client.get(f"/api/v1/schools/{school}/").data
        self.assertEqual([school_detail[k] for k in ("teacher_count", "classroom_count", "student_count")], [1, 2, 1])
        self.assertEqual(self.client.get(f"/api/v1/classrooms/{rooms[0]}/").data["teachers"], [teacher])
        self.assertEqual(self.client.get("/api/v1/teachers/", {"school": school, "firstname": "an"}).data[0]["id"], teacher)
        self.assertEqual(self.client.get("/api/v1/students/", {"classroom": rooms[1]}).data, [])

        moved = self.client.patch(f"/api/v1/students/{student}/", {"classroom": rooms[1]}, format="json")
        self.assertEqual(moved.status_code, 200)
        self.assertEqual(self.client.get(f"/api/v1/classrooms/{rooms[1]}/").data["students"], [student])
        self.assertEqual(self.client.delete(f"/api/v1/teachers/{teacher}/").status_code, 204)
        self.assertEqual(self.client.get(f"/api/v1/schools/{school}/").data["teacher_count"], 0)
