"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


import os
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.http import JsonResponse, HttpResponse
from core.views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboards', LeaderboardViewSet)


# API root endpoint that returns the correct codespace URL using $CODESPACE_NAME
def api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    # Use HTTPS for codespace, HTTP for localhost
    if codespace_name == 'localhost':
        base_url = f"http://localhost:8000/api/"
    else:
        base_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    return JsonResponse({
        "users": base_url + "users/",
        "teams": base_url + "teams/",
        "activities": base_url + "activities/",
        "workouts": base_url + "workouts/",
        "leaderboards": base_url + "leaderboards/",
    })

# Simple homepage view
def homepage(request):
    return HttpResponse("<h1>Welcome to Octofit Tracker Backend!</h1><p>This is the API server. Visit <a href='/api/'>/api/</a> for the API root.</p>")

urlpatterns = [
    path('', homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', api_root, name='api-root'),
]
