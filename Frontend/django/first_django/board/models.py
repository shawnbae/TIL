from django.db import models

# Create your models here.
# 아래와 같은 class 형식으로 model을 사용
# class Board(models.Model):
#   __class__
# 모델 만들기
class Fcuser(models.Model):
    username = models.CharField(max_length=64,
                                verbose_name="사용자명")
    password = models.CharField(max_length=64,
                                verbose_name="비밀번호")
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                verbose_name="등록시간")

    # 내가 가지고 있는 user네임을 반환함. 
    def __str__(self):
        return self.username


    # django Framework에 table 이름을 전달하는 역할
    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트캠퍼스 사용자' # FCuser와 같은 이름이 아닌 친숙한 이름으로 사용
        verbose_name_plural = '패스트캠퍼스 사용자' # django는 기본적으로 복수형으로 보여주는데, 그 이름을 따로 설정해야 함.