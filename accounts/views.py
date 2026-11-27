from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView
from rest_framework import authentication,permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.serializers import TrainerSerializer,TrainerProfileSerializer,StudentSerializer,StudentProfileSerializer
from accounts.models import TrainerProfile,StudentProfile

class TrainerSignUpView(CreateAPIView):

    serializer_class = TrainerSerializer


class TrainerProfileRetrieveUpdateView(APIView):



    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        auth_user = request.user

        qs = TrainerProfile.objects.get(user=auth_user)

        serializer_instance = TrainerProfileSerializer(qs)

        return Response(serializer_instance.data)

    def put(self,request):

       form_data = request.data

       instance = TrainerProfile.objects.get(user=request.user)

       serializer_instance = TrainerProfileSerializer(data=form_data,instance=instance)

       if serializer_instance.is_valid():

           serializer_instance.save()

           return Response(serializer_instance.data)

       else:

           return Response(serializer_instance.errors)

           

class StudentSignUpView(CreateAPIView):

    serializer_class = StudentSerializer


class StudentProfileRetrieveUpdateView(RetrieveAPIView,UpdateAPIView):

    serializer_class = StudentProfileSerializer

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return StudentProfile.objects.get(user=self.request.user)

    