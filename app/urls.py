from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # Trang home, chỉ cho phép truy cập nếu đã đăng nhập
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('change-password/', views.change_password, name='change-password'),
    path('update-avatar/', views.update_avatar, name='update_avatar'),
    path('create-task/', views.create_task, name='create_task'),
    path('mark-task-completed/<int:task_id>/', views.mark_task_completed, name='mark_task_completed'),
    path('mark-task-pending/<int:task_id>/', views.mark_task_pending, name='mark_task_pending'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
