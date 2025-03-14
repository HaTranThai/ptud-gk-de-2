from django.contrib.auth.models import User
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # Thêm import này

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, default='avatars/default.jpg')

    def __str__(self):
        return f"{self.user.username}'s profile"
    
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Chưa hoàn thành'),
        ('completed', 'Đã hoàn thành'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True, help_text="Thời hạn hoàn thành")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    @property
    def is_overdue(self):
        if self.status == 'pending' and self.deadline and self.deadline < timezone.now():
            return True
        return False
    