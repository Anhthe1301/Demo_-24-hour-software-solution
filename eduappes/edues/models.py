from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import ForeignKey
#Sau khi cài xong cái RichTextField nhớ sửa dưới thằng muốn sửa rồi migrate nha
from ckeditor.fields import RichTextField
from django.template.defaultfilters import length


# Đại diện cho một bảng của CSDL mySQL
class Category(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)

    # toString -> lấy ra tên
    def __str__(seft):
        return seft.name


# Dùng để chứng thực người dùng
class User(AbstractUser):
    pass  # Xong vào setting khai báo AUTH_USER_MODEL

    # lệnh ((pip install pymysql)) qua setting import pymysql
    # Xong cài driver để chạy Lệnh makemigrations cho django biết có sự thay
    # đổi trong models.py và ta muốn lưu các thay đổi
    # số trong migration bằng ((python manage.py makemigrations tenapp))


# Nếu phát sinh thêm lỗi chạy : ((pip install cryptography))
# Sau khi cài xong co them file 0001_initial.py
# Sau đó chạy : ((python manage.py migrate)0  -> để kích hoạt những thay doi tu code xuong CSDL


# Sau do va Shell đe lap trinh tung dong lenh xuong mySQL ((python manage.py shell
# from edues.models import *
# Chạy Category.objects.crate(name="Soft") , xong nho refresh csdl
# Category.objects.all() de test giua code và mysql đã tương tác chưa
# Xong rồi đi tạo superuser -> admin bên urls của project


# Tiếp tục viết một bảng database
class Course(models.Model):
    # null =False không cho để trống
    subject = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to="edues/%Y/%m")
    # khi trên web người dùng up ảnh sẽ về edues với năm và tháng up load
    # Thêm MEDIA_ROOT bên setting
    # Cài thêm thư viện xử lý ảnh (pip install Pillow)

    # Thiết kế khóa ngoại để có thể xêp Course vào 1 Category
    category_fk = models.ForeignKey(Category,
                                    on_delete=models.CASCADE)  # Khi on_delete=models.CASECADE , (RESTRICT La khong xoa theo)

    # Category chứa Course bị xóa thi no bi xóa theo
    def __str__(self):
        return self.subject

    # Sao đó python manage.py makemigrations edues (để tạo ra file thay đổi)

    # python manage.py migrate edues (để đưa xuống csdl)

    # Trong một danh mục không đc trùng tên môn học
    class Meta:
        unique_together = ('subject', 'category_fk')


# Xem basemodel như 1 lớp abstract ta chỉ dùng các biến chứu không tạo nó ra
class BaseModel(models.Model):
    acctive = models.BooleanField(default=False) #null = True or default =True de các bảng đã có giá
    #trị tu đầu rồi về sau khi kế thừa lại lớp này thì các cột mới kế thừa sẽ là null
    create_date = models.DateTimeField(auto_now_add=True,null=True)  # lấy ngày nó đc tạo ra -> chỉ lấy 1 lần đầu
    update_date = models.DateField(auto_now=True,null=True)  # lấy ngày khi nó được cập nhật , lấy đc nhiều lần khi cập nhật lại thì nó sẽ đổi

    # nên để biến nó thành abstract không tạo nó ra một bảng ta dùng :

    class Meta:
        abstract = True
        ordering = ['-id']  # giam theo id . nếu muốn tăng thì +


# Ke Thua
class Lesson(BaseModel):  # Khóa học
    subject = models.CharField(max_length=255, null=False)
    content = RichTextField(null=False)  #  null =Flase Không được để trống
    image = models.ImageField(upload_to="lesson/%Y/%m" )
    course = ForeignKey(Course, on_delete=models.RESTRICT)

    def __str__(self):
        return self.subject


# XONG Rồi makemigrations .... và migrate
# Fix lai tu day
class View(models.Model):
    name = models.CharField(max_length=200)

    view_count = models.IntegerField()
