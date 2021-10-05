# 기본적으로 참조할 사이트
https://docs.djangoproject.com/ko/3.2/topics/

# 계층 구조
## 모델 계층
- Model은 DataBase를 담당함.
- 기본적으로 SQL이라는 문법을 통해 DataBase의 설계가 이루어져야 하지만, django는 프레임워크로서 DB를 설계할 수 있는 기능들을 별도로 제공함.
- https://docs.djangoproject.com/ko/3.2/topics/db/models/



## 뷰 계층

- 비즈니스 로직에 필요한 부수적인 것들을 관리함. model에서 정리된 데이터를 동작시키는 계층.
- 예를 들어, 아래와 같은 예시에서는 path를 클릭했을 때의 함수를 호출해줌.
  - 만약 django Framework가 관리해주지 않는다면, url마다 직접 함수를 할당해주어야 하는 불편함이 존재했을 것.
  - 더불어 변수 (아래 예시의 year 등)을 사용할 수도 있음.

```python
from django.urls import path

from . import views

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]
```

- 아래와 같은 함수로 요청을 모두 관리할 수 있음.

```python
from django.http import HttpResponse
import datetime

# request를 인자로 받아 모든 요청을 처리해줌.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
```



## 템플릿 계층

- html 문법을 사용할 수 있는 코드
- 내가 원하는 데이터를 html형태로 만들 수 있음.