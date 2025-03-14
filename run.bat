@echo off

REM Kiểm tra xem môi trường ảo đã tồn tại chưa
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
) else (
    echo Virtual environment already exists.
)

REM Kích hoạt môi trường ảo
echo Activating virtual environment...
call venv\Scripts\activate

REM Cài đặt các phụ thuộc từ requirements.txt
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

REM Chạy migrations (thiết lập cơ sở dữ liệu)
echo Running database migrations...
python manage.py migrate

REM Tạo superuser (có thể bỏ qua nếu không cần)
echo Do you want to create a superuser? (Y/N)
set /p create_superuser="Enter choice: "
if /i "%create_superuser%"=="Y" (
    echo Creating superuser...
    python manage.py createsuperuser
) else (
    echo Skipping superuser creation.
)

REM Khởi động server Django
echo Starting Django development server...
python manage.py runserver

REM Thông báo hoàn tất
echo Setup completed successfully!
pause
