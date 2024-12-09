from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.
def sign_up_by_html(request):
    users = ['George', 'Muphell', 'Astrud', 'Kukueff']
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password == repeat_password and int(age) >= 18 and username not in users:
            return HttpResponse(f'Приветствуем, {username}')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'registration_page.html', context=info)
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return render(request, 'registration_page.html', context=info)
        elif username in users:
            info['error'] = 'Пользователь уже существует'
            return render(request, 'registration_page.html', context=info)

    return render(request, 'registration_page.html')


def sign_up_by_django(request):
    users = ['George', 'Muphell', 'Astrud', 'Kukueff']
    form = UserRegister(request.POST)
    info = {'form': form}

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password == repeat_password and int(age) >= 18 and username not in users:
                return HttpResponse(f'Приветствуем, {username}')
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', context=info)
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', context=info)
            elif username in users:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', context=info)
    else:
        form = UserRegister()
        # return render(request, 'registration_page.html', context=info)
    return render(request, 'registration_page_djn.html', {'form': form})
