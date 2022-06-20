from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('<slug:slug>/', views.DetailBlog.as_view(), name='detail_blog'), 
]