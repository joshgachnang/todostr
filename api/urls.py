import views
from django.conf.urls import url


task_list = views.TaskViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
task_detail = views.TaskViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = (
    url(r'^tasks/$', task_list),
    url(r'^tasks/(?P<pk>[0-9]+)/$', task_detail),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
)
