from django.urls import path
from . import views

urlpatterns = [
    path('',views.index.as_view(),name='index'),
    path('register',views.SignUp.as_view(),name='signup'),
    path('login',views.Login.as_view(),name='login'),
    path('logout',views.logout_view, name='logout'),
    path('createpost',views.CreatePost.as_view(),name='createpost'),
    path('profile/', views.profile, name='profile'),
    path('updateprofile/<int:pk>/',views.UpdateProfile.as_view(),name='updateprofile'),
    path('deleteuser/', views.UserDeleteView.as_view(), name='deleteuser'),
    path('post/<int:pk>/',views.DetailPost.as_view(),name='post'),
    path('post/<int:pk>/delete/', views.delete_post, name='deletepost'),
    path('createcomment/<int:pk>/',views.CreateComment.as_view(),name='createcomment'),
    path('updatecomment/<int:pk>/',views.UpdateComment.as_view(),name='updatecomment'),
    path('<int:pk>/deletecomment', views.DeleteComment.as_view(), name='deletecomment'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
]