from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password # 자동으로 비밀번호를 암호화해서 저장할 수 있게 함.
from .models import Fcuser
from .forms import LoginForm

# Create your views here.


def home(request):
    user_id = request.session.get('user')

    if user_id:
        fuser = Fcuser.objects.get(pk=user_id)

    return render(request, 'home.html')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id # dictionary를 사용하듯이 사용하면 되며, cookie를 관리한다.
            return redirect('/') # 현재 경로로 redirect할 때엔 redirect('/')와 같이 사용.
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# GET방식과 POST방식 두 가지 존재.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username', None) # request.POST['username']
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}
        # 입력받지 않은 값을 입력받았을 때의 예외 처리
        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        # 비밀번호 입력, 비밀번호 재입력이 다른 경우
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.' # 렌더 메시지를 저장하여 return의 render함수로 던짐.
            #return HttpResponse('비밀번호가 다릅니다!') --> 페이지가 바뀌어야만 에러 메시지가 보임. 불편.
        else:
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )

            fcuser.save()

        return render(request, 'register.html', res_data)
