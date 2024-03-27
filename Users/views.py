from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from .serializers import *
from .models import *

@api_view(['POST'])
class RegistrationView(APIView):
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'message': 'User Created'
                }
                return Response(json_data, status=status.HTTP_200_OK)
            else :
                json_data = {
                    'status_code': 200,
                    'status': 'fail',
                    'data': 'data not valid'
                }
                return Response(json_data, status=status.HTTP_200_OK)
        except Exception as e:
            print("Error --------:", e)
            json_data = {
                'status_code': 400,
                'status': 'Fail',
                'Reason': e,
                'Remark': 'landed in exception',
            }
            raise APIException(json_data, code=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
class VerificationView(APIView):
    def post(self, request):
        try:
            serializer = VerificationSerializer(data=request.data)
            if serializer.is_valid():
                email_or_username = serializer.email_or_username('email_or_username')
                password = serializer.otp('password')

                email = User.email
                oldpassword = User.password

                if email_or_username == email and password == oldpassword :
                    json_data = {
                        'status_code': 200,
                        'status': 'Success',
                        'message': 'User Verified'
                    }
                    return Response(json_data, status=status.HTTP_200_OK)
                else :
                    json_data = {
                    'status_code': 200,
                    'status': 'fail',
                    'data': 'User Not Verified'
                }
                return Response(json_data, status=status.HTTP_200_OK)
            else :
                json_data = {
                    'status_code': 200,
                    'status': 'fail',
                    'data': 'data not valid'
                }
                return Response(json_data, status=status.HTTP_200_OK)
          
        except Exception as e:
            print("Error --------:", e)
            json_data = {
                'status_code': 400,
                'status': 'Fail',
                'Reason': e,
                'Remark': 'landed in exception',
            }
            raise APIException(json_data, code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


@api_view(['POST'])
class LoginView(APIView):
    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            refresh = RefreshToken.for_user(user)
            if serializer.is_valid():
                email_or_username = serializer.email_or_username('email_or_username')
                password = serializer.otp('password')

                user = authenticate(request, username=email_or_username, password=password)
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'message': 'User login Sucessfull'
                }
                return Response(json_data, status=status.HTTP_200_OK)
            else :
                json_data = {
                    'status_code': 200,
                    'status': 'fail',
                    'data': 'Please Enter valid Credentials'
                }
                return Response(json_data, status=status.HTTP_200_OK)
        except Exception as e:
                print("Error --------:", e)
                json_data = {
                    'status_code': 400,
                    'status': 'Fail',
                    'Reason': e,
                    'Remark': 'landed in exception',
                }
                raise APIException(json_data, code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
class ForgotPasswordView(APIView):
    def post(self, request):
        try:
            serializer = ForgotPasswordSerializer(data=request.data)
            if serializer.is_valid():
                if serializer.email_or_username == User.email:
                    json_data = {
                        'status_code': 200,
                        'status': 'Success',
                        'message': 'User Found'
                    }
                    return Response(json_data, status=status.HTTP_200_OK)
            else :
                json_data = {
                    'status_code': 200,
                    'status': 'fail',
                    'data': 'data not valid'
                }
                return Response(json_data, status=status.HTTP_200_OK)
          
        except Exception as e:
            print("Error --------:", e)
            json_data = {
                'status_code': 400,
                'status': 'Fail',
                'Reason': e,
                'Remark': 'landed in exception',
            }
            raise APIException(json_data, code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


@api_view(['POST'])
class ResetPasswordView(APIView):
    def post(self, request):
        try:
            serializer = ResetPasswordSerializer(data=request.data)
            if serializer.is_valid():
                if serializer.email_or_username == User.email and serializer.otp == User.otp:
                    User.password = serializer.new_password
                    json_data = {
                        'status_code': 200,
                        'status': 'Success',
                        'message': 'User Password nreset Sucessful'
                    }
                    return Response(json_data, status=status.HTTP_200_OK)
            else :
                json_data = {
                    'status_code': 200,
                    'status': 'fail',
                    'data': 'data not valid'
                }
                return Response(json_data, status=status.HTTP_200_OK)
          
        except Exception as e:
            print("Error --------:", e)
            json_data = {
                'status_code': 400,
                'status': 'Fail',
                'Reason': e,
                'Remark': 'landed in exception',
            }
            raise APIException(json_data, code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        