
# Create your views here.
from models import Task
from serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def pre_save(self, obj):
        print 'task list save'
        obj.user = self.request.user


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer