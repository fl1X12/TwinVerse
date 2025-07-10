from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import TwinProfile
from .serializers import TwinProfileSerializer

class TwinProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            profile = request.user.twin_profile
            serializer = TwinProfileSerializer(profile)
            return Response(serializer.data)
        except TwinProfile.DoesNotExist:
            return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        profile = request.user.twin_profile
        serializer = TwinProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print("Validation errors:", serializer.errors)
        return Response(serializer.errors, status=400)
    
    def post(self, request):
        try:
            profile = request.user.twin_profile
            serializer = TwinProfileSerializer(profile, data=request.data, partial=True)
        except TwinProfile.DoesNotExist:
            serializer = TwinProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
