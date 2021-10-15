from django.shortcuts import render

# Create your views here.
# 아래와 같은 형식으로 request들을 처리함.
#def test(request):
#    pass
#    pass
#    return httpresponse

def register(request):
    return render(request, 'register.html') # templates폴더의 register.html을 렌더링함.