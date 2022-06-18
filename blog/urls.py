from . import views
from django.urls import path
from .views import ContactFormView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.DetailBlog.as_view(), name='detail_blog'),
    path('', views.ContactFormView.as_view(), name='contact_form'),
]