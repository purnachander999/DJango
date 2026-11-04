from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:post_id>/', views.post_details, name='post_details'),
    path('user/<str:username>/', views.user, name='user_profile'),
    path('article/<int:year>/<int:month>/', views.article_details, name='article_details'),
]