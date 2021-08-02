from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Urls router restframework
#from rest_framework import routers
#from core.views import MemberViewSet

#router = routers.DefaultRouter()
#router.register(r'members', MemberViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api-auth/', include('rest_framework.urls'))
]