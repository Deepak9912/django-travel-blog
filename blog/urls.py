from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('comment/edit/<slug:slug>/', views.CommentEditView.as_view(), name='comment_edit'),
    path('<slug:slug>/', views.DetailBlog.as_view(), name='detail_blog'),  
]