from django.shortcuts import render
from rest_framework import viewsets,generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import authentication, permissions
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
# Create your views here.

class UserRegistrationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        for user in User.objects.all():
            Token.objects.get_or_create(user=user)
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )
        queryset = self.queryset
        
        return queryset
    
    def create(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        u = serializer.save()
        Token.objects.create(user=u)
        return Response(serializer.data)


    
