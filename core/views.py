from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth import authenticate, login, get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Conta,Lead
from django.utils.safestring import mark_safe
import json
from time import sleep
from django.http import JsonResponse
# Create your views here.


class home(View):
    def get(self, request):
        print(get_user(request))
        return render(request, 'home.html')

    def post(self, request):
        todos = Lead.objects.all()
        emails = todos.filter(email=request.POST['email'])
        if not emails:

            novo_lead = Lead(id=len(todos)+1, nome=request.POST['nome'], email=request.POST['email'],
                             telefone=request.POST['telefone'], mensagem=request.POST['mensagem'])
            novo_lead.save()
            print('aq foi')


        return redirect('/obrigado')


class SalaView(TemplateView):
    template_name = 'homechat.html'

    def get_context_data(self, **kwargs):
        context = super(SalaView, self).get_context_data(**kwargs)
        context['nome_sala_json'] = mark_safe(
            json.dumps(self.kwargs['nome_sala'])
        )
        return context


class signin(View):
    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        usuario = request.POST['usuario']
        senha = request.POST['password']
        user = authenticate(username=usuario, password=senha)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
        else:

            return render(request, 'signin.html')


class signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        usuario = request.POST['usuario']
        email = request.POST['email']
        senha = request.POST['senha']

        if authenticate(username=usuario, password=senha) is None:
            usuario_novo = User(username=usuario, email=email)
            usuario_novo.set_password(senha)
            usuario_novo.save()
            nova_conta = Conta(id=usuario_novo.pk, username=usuario, amount=100)
            nova_conta.save()

        return render(request, 'signin.html')


class Obrigado(TemplateView):
    template_name = 'obrigado.html'

