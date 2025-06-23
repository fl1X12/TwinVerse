from rest_framework import generics, permissions
from .models import CustomUser,Profile
from .serializers import RegisterSerializer
from .serializers import FollowUserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "email": user.email,
            "name": user.name,
            "username":user.username,
        })

class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FollowUserSerializer(data=request.data)
        if serializer.is_valid():
            target_username = serializer.validated_data['target_username']
            
            try:
                target_user = CustomUser.objects.get(username=target_username)
            except CustomUser.DoesNotExist:
                return Response({"error": "User not found."}, status=404)

            if target_user == request.user:
                return Response({"error": "You cannot follow yourself."}, status=400)

            profile = request.user.profile
            target_profile = target_user.profile

            if target_profile in profile.follows.all():
                profile.follows.remove(target_profile)
                return Response({"detail": f"Unfollowed {target_username}"})
            else:
                profile.follows.add(target_profile)
                return Response({"detail": f"Followed {target_username}"})

        return Response(serializer.errors, status=400)
