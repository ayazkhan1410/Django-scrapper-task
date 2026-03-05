from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProfileCreateAPIView(APIView):
    def get(self, request):
        return Response({
            "message": "Profile created successfully"
        }, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({
            "message": "Profile created successfully"
        }, status=status.HTTP_200_OK)
