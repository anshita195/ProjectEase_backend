from rest_framework import routers
from ProjectEase_app.views import *
from django.urls import include, path


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('lists', ListViewSet)
router.register('cards', CardViewSet)
router.register('projects', ProjectViewSet)
router.register('project_roles', Project_roleViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('oauth/callback/', OauthCallback.as_view()),
    path('logout/', Logout.as_view()),
    path('check_login/', check_login),
    # path('open_auth/callback/',OauthCallback.as_view()),



]
