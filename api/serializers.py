from django.contrib.auth.models import User,Group
from rest_framework import serializers

class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        modle=User
        fields=('url','username','email','groups')
class GroupSerialiers(serializers.HyperlinkedModelSerializer):
    class Meta:
        modle=Group
        fields=('url','name')