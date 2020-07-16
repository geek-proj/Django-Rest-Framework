from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from .views import FieldsListView,FieldsCreateView,FieldsRetriveView

router = routers.DefaultRouter()
# router.register(r'requests', Requests,basename='request')
# router.register(r'groups', views.GroupViewSet)
request_urls = router.urls
request_urls += [
	url(r'^create/request/$',FieldsCreateView.as_view()),
	url(r'^requests/(?P<pk>[0-9]+)/$',FieldsRetriveView.as_view()),
	url(r'^list/',FieldsListView.as_view())
]
