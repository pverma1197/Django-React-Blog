from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, BlogSerializer
from django.core.mail import send_mail
from django.conf import settings
from .models import Blog


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        # username = request.user.id
        # print(username)
        return Response(content)


# User Registration api
class UserRegister(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # mail sending code
            user_name = request.data['username']
            subject = "Register Successful Mail"
            msg = "Hello  " + user_name + "! , you are successful register in our website. Hope you are enjoy blog reading."
            to = request.data['email']
            send_email = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
            response_msg = {'message': 'User register Sucessfully'}
            return Response(response_msg, content_type='application/json')
        return Response(serializer.errors)


# Blog create API
class CreateBlog(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.data["user"] = request.user.id
        serializer = BlogSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            # a = serializer.data['tags']
            # print(type(a))
            response_msg = {'message': 'Blog add Sucessfully'}
            return Response(response_msg, content_type='application/json')
        return Response(serializer.errors)


# Get Blog data API
class GetBlog(APIView):

    def get(self, request):
        items = Blog.objects.all()
        serializer = BlogSerializer(items, many=True)
        return Response(serializer.data)
