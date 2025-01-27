from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from users.models import Users, UserRole
from django.contrib.auth.hashers import make_password, check_password
from django.db import IntegrityError, DatabaseError


# Create your views here.

def login_page(request):
    print("login_page")
    return render(request, 'login.html')

def register_page(request):
    template = loader.get_template('register.html')    
    return HttpResponse(template.render(request=request))


def save_user(request): 
    # form으로부터(register.html) 데이터를 받아서 DB에 저장
    msg = "회원가입이 완료되었습니다."
    user_email = request.POST.get('UserEmail')
    password = request.POST.get('Password')
    
    print(user_email)
    # 패스워드 보안을 위해 암호화
    enc_password = make_password(password)
    
    print(enc_password)
    try : 
        role = UserRole.objects.get(id=2)
        new_user = Users(user_email=user_email, password=enc_password, role=role)
        new_user.save()
        
    except IntegrityError as e:
        msg = f"이미 존재하는 이메일입니다. {e}"
        
    except DatabaseError as e:
        msg = f"DB 오류가 발생했습니다. {e}"
    
    context = {
        'msg': msg
    }
    template = loader.get_template('reg_response.html')
    return HttpResponse(template.render(context, request=request))

def login_process(request):
    msg = "회원가입이 완료되었습니다."
    user_email = request.POST.get('UserEmail')
    password = request.POST.get('Password')
    
    user = Users.objects.get(user_email=user_email)
    if user is None:
        msg = "존재하지 않는 이메일입니다."
        context = {
            'msg': msg  
        }
        template = loader.get_template('reg_response.html')
        return HttpResponse(template.render(context, request=request))

    if not check_password(password, user.password):# 앞에가 입력받은 패스워드, 뒤에가 DB에 저장된 패스워드
        
        msg = "비밀번호가 맞지 않습니다."
        context = {
            'msg': msg  
        }
        template = loader.get_template('reg_response.html')
        return HttpResponse(template.render(context, request=request))
    
    request.session['user_id'] = user.id
    request.session['user_email'] = user.user_email
    
    
    return render(request, 'index.html')

def logout(request):
    request.session.flush()
    return redirect('index')
