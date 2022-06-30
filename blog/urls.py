from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    #path('comment_edit/<slug:slug>/', views.CommentEditView.as_view(), name='comment_edit'),
    path('delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),
    path('edit_comment/<int:pk>', views.EditComment.as_view(), name='edit_comment'),
    path('<slug:slug>/', views.DetailBlog.as_view(), name='detail_blog'),  
]