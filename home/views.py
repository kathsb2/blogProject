from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BlogSerializer, CommentSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Blog, Comment
from django.db.models import Q

# Create your views here.

class SingleBlogView(APIView):

    def get(self, request, id):
        try:
                blogs = Blog.objects.filter(uid=id)
                serializer = BlogSerializer(blogs, many = True)

                return Response({
                    'data': serializer.data,
                    'message': 'Success!',
                }, status = status.HTTP_200_OK)



        except Exception as e:
            print(e)

            return Response({
                'data': {},
                'message': 'Something went wrong',
            }, status = status.HTTP_400_BAD_REQUEST)

class PublicBlogView(APIView):

    def get(self, request):
        try:
            blogs = Blog.objects.all()
            serializer = BlogSerializer(blogs, many = True)

            return Response({
                'data': serializer.data,
                'message': 'Success!',
            }, status = status.HTTP_200_OK)

        except Exception as e:
            print(e)

            return Response({
                'data': serializer.errors,
                'message': 'Something went wrong',
            }, status = status.HTTP_400_BAD_REQUEST)


class BlogView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            data = request.data
            data['user'] = request.user.id
            serializer = BlogSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Something went wrong',
                }, status = status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response({
                'data': serializer.data,
                'message': 'Post Created!',
            }, status = status.HTTP_201_CREATED)

        except Exception as e:
            print(e)

            return Response({
                'data': {},
                'message': 'Something went wrong',
            }, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
                blogs = Blog.objects.filter(user=request.user)
                serializer = BlogSerializer(blogs, many = True)

                return Response({
                    'data': serializer.data,
                    'message': 'Success!',
                }, status = status.HTTP_200_OK)



        except Exception as e:
            print(e)

            return Response({
                'data': {},
                'message': 'Something went wrong',
            }, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            data = request.data

            blog = Blog.objects.filter(uid = id)

            if not blog.exists():
                return Response({
                    'data': {},
                    'message': 'Blog does not exists!',
                }, status = status.HTTP_400_BAD_REQUEST)

            if request.user != blog[0].user:
               return Response({
                    'data': {},
                    'message': 'You are not authorized!',
                }, status = status.HTTP_400_BAD_REQUEST)

            serializer = BlogSerializer(blog[0],data=data, partial = True)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Something went wrong',
                }, status = status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response({
                'data': serializer.data,
                'message': 'Post Updated!',
            }, status = status.HTTP_201_CREATED)

        except Exception as e:
            print(e)

            return Response({
                'data': serializer.errors,
                'message': 'Something went wrong',
            }, status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        try:
            data = request.data

            blog = Blog.objects.filter(uid = id)

            if not blog.exists():
                return Response({
                    'data': {},
                    'message': 'Blog does not exists!',
                }, status = status.HTTP_400_BAD_REQUEST)

            if request.user != blog[0].user:
               return Response({
                    'data': {},
                    'message': 'You are not authorized!',
                }, status = status.HTTP_400_BAD_REQUEST)

            blog[0].delete()

            return Response({
                'data': {},
                'message': 'Post Deleted!',
            }, status = status.HTTP_201_CREATED)

        except Exception as e:
            print(e)

            return Response({
                'data': {},
                'message': 'Something went wrong',
            }, status = status.HTTP_400_BAD_REQUEST)

class CommentView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, post_id):
        try:
                comments = Comment.objects.filter(post_id=post_id)
                serializer = CommentSerializer(comments, many = True)

                return Response({
                    'data': serializer.data,
                    'message': 'Success!',
                }, status = status.HTTP_200_OK)



        except Exception as e:
            print(e)

            return Response({
                'data': {},
                'message': 'Something went wrong',
            }, status = status.HTTP_400_BAD_REQUEST)

    def post(self, request, post_id):
        try:
            data = request.data
            data['user'] = request.user.id
            data['post'] = post_id
            serializer = CommentSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Something went wrong',
                }, status = status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response({
                'data': serializer.data,
                'message': 'Comment created!',
            }, status = status.HTTP_201_CREATED)

        except Exception as e:
            print(e)

            return Response({
                'data': {},
                'message': 'Something went wrong',
            }, status = status.HTTP_400_BAD_REQUEST)



    def delete(self, request, post_id, id):
        try:
            data = request.data

            comment = Comment.objects.filter(uid = id)

            if not comment.exists():
                return Response({
                    'data': {},
                    'message': 'Comment does not exists!',
                }, status = status.HTTP_400_BAD_REQUEST)

            if request.user != comment[0].user:
               return Response({
                    'data': {},
                    'message': 'You are not authorized!',
                }, status = status.HTTP_400_BAD_REQUEST)

            comment[0].delete()

            return Response({
                'data': {},
                'message': 'Comment Deleted!',
            }, status = status.HTTP_201_CREATED)

        except Exception as e:
            print(e)

            return Response({
                'data': {},
                'message': 'Something went wrong',
            }, status = status.HTTP_400_BAD_REQUEST)



