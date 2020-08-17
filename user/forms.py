from django import forms


class RegisterForm(forms.Form):
    '''注册验证表单'''
    name = forms.CharField(required=True, max_length=15)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    invited = forms.CharField(required=True, min_length=3)


class LoginForm(forms.Form):
    # 用户名密码不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class ForgetPwdForm(forms.Form):
    '''忘记密码'''
    email = forms.EmailField(required=True)


class ModifyPwdForm(forms.Form):
    '''重置密码'''
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)
