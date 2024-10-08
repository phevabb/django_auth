

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework.exceptions import ValidationError

from .models import User, UserToken
from core.serializers import UserSerializer
from django.contrib.auth.hashers import make_password
from .authentication import JWTAuthentication, create_access_token, create_refresh_token, decode_refresh_token
import jwt, datetime

# Create your views here.
class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        if data['password'] != data['confirm_password']:
            raise exceptions.APIException('Passwords do not match!')

        hashed_password = make_password(data['password'])
        data['password']  = hashed_password
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            raise ValidationError(serializer.errors)

class LoginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        if user is None:
            raise exceptions.APIException('invalid credentials')

        if not user.check_password(password):
            raise exceptions.APIException('invalid credentials')

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        UserToken.objects.create(
            user_id=user.id,
            refresh_token=refresh_token,
            expires_at=datetime.datetime. now(datetime. UTC) + datetime.timedelta(days=7)
        )

        response = Response()

        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
        response.data = {
            'access_token': access_token,
        }
        return response

class userAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        return Response(UserSerializer(request.user).data)



class RefreshAPIView(APIView):

    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        id = decode_refresh_token(refresh_token)

        if not UserToken.objects.filter(
            user_id=id,
            refresh_token=refresh_token,
            expires_at__gt=datetime.datetime. now( tz=datetime. UTC)
            ).exists():
            raise exceptions.AuthenticationFailed('unauthenticated')

        access_token = create_access_token(id)
        return Response({'access_token': access_token})

class LogoutAPIView(APIView):


    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        UserToken.objects.filter(refresh_token=refresh_token).delete()
        response = Response()
        response.delete_cookie('refresh_token')
        response.data = {
            'message': 'Successfully logged out.'
        }

        return response


