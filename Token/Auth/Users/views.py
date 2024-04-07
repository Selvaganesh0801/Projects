from knox.auth import AuthToken
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializer import RegisterSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from knox.views import LogoutView as KnoxLogoutView


@api_view(['POST'])

def register_Api(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    custom_response = {
        "code": "200",
        "status": "OK",
        "message": "Registration Successfully",
    }

    return Response(custom_response, status=status.HTTP_200_OK)


@api_view(['POST'])

def login_Api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    created, token = AuthToken.objects.create(user)
    custom_response = {
        "code": "200",
        "status": "OK",
        "message": "Login Successfully",
        "responseData": {
            "token": token,
            "userDetail": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }
        }
    }

    return Response(custom_response, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_userdata(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            "user_info": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            },
        })
    return Response({'Error!': "Not Authenticated"}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
#
# def get_userdata(request):
#     user = request.user
#
#     if user.is_authenticated:
#         return Response({
#             "user_info": {
#                 "id": user.id,
#                 "username": user.username,
#                 "email": user.email
#             },
#         })
#     return Response({'Error!': "Not Authenticated"}, status=400)




class LogoutView(KnoxLogoutView):
    def post(self, request, format=None):
        request._auth.delete()

        custom_response = {
            "code": "200",
            "status": "OK",
            "message": "Logout Successfully",
        }

        return Response(custom_response, status=status.HTTP_200_OK)
