from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import UserSerializer, ExerciseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Exercises, UserPlan
from django.core.exceptions import ObjectDoesNotExist
import jwt
from workoutapi.settings import SIMPLE_JWT

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

""" Exercise View """


class ExerciseView(APIView):
    def get(self, request):
        exercises = Exercises.objects.all()

        return Response(ExerciseSerializer(exercises, many=True).data)


""" User Plan View """


class UserPlanView(APIView):

    def post(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed("Unauthenticated user!")
        try:
            payload = jwt.decode(token, SIMPLE_JWT['SIGNING_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated user!")

        user = User.objects.filter(pk=payload['user_id']).first()

        exercises = request.data['exercises']
        frequency = request.data['frequency']
        goals = request.data['goals']
        exercise_type = request.data['exercise_type']
        daily_duration = request.data['daily_duration']

        if UserPlan.objects.filter(user=user):
            return Response({'message': 'User plan already exists!'})

        user_choice = UserPlan.objects.create(user=user,
                                              frequency=frequency,
                                              goals=goals,
                                              exercise_type=exercise_type,
                                              daily_duration=daily_duration)
        exercises_lst = []
        for exercise in exercises:
            try:
                ex = Exercises.objects.get(name__contains=exercise)
                user_choice.exercises.add(ex)
            except ObjectDoesNotExist:
                exercises_lst.append(exercise)
        user_choice.save()

        if len(exercises_lst) == 0:
            return Response({"message": f"User plan added successfully!"})
        else:
            return Response({"message": f"User plan added successfully! but {exercises_lst} not added because we can't find it"})

    def put(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed("Unauthenticated user!")
        try:
            payload = jwt.decode(token, SIMPLE_JWT['SIGNING_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated user!")

        user = User.objects.filter(pk=payload['user_id']).first()

        exercises = request.data['exercises']
        frequency = request.data['frequency']
        goals = request.data['goals']
        exercise_type = request.data['exercise_type']
        daily_duration = request.data['daily_duration']

        user_choice = UserPlan.objects.get(user=user)

        user_choice.frequency = frequency
        user_choice.goals = goals
        user_choice.exercise_type = exercise_type
        user_choice.daily_duration = daily_duration

        exercises_lst = []
        for exercise in exercises:
            try:
                ex = Exercises.objects.get(name__contains=exercise)
                user_choice.exercises.add(ex)
            except ObjectDoesNotExist:
                exercises_lst.append(exercise)
        user_choice.save()

        if len(exercises_lst) == 0:
            return Response({"message": f"User plan updated successfully!"})
        else:
            return Response({"message": f"User plan updated successfully! but {exercises_lst} not added because we can't find it"})
