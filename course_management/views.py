from django.shortcuts import render,get_object_or_404

# Create your views here.
# from rest_framework.generics import ListAPIView
from rest_framework import authentication,permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from course_management.serializers import CourseSerializers
from course_management.models import Course

from accounts.permissions import IsOwner

class CourseListCreateView(APIView):

    # serializer_class = CourseSerializers

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    # def get_queryset(self):
    #     return Course.objects.filter(trainer=self.request.user)

    def get(self,request):

        qs = Course.objects.filter(trainer=request.user)

        serializer_instance = CourseSerializers(qs,many=True)

        return Response(serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serializer_instance = CourseSerializers(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(trainer=request.user)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)

class CourseRetrieveUpdateDeleteView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwner]

    def get(self,request,pk=None):

        qs = get_object_or_404(Course,id=pk)

        self.check_object_permissions(request,qs)

        serializer_instance = CourseSerializers(qs)

        return Response(serializer_instance.data)

    def put(self,request,pk=None): # patch(self,req.....)

        form_data = request.data

        instance = get_object_or_404(Course,id=pk)

        self.check_object_permissions(request,instance)

        serializer_instance = CourseSerializers(data=form_data,instance=instance) #,partial=True

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)

    def delete(self,request,pk=None):

        instance = get_object_or_404(Course,id=pk)

        self.check_object_permissions(request,instance)

        instance.delete()

        return Response({"message":"deleted........."})

    

        