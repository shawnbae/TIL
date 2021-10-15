from django.contrib import admin
from .models import Fcuser

# Register your models here.
class FcuserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fcuser, FcuserAdmin) # 사용자를 생성하는 창을 만들어줌.

