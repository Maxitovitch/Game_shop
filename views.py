from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Order, Genre
from .forms import SupportTicketForm


def game_list(request):
    search_query = request.GET.get('search', '')
    games = Game.objects.filter(title__icontains=search_query)
    genres = Genre.objects.all()


    sort_by = request.GET.get('sort', 'title')
    games = games.order_by(sort_by)

    return render(request, 'games/game_list.html', {'games': games, 'genres': genres, 'search_query': search_query})


def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'games/game_detail.html', {'game': game})

def buy_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.user.is_authenticated:
        order = Order(user=request.user, game=game)
        order.save()
        return render(request, 'games/buy_success.html', {'code': order.code})



def support_ticket_view(request):
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем тикет
            messages.success(request, "Ваш запрос успешно отправлен!")
            return redirect('support_ticket')  # Перенаправляем на страницу с формой
    else:
        form = SupportTicketForm()

    return render(request, 'support/support.html', {'form': form})






from django.contrib.auth.models import User

from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate



def register_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Пользователь с таким именем уже существует')
            else:
                user = User.objects.create_user(username=username)
                user.password = make_password(password1)
                user.save()

                messages.success(request, 'Регистрация прошла успешно')
                return redirect('game_list')

        else:
            messages.error(request, 'Пароли не совпадают')



    return render(request, 'accounts/register.html')




def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('game_list')  # Замените 'home' на ваше домашнее представление
        else:
            messages.error(request, 'Неправильное имя пользователя или пароль')

    return render(request, 'accounts/login.html')





def filtered_games(request, genre_id):
    return game_list(request, genre_id=genre_id)


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User


def set_money(request):
    if request.method == 'POST':
        money = request.POST.get('money')
        user = request.user  # Получаем текущего авторизованного пользователя
        user.money = money  # Устанавливаем количество денег
        user.save()  # Сохраняем изменения

        return redirect('game_list')  # Перенаправление на главную страницу или другую страницу

    return render(request, 'accounts/money.html')




