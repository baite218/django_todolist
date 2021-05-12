from django.contrib import admin
from django.urls import path, include

from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from rest_framework import routers

from users.views import UserView
from tasks.views import TaskView
from categories.views import CategoryView


router = routers.DefaultRouter()

router.register(r'categories', CategoryView)
router.register(r'tasks', TaskView)
router.register(r'users', UserView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin', LoginView.as_view(), name='rest_login'),
    path('signup', RegisterView.as_view(), name='rest_register'),
]

urlpatterns += router.urls
