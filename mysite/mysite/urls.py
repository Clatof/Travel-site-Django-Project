from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from firstapp import views

admin.site.site_header = "RealSanjeev Admin"
admin.site.site_title = "RealSanjeev Admin Portal"
admin.site.index_title = "Welcome to RealSanjeev Researcher Portal"

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)


urlpatterns = [
        path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path("index/", include("firstapp.urls")),
    path("admin/", admin.site.urls),

]