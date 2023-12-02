from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes((AllowAny,))
def api_root(request, format=None):
    return Response(
        {
            "create_post": reverse(
                "create_post", request=request, format=format
            ),
            "comment_post": reverse(
                "comment_post", request=request, format=format
            ),
            "react_post": reverse(
                "react_post", request=request, format=format
            ),
            "post_list": reverse(
                "post_list", args=[1], request=request, format=format
            ),
            "comment_list": reverse(
                "comment_list", args=[1], request=request, format=format
            ),
            "like_list": reverse(
                "like_list", args=[1], request=request, format=format
            ),
            "create_hackathon": reverse(
                "create_hackathon", request=request, format=format
            ),
            "list_hackathon": reverse(
                "list_hackathon",args=["IIT Bhilai"], request=request, format=format
            ),
            "register_hackathon": reverse(
                "register_hackathon", request=request, format=format
            ),
            "submit_hackathon": reverse(
                "submit_hackathon", request=request, format=format
            ),
            "winner_hackathon": reverse(
                "winner_hackathon", request=request, format=format
            ),

            "registered_hackathon": reverse(
                "registered_hackathon",args=[1], request=request, format=format
            ),
            "view_hackathon": reverse(
                "view_hackathon",args=[1], request=request, format=format
            ),
            "create_seminar": reverse(
                "create_seminar", request=request, format=format
            ),
            "register_seminar": reverse(
                "register_seminar", request=request, format=format
            ),
            "list_seminar": reverse(
                "list_seminar", args=["IIT Bhilai"], request=request, format=format
            ),
            "view_seminar": reverse(
                "view_seminar", args=[1], request=request, format=format
            ),
            "send_message": reverse(
                "send_message", request=request, format=format
            ),
            "message_details": reverse(
                "message_details", request=request, format=format
            ),
            "user_conversations": reverse(
                "user_conversations", args=[1], request=request, format=format
            ),
            "endorse": reverse(
                "endorse", request=request, format=format
            ),
            "endorsement_list": reverse(
                "endorsement_list", args=[1], request=request, format=format
            ),
            "student_list": reverse(
                "student_list", request=request, format=format
            )
        }
    )