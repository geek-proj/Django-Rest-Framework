from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
	# token = serializers.
	class Meta:
		model = User
		fields = '__all__'