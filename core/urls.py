from django.urls import path
from .views import home, signin, signup, SalaView, Obrigado


urlpatterns = [
    path('', home.as_view()),
    path('signin/', signin.as_view()),
    path('signup/', signup.as_view()),
    path('obrigado/', Obrigado.as_view()),
    path('chat/<str:nome_sala>/', SalaView.as_view())


]