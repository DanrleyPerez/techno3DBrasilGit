from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .chat_responder import ChatResponder
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self):
        super().__init__()
        self.codigo = 0

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['nome_sala']
        self.room_group_name = 'chat_%s' % self.room_name
        self.message_list = []

        #entrar na sala

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        self.codigo = code

        #sai da sala
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    #recebe mensagem do websockte
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.message_list.append(message)
        self.resposta_automatica = ChatResponder().processa(self.message_list)
        classific = ''
        # if '@' in message:
        #     try:
        #         if self.message_list[1] == 'sim' or self.message_list[1] == 'Sim' or self.message_list[1] == 'S' or self.message_list[1] == 's':
        #             classific = "novo produto"
        #         elif self.message_list[2] == 'sim' or self.message_list[2] == 'Sim' or self.message_list[2] == 'S' or self.message_list[2] == 's':
        #             classific = "serviço 3d"
        #         elif self.message_list[3] == 'software' or self.message_list[3] == 'Software':
        #             classific = "interesse em software"
        #         elif self.message_list[4] == 'desenvolvedor' or self.message_list[4] == 'Desenvolvedor':
        #             classific = "interesse no desenvolvedor"
        #
        #         contato = SaveContato(email=message,mensagem=classific)
        #         contato.salvar()
        #     except:
        #         pass



        if self.resposta_automatica == "Desculpe, não consegui entender, digite novamente":
            self.message_list.pop(len(self.message_list)-1)
        #envia mensagem para sala
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'answer': self.resposta_automatica,
            }
        )


        #recebe mensagem da sala

    async def chat_message(self, event):
        message = event['message']
        answer = event['answer']

        await super().send(text_data=json.dumps({
            'message': message,
            'answer': answer,
        }))
        if answer == "Obrigado, entraremos em contato. Encerrando a conversa ...":
            await self.disconnect(self.codigo)



        #envia mensage para o websocket


