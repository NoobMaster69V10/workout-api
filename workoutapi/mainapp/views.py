from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User

""" Authentication/Registration/Logout Views """


class RegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "User created successfully"})


#########################
class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed("User not found!")
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")

        refresh = RefreshToken.for_user(user)

        response = Response()

        response.set_cookie(key='jwt', value=str(refresh.access_token), httponly=True)
        response.data = {
            "jwt": str(refresh.access_token),
            'refresh': str(refresh),
        }

        return response


#########################
class LogoutView(APIView):
    def post(self, request):
        if request.COOKIES.get('jwt') is not None:

            response = Response()
            response.delete_cookie('jwt')
            response.data = {
                'message': 'Successfully logged out'
            }
            return response
        else:
            return Response({'message': 'Not authenticated'})


#########################

