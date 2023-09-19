from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers
from rest_framework import generics


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = models.StudentData.objects.all()
    serializer_class = serializers.StudentSerializer


class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudentData.objects.all()
    serializer_class = serializers.StudentSerializer

# class StudentView(APIView):
#     def get(self, request):
#         student_data = models.StudentData.objects.all()
#         serializer = serializers.StudentSerializer(student_data, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = serializers.StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SnippetDetailDetail(APIView):
#     def get(self, request, pk, format=None):
#         snippet = models.StudentData.objects.get(pk=pk)
#         serializer = serializers.StudentSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = models.StudentData.objects.get(pk=pk)
#         serializer = serializers.StudentSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = models.StudentData.objects.get(pk=pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
