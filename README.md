# Thông tin cá nhân sinh viên

- **Trần Thái Hà**
- **MSSV: 22636801**
- **STT: 16**

# Mô tả Dự án

Xây dựng một ứng dụng quản lý công việc:
- **Đăng ký & Đăng nhập:** Tạo tài khoản và đăng nhập để sử dụng hệ thống,  cho phép user có thể upload avatar.
- **Đăng tải & Quản lý Task:** Viết task.
- **Chức năng:**  Chức năng hiển thị số công việc trễ hạn.

# Hướng dẫn cài dặt và chạy chương trình

### Tải hệ thống

Clone dự án từ Github:
```bash
git clone https://github.com/HaTranThai/ptud-gk-de-2.git
```

Vào thư mục hệ thống:
```bash
cd ptud-gk-de-2
```

### Cài đặt mô trường ảo

Trước tiên, đảm bảo bạn đã cài đặt Python (phiên bản ≥ 3.10).

Tạo môi trường ảo:
```bash
python -m venv venv
```

Kích hoạt môi trường ảo:
- Windows: 
    ```bash
    venv\Scripts\activate
    ```

- Ubuntu/Linux:
    ```bash
    source venv/bin/activate
    ```

### Cài đặt thư viện

Cập nhật phiên bản mới nhất của pip trong môi trường ảo:
```bash
python -m pip install --upgrade pip
```

Sau đó, cài đặt các thư viện cần thiết từ `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Chạy chương trình

Áp Dụng Migrations vào Database:
```bash
python manage.py makemigrations
python manage.py migrate
```

Tạo Superuser (Tài Khoản Quản Trị)
```bash
python manage.py createsuperuser
```

Chạy Server 
```bash
python manage.py runserver
```

### Nếu muốn chạy tự động

Chạy file `run.bat`:
```bash
.\run.bat
```

# Link project đã triển khai

- [http://127.0.0.1:8000](http://127.0.0.1:8000)
