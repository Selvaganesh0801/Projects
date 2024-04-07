from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .models import User, Role
from .serializer import UserSerializer, RoleSerializer


# User Crud App Start

# User Get Method start
@api_view(['GET'])
def UserDetail(request):
    obj = User.objects.all()
    serializer = UserSerializer(obj, many=True)
    msg = {'code': status.HTTP_200_OK, 'msg': "Data Get Successfully", 'data': serializer.data}
    return Response(msg, status.HTTP_200_OK)

# User Get Method End

# User Get Method get Only Single Value
class UserInfo(APIView):
    def get(self, request, id):
        try:
            obj=User.objects.get(id=id)
            serializer = UserSerializer(obj)
            msg = {'code': status.HTTP_200_OK, 'msg': 'Datas Get Successfully', 'data': serializer.data,}
            return Response(msg, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            msg={'code': status.HTTP_400_BAD_REQUEST, 'msg': 'Data Not Found'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

# User Create Method Start

class UserPost(APIView):
        def post(self, request):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data.get('email')
                phone_no = serializer.validated_data.get('phone_no')
                if User.objects.filter(email=email, phone_no=phone_no).exists():
                    msg = {"code": status.HTTP_400_BAD_REQUEST, 'msg': 'Email id Already Existing'}
                    return Response(msg, status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                msg = {"code": status.HTTP_201_CREATED, 'msg': 'User_Data Created Successfully',
                       'data': serializer.data}
                return Response(msg, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Create Method End

# User Update Method Start

class userUpdate(APIView):
    def put(self,request):
        try:
            id = request.data.get('id')
            obj = User.objects.get(id=id)
            obj1 = UserSerializer(obj, data=request.data)
            if obj1.is_valid():
                obj1.save()
                msg = {"code": status.HTTP_201_CREATED, "msg": "Data Updated Successfully", "data": obj1.data}
                return Response(msg,status=status.HTTP_205_RESET_CONTENT)
        except User.DoesNotExist:
            msg = {"code": status.HTTP_404_NOT_FOUND, "msg": "Invalid ID"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

# User Update Method End

# User Delete Method Start
class userDelete(APIView):
    def delete(self, request, id):
        try:
            obj = User.objects.get(id=id)
            obj.delete()
            msg = {"code": status.HTTP_204_NO_CONTENT, "msg": "Datas Deleted Successfully"}
            return Response(msg, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            msg = {"code": status.HTTP_404_NOT_FOUND, "msg": "Data Deleted Successfully"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

# User Delete Method End

# User Crud App Methods End



# Role Crud App Start

# Role Get Method Start

class RoleDetails(APIView):
    def get(self, request):
        obj = Role.objects.all()
        serializer = RoleSerializer(obj, many=True)
        msg = {'code': status.HTTP_200_OK, 'msg': "Data Fetched Successfully", 'data': serializer.data}
        return Response(msg, status.HTTP_200_OK)

# Role Get Method End

# Role Get Method to get Single Value

class RoleInfo(APIView):
    def get(self, request, id):
        try:
            obj=Role.objects.get(id=id)
            serializer = RoleSerializer(obj)
            msg = {'code': status.HTTP_200_OK, 'msg': 'User Details Fetched Successfully', 'data': serializer.data,}
            return Response(msg, status=status.HTTP_200_OK)
        except Role.DoesNotExist:
            msg={'code': status.HTTP_400_BAD_REQUEST, 'msg': 'Data Not Found'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

# Role Get Method End

# Role Create Method Start

class RolePost(APIView):
        def post(self, request):
            serializer = RoleSerializer(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data.get('email')
                phone_no = serializer.validated_data.get('phone_no')
                if Role.objects.filter(email=email, phone_no=phone_no).exists():
                    msg = {"code": status.HTTP_400_BAD_REQUEST, 'msg': 'Email id Already Existing'}
                    return Response(msg, status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                msg = {"code": status.HTTP_201_CREATED, 'msg': 'User Data Created Successfully',
                       'data': serializer.data}
                return Response(msg, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Role Create Method End

# Role Updated Method Start

class RoleUpdate(APIView):
    def put(self,request):
        try:
            id = request.data.get('id')
            obj = Role.objects.get(id=id)
            obj1 = RoleSerializer(obj, data=request.data)
            if obj1.is_valid():
                obj1.save()
                msg = {"code": status.HTTP_201_CREATED, "msg": "User Data Updated Successfully", "data": obj1.data}
                return Response(msg,status=status.HTTP_200_OK)
        except Role.DoesNotExist:
            msg = {"code": status.HTTP_400_BAD_REQUEST, "msg": "Invalid ID"}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

# Role Update Method End

# Role Delete Method Start

class RoleDelete(APIView):
    def delete(self, request, id):
        try:
            obj = Role.objects.get(id=id)
            obj.delete()
            msg = {"code": status.HTTP_204_NO_CONTENT, "msg": "Datas Deleted Successfully"}
            return Response(msg, status=status.HTTP_200_OK)
        except Role.DoesNotExist:
            msg = {"code": status.HTTP_404_NOT_FOUND, "msg": "Data Deleted Successfully"}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

# Role Delete Method End

# Role Crud Methods End
