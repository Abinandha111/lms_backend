from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication,permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from course_management.serializers import CourseSerializers
from course_management.models import Course

from accounts.permissions import IsOwner

class CourseListCreateView(ListAPIView,CreateAPIView):

    serializer_class = CourseSerializers

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return Course.objects.filter(trainer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(trainer = self.request.user)

class CourseRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    queryset = Course.objects.all()

    serializer_class = CourseSerializers

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwner]


    

    

    

        