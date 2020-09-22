from django.urls import path, include

urlpatterns = [
	path(r'v1/wall/', include('wallsimulator.v1.urls'), name='v1')
]