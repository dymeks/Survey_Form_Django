from django.conf.urls import url
from . import views  

urlpatterns = [
	url(r'^$', views.index),
	# url(r'^process$',views.result),
	# url(r'^clear$',views.clear_session)
]