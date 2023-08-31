from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserForm, ProfileForm
from .models import Profile



def sign_up(request):
    if request.method == 'GET':
        return render(request, 'users/signup.html', context={
                'page_title': 'Реєстрація'
            })
    elif request.method == 'POST':
        #1 зчитування даних з форми
        login_x =request.POST.get('login')
        pass1_x =request.POST.get('pass1')
        pass2_x =request.POST.get('pass2')
        email_x =request.POST.get('email')

        #2 додавання користувача у базу:
        user = User.objects.create_user(login_x, email_x, pass1_x)
        user.save()

        #3 Формування звіту
        color = 'red'
        report = 'в реєстрації відмовлено'
        if user is not None:
            color = 'green'
            report = 'реєстрація успішна'

        #4 завантаження сторінки звіту

        return render(request, 'users/reports.html', context={
                'page_title': 'звіт про реєстрацію',
                'color': color,
                'report': report
            })

def sign_in(request):
    if request.method == 'GET':
        return render(request, 'users/signin.html', context={
                'page_title': 'Авторизація'
            })
    elif request.method == 'POST':
        #1 зчитування даних з форми
        login_x =request.POST.get('login')
        pass1_x =request.POST.get('pass1')

        #2 Перевірка пари логін-пароль
        user = authenticate(request, username=login_x, password=pass1_x)

        #3 Формування звіту
        color = 'red'
        report = 'в авторизації відмовлено'
        if user is not None:
            color = 'green'
            report = 'авторизація успішна'
            login(request, user)

        #4 завантаження сторінки звіту

        return render(request, 'users/reports.html', context={
                'page_title': 'звіт про авторизацію',
                'color': color,
                'report': report
            })


def sign_out(request):
    logout(request)
    return redirect('/')


def profile(request):
    return render(request, 'users/profile.html', context={
                'page_title': 'профіль користувача',
            })


class Profile_update(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'users/profile_update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)





def ajax_reg(request):
    response = dict()
    login = request.GET.get('login')
    try:
        User.objects.get(username=login)
        response['message'] = 'зайнятий'
    except User.DoesNotExist:
        response['message'] = 'вільний'
    return JsonResponse(response)


def ajax_reg_email(request):
    response = dict()
    email = request.GET.get('email')
    try:
        User.objects.get(email=email)
        response['message'] = 'зайнятий'
    except User.DoesNotExist:
        response['message'] = 'вільний'
    return JsonResponse(response)