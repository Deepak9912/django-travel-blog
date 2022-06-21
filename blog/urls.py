from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('post/edit/<int:pk>', views.PostEditView.as_view(), name='post-edit'),
    path('<slug:slug>/', views.DetailBlog.as_view(), name='detail_blog'),
]