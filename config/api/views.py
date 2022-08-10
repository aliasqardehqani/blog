from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeleteAccount(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def delete(self, request, id):
    #     if request.method == 'POST':
    #         user = User.objects.get(id=id)
    #         user.delete()

    def delete(self, request, pk):
        if request.user.is_active and request.user.is_authenticated:
            query = User.objects.get(pk=pk)
            query.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return HttpResponse('You must first arrive at join...')
