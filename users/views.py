from rest_framework import generics, permissions
from .models import CustomUser,Profile
from .serializers import RegisterSerializer
from .serializers import FollowUserSerializer
from .serializers import DiscoverProfileSerializer
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from twins.models import TwinProfile

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=201)
        print("❌ Registration errors:", serializer.errors)  # debug here
        return Response(serializer.errors, status=400)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        try:
            twin_profile = user.twin_profile  # thanks to related_name='twin_profile'
            is_onboarded = True
        except TwinProfile.DoesNotExist:
            is_onboarded = False
        
        return Response({
            "email": user.email,
            "name": user.name,
            "username":user.username,
            "is_onboarded": is_onboarded,
        })

class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            profile = request.user.profile
            follows = profile.follows.exclude(user=request.user)
            data = ProfileSerializer(follows, many=True).data
            return Response(data, status=200)
        except ObjectDoesNotExist:
            return Response({"error": "Profile not found"}, status=404)

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
        print(serializer.errors)
        return Response(serializer.errors, status=400)

class DiscoverProfilesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        current_profile = request.user.profile
        followed_profiles = current_profile.follows.all()

        # Exclude self and already followed profiles
        discoverable_profiles = Profile.objects.exclude(id__in=followed_profiles).exclude(id=current_profile.id)

        serializer = DiscoverProfileSerializer(discoverable_profiles, many=True)
        return Response(serializer.data)