from django.contrib import admin
from .models import Fcuser

# Register your models here.
class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password') # admin/board 페이지에 출력하고 싶은 field들을 설정해줌.
    
admin.site.register(Fcuser, FcuserAdmin) # 사용자를 생성하는 창을 만들어줌.

