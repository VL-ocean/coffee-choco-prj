from . import views
from django.urls import path


urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog'),
    # path('', views.PostList.as_view(), name='home'),
]