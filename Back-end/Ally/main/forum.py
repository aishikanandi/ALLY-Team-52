from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Post, UserDetails, Forum, Tag
from .serializers import CreatePostSerializer, CommentPostSerializer, PostSerializer, CommentSerializer
import json
from datetime import datetime

class CreatePost(APIView):
    def post(self, request):

        user_id = request.data.get('userID')
        forum_id = request.data.get('forumID')
        tag_names = request.data.get('tags')
        data = {
            "content" : request.data.get('content')
        }

        try:
            user_instance = UserDetails.objects.get(pk=user_id)
            forum_instance = Forum.objects.get(pk=forum_id)
        except UserDetails.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Forum.DoesNotExist:
            return Response({"error": "Forum not found"}, status=status.HTTP_404_NOT_FOUND)

        if tag_names is not None:
            tags = []
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                tags.append(tag)

        serializer = CreatePostSerializer(data=data)
        if serializer.is_valid():
            post_instance = serializer.save(postedBy=user_instance, forumID=forum_instance)
            post_instance.tags.set(tags)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AddCommentView(APIView):
    def post(self, request):

        user_id = request.data.get('userID')
        post_id = request.data.get('postID')
        data = {
            "comment" : request.data.get('comment')
        }

        try:
            user = UserDetails.objects.get(pk=user_id)
            post = Post.objects.get(pk=post_id)
        except UserDetails.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommentPostSerializer(data=data)
        if serializer.is_valid():
            comment_text = {
                "Comment" : serializer.validated_data.get('comment'),
                "byUserID" : user_id,
                "user" : user.firstName + " " + user.lastName,
                "Timestamp" : str(datetime.now())
            }
            jsonDec = json.decoder.JSONDecoder()
            comments =  jsonDec.decode(post.comments)
            comments.append(comment_text)
            post.comments = json.dumps(comments)
            post.commentsCount += 1
            post.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AddReactionView(APIView):
    def post(self, request):

        user_id = request.data.get('userID')
        post_id = request.data.get('postID')

        try:
            user = UserDetails.objects.get(pk=user_id)
            post = Post.objects.get(pk=post_id)
        except UserDetails.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            jsonDec = json.decoder.JSONDecoder()
            likes =  jsonDec.decode(post.likes)
            if user_id not in likes.keys():
                likes[user_id] = user.firstName + " " + user.lastName
                post.likesCount += 1
            post.likes = json.dumps(likes)
            post.save()
            return Response({"message" : "success"}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"error" : e}, status=status.HTTP_400_BAD_REQUEST)



class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100



class ListPostView(ListAPIView):
    serializer_class = PostSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        tag_names = self.request.query_params.getlist('tags')
        forum_id = self.kwargs.get('forumID')

        queryset = Post.objects.filter(forumID=forum_id)
        queryset = queryset.order_by('-postedTime')
        if tag_names:
            for tag_name in tag_names:
                queryset = queryset.filter(tags__name=tag_name)
        queryset = queryset.prefetch_related('tags')
        return queryset
    


class ListCommentView(APIView):
    def get(self, request, postID):

        try:
            comments = Post.objects.get(pk=postID).comments
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            jsonDec = json.decoder.JSONDecoder()
            comments =  jsonDec.decode(comments)
            serializer = CommentSerializer(data=comments, many=True)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({"error" : e}, status=status.HTTP_400_BAD_REQUEST)



class ListReactionView(APIView):
    def get(self, request, postID):

        try:
            likes = Post.objects.get(pk=postID).likes
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            jsonDec = json.decoder.JSONDecoder()
            likes =  jsonDec.decode(likes)
            return Response(likes, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({"error" : e}, status=status.HTTP_400_BAD_REQUEST)