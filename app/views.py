from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, UserPasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile
from .models import Task
from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
from .models import Task
from django.utils import timezone

# your_app/views.py
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    messages.success(request, f'"{task.title}" đã được xóa!')
    return redirect('home')

@login_required
def mark_task_pending(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if task.status != 'pending':
        task.status = 'pending'
        task.finished = None
        task.save()
        messages.success(request, f'"{task.title}" đã được đánh dấu chưa hoàn thành!')
    return redirect('home')

@login_required
def mark_task_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if task.status != 'completed':
        task.status = 'completed'
        task.finished = timezone.now()  # Sử dụng timezone để xử lý thời gian
        task.save()
        messages.success(request, f'"{task.title}" đã được đánh dấu hoàn thành!')
    return redirect('home')

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Công việc đã được tạo thành công!')
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

@login_required
def update_avatar(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ảnh đại diện đã được cập nhật thành công!')
            return redirect('home')
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'update_avatar.html', {'form': form})


@login_required
def home(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        # Tính số công việc trễ hạn
        overdue_tasks = tasks.filter(status='pending', deadline__lt=timezone.now()).count()
        print(f"Debug: User={request.user.username}, Overdue Tasks={overdue_tasks}, Total Tasks={tasks.count()}")  # Debug
    else:
        tasks = Task.objects.none()
        overdue_tasks = 0
    
    return render(request, 'home.html', {'tasks': tasks, 'overdue_tasks': overdue_tasks})

# View đăng ký
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Đăng ký thành công! Vui lòng đăng nhập.")
            return redirect('login')
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})

# View đăng nhập
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if not user.is_active:
                messages.error(request, "🔒 Tài khoản của bạn đã bị vô hiệu hóa. Vui lòng liên hệ quản trị viên.")
                return redirect('login')
            
        if form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Sau khi đăng nhập, chuyển hướng về trang home
            else:
                messages.error(request, "❌ Tên đăng nhập hoặc mật khẩu không đúng.")      
        else:
            messages.error(request, "❌ Tên đăng nhập hoặc mật khẩu không đúng.")  
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# View đăng xuất
def logout_view(request):
    logout(request)
    messages.success(request, "👋 Bạn đã đăng xuất thành công.")
    return redirect('login')  # Sau khi đăng xuất, chuyển hướng về trang login

@login_required
def change_password(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Giữ session đăng nhập
            messages.success(request, "✅ Mật khẩu đã được thay đổi thành công!")
            return render(request, 'password_success.html')
        else:
            messages.error(request, "❌ Có lỗi xảy ra, vui lòng kiểm tra lại thông tin.")
    else:
        form = UserPasswordChangeForm(user=request.user)

    return render(request, 'change_password.html', {'form': form})
