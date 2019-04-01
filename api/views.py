from django.contrib.auth.models import User,Group
from rest_framework import  viewsets
from api.serializers import UserSerializers,GroupSerialiers

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializers
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerialiers