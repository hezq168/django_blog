from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from users.models import UserProfile, VerifyCode
from users.email_send import send_register_email
from users.forms import RegisterForm, LoginForm

# 验证码
import io
from apps.users import check_code as CheckCode


class CustomBackend(ModelBackend):
    """重写用户验证"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 验证码
def check_code(request):
    """
    获取验证码
    :param request:
    :return:
    """
    stream = io.BytesIO()
    img, code = CheckCode.create_validate_code()
    img.save(stream, 'PNG')
    request.session['CheckCode'] = code.lower()
    return HttpResponse(stream.getvalue())


class Register(View):
    """
    注册
    """

    def get(self, request):
        reg = RegisterForm()
        return render(request, 'user/register.html', {'reg': reg})

    def post(self, request):
        reg = RegisterForm(request.POST)
        if reg.is_valid():
            code = request.POST.get('code', None)
            if code.lower() in request.session['CheckCode']:
                reg_data = reg.cleaned_data
                if UserProfile.objects.filter(Q(username=reg_data['email']) | Q(email=reg_data['email'])):
                    return render(request, 'user/register.html', {'reg': reg, 'msg': '邮箱已经存在！'})
                user_profile = UserProfile()
                user_profile.username = reg_data['email']
                user_profile.email = reg_data['email']
                user_profile.nick_name = reg_data['nick_name']
                user_profile.is_active = False
                user_profile.password = make_password(reg_data['pwd'])
                user_profile.save()
                # 注册成功，发送激活邮件
                send_register_email(reg_data['email'], 'register')
                return render(request, 'user/reg_msg.html', {'email': reg_data['email']})
            else:
                msg = '验证码错误！'
        else:
            msg = ''
        return render(request, 'user/register.html', {'reg': reg, 'msg': msg})


class UserLogin(View):
    """
    登录
    """

    def get(self, request):
        login_form = LoginForm()
        next = request.GET.get('next', '/')
        return render(request, 'user/login.html', {'login': login_form, 'next': next})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            code = request.POST.get('code', None)
            next = request.POST.get('next', '/')
            if code.lower() in request.session['CheckCode']:
                login_data = login_form.cleaned_data
                user = authenticate(username=login_data['email'], password=login_data['pwd'])
                if user:
                    if user.is_active == True:
                        login(request, user)
                        return redirect(next)
                    else:
                        return render(request, 'user/login.html', {'msg': '用户名未激活！'})
                else:
                    msg = '用户或密码错误！'
            else:
                msg = '验证码错误！'
        else:
            msg = ''
        return render(request, 'user/login.html', {'login': login_form, 'msg': msg})


@login_required
def UserLogout(request):
    """
    退出
    """

    logout(request)
    return redirect('/users/login')


class ActiveUserView(View):
    """
    用户激活
    """

    def get(self, request, active_code):
        re_email = VerifyCode.objects.filter(code=active_code).first()
        if re_email:
            user = UserProfile.objects.get(email=re_email.email)
            # 激活用户
            user.is_active = True
            user.save()
            re_email.delete()
            return redirect('/users/login')
        else:
            return render(request, 'user/active_fail.html')
