# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from .models import Project
# from .serializer import ProjectSerializer
#
# # Create your views here.
#
# class projectGet(APIView):
#     def get(self,request):
#         obj=Project.objects.all()
#         obj1=ProjectSerializer(obj,many=True)
#         msg={"CODE":status.HTTP_200_OK,"msg":"Successfully Datas GET","data":obj1.data}
#         return Response(msg,status=status.HTTP_200_OK)
#
# class projectPost(APIView):
#     def post(self,request):
#         obj1=ProjectSerializer(data=request.data)
#         if obj1.is_valid():
#             obj1.save()
#             msg={"CODE":status.HTTP_201_CREATED,"msg":"Successfully Datas CREATED","data":obj1.data}
#             return Response(msg,status=status.HTTP_201_CREATED)
