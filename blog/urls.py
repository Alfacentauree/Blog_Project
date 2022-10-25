from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('about',views.about,name='about'),
    path('',views.posts,name='posts'),
    path('draft-post/',views.draft,name='draft-post'),
    path('add_comment/<str:pk>',views.add_comment,name='add_comment'),
    path('post/<str:pk>/',views.post,name='post'),
    path('create-post/',views.create_post,name='create-post'),
    path('update-post/<str:pk>/',views.update_post,name='update-post'),
    path('delete-post/<str:pk>/',views.delete_post,name='delete-post'),
    path('comment_approve/<str:pk>/',views.comment_approve,name='comment_approve'),
    path('comment_remove/<str:pk>/',views.comment_remove,name='comment_remove'),
    path('publish_post/<str:pk>/',views.publish_post,name='publish_post')
]