from rest_framework import serializers
from core.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name','last_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }