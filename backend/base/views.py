from fjango.contrib.auth.models import User
from rest_framework import viewsets, permissions
from backend.base.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Endpoint that allows users to be viewd or edited
    """
    queryset = User.objects.all()
    serialize_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]