from rest_framework import serializers
from . import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = models.StudentData
        fields = "__all__"
