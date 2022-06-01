from .models import entraremContato


class SaveContato():
    def __init__(self, email, mensagem):
        self.email = email
        self.mensagem = mensagem

    def salvar(self):
        objetos = entraremContato.objects.all()
        novo_contato = entraremContato(id=len(objetos) + 1, email=self.email, mensagem=self.mensagem)
        novo_contato.save()