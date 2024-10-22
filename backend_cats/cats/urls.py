from django.urls import path, include
from .views import index

urlpatterns = [
     path('', index, name='home'),
     path('api-auth/', include('rest_framework.urls'))
]
