from .models import Fields
from django.contrib.auth.models import User
from rest_framework import serializers

class FieldsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Fields
		fields = ('date_added','name','value','user')

class UserSerializer(serializers.ModelSerializer):
	fields = FieldsSerializer(many=True)
	class Meta:
		model = User
		fields = ('username','email','fields')
