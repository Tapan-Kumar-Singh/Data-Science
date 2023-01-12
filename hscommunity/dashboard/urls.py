from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.user, name='user'),
    path('add-user/', views.AddUser, name='add-user'),
    path('update-user/<int:id>/', views.UpdateUser, name='update-user'),
    path('delete-user/<int:id>/', views.DeleteUser, name='delete-user'),

    # urls for Handle Posts
    path('posts/', views.AllPosts, name='all-posts'),
    path('add-article/', views.AddArticle, name='add-article'),
    path('edit-article/<int:id>/', views.EditArticle, name='edit-article'),

    # Handle Archived Posts
    path('archived-post/', views.ArchivedPosts, name='archived-posts'),

    # Urls for handle Videos
    path('videos/', views.Videos, name='videos'),
]
