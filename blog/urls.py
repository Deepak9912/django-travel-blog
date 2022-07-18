from . import views
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('contact/', include('contact.urls')),
    path('delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),
    path('edit_comment/<int:pk>', views.EditComment.as_view(), name='edit_comment'),
    path('<slug:slug>/', views.DetailBlog.as_view(), name='detail_blog'),  
]
