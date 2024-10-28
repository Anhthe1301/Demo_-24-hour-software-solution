from django.contrib import admin
# Hổ trợ nhúng hình ảnh vào
from django.utils.html import mark_safe
# Thêm những models vào import này
from .models import Category, Course, Lesson, View


# khi dùng .models Điều này cho phép bạn
# truy cập vào lớp Category được định nghĩa trong models.py của cùng ứng dụng mà không cần chỉ rõ tên ứng dụng.

# Ta có thể tự tạo ra lớp này để custom lại các thuộc tính trang admin của (Lesson)
# Truyền LessonAdmin vào register rồi giữ Ctrl +Click vào ModelAdmin để vào thư viện nó
class LessonAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content']  # Tìm kiếm theo subject và contentx
    list_display = ['id', 'subject', 'content', 'create_date']
    # Đúng rồi! Khi bạn khai báo edues.models, điều đó có nghĩa
    # là bạn đang ở trong một ứng dụng khác và muốn sử dụng các mô hình (models) được định nghĩa trong ứng dụng edues.
    # Register your models here.
    list_filter = ['subject']  # Tạo ra thanh filter trên web để loc
    list_per_page = 1  # phân trang
    readonly_fields = ['avatar']

    def avatar(self, lesson):  # lesson la ten thu muc chứa ảnh có thể là đối tương khác
        return mark_safe(f'<img src="/static/{lesson.image.name}" width="120" />')
        # Tự nó nó vào đúng ở static sẳn từ static ta vào nữa

    # Đề lại để viết css -> tạo thu muc css trước nha
    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    #Sau khi viết này nho truyen CategoryAdmin vao admin.site.register
    #có thể cài pip install django-ckeditor cho textfield soạn thảo văn bản ok hơn
    #Sau đó vào Settings thêm vào INSTALL APP ckedditor và ckeditor_uploader
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
