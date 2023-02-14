from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name="home"),
    path('insert_post/',views.postsInsert,name="postsInsert"),
    path('update_post/<str:id>',views.update_post,name="update_post"),
    path('delete_post/<str:id>',views.delete_post,name="delete_post"),
    path('loginUser/',views.loginUser,name="loginUser"),
    path('lgutUser/',views.logoutUser,name="logoutUser"),
    path('view_post/<str:id>',views.view_post,name="view_post"),
    path('publish_post/<str:id>',views.publish_post, name="publish_post"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)