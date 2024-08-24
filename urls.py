
from django.urls import path
from .views import game_list, game_detail, buy_game, support_ticket_view, login_page, register_page, filtered_games, set_money
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', login_page, name='login'),
    path('games/', game_list, name='game_list'),
    path('game/<int:game_id>/', game_detail, name='game_detail'),
    path('buy/<int:game_id>/', buy_game, name='buy_game'),
    path('support/', support_ticket_view, name='support_ticket'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('genre/<int:genre_id>/', filtered_games, name='filtered_games'),
    path('money/', set_money, name='set_money')
]

