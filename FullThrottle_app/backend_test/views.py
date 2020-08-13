from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import User, ActivityPeriod
from . serializers import UserDataSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html')

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserDataSerializer(users, many=True)
        response = {'ok':True, 'members' : serializer.data}
        return Response(response)
           