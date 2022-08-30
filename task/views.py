from collections import UserList
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import UserSerializer
from . models import UserData
from task import serializers
from rest_framework.pagination import PageNumberPagination
# Create your views here.

@api_view(['GET'])
def showUserList(request):
    paginator = PageNumberPagination()
    paginator.page_size = 5
    userList=UserData.objects.all()
    result_page = paginator.paginate_queryset(userList, request)
    serializer=UserSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def UserDetails(request,pk):
    userList=UserData.objects.get(id=pk)
    seriaizer=UserSerializer(userList,many=False)
    return Response(seriaizer.data)

@api_view(['POST'])
def CreateUserList(request):
    serializers=UserSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def UpdateList(request, pk):
    userList=UserData.objects.get(id=pk)
    serializer=UserSerializer(instance=userList, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteUser(request, pk):
    userList=UserData.objects.get(id=pk)
    userList.delete()

    return Response('User Deleted')

