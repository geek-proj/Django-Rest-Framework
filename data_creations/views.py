from django.shortcuts import render
from .serializers import FieldsSerializer,UserSerializer
from .models import Fields,User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.


class FieldsRetriveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class FieldsCreateView(generics.CreateAPIView):
    serializer_class = FieldsSerializer
    queryset = Fields.objects.all()

class FieldsListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    