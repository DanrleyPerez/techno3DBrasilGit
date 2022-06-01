from time import sleep

class ChatResponder:
    def processa(self,lista_mensagem):
        resposta = ''


        if len(lista_mensagem) == 1:
            if "?" in lista_mensagem[0]:
                resposta = 'Estamos bem também. Você tem alguma ideia que deseja materializar em um projeto? Digite "sim" ou "nao" '
            else:
                resposta = ' Você tem alguma ideia que deseja materializar em um projeto? Digite "sim" ou "nao" '

            return resposta

        elif len(lista_mensagem) == 2:
            if 's' in lista_mensagem[1] or 'S' in lista_mensagem[1]:
                resposta = 'mande-nos aqui seu email, para que possamos conversar'
            elif lista_mensagem[1] == 'nao' or lista_mensagem[1] == 'Não' or lista_mensagem[1] == 'N' or lista_mensagem[1] == 'Nao' or lista_mensagem[1]=='Não ' or lista_mensagem[1]=='Nao ':
                resposta = 'Você presta algum tipo de serviço relacionado a impressão 3d? (Modelagem, Impressão 3D ou Pintura?'
            else:
                resposta = "Desculpe, não consegui entender, digite novamente"
            return resposta

        elif len(lista_mensagem) == 3:
            if lista_mensagem[2] == 'sim' or lista_mensagem[2] == 'Sim' or lista_mensagem[2] == 'Sim ':
                resposta = 'digite aqui seu email para que possamos contacta-lo'
            elif "@" in lista_mensagem[2]:
                resposta = 'Obrigado, entraremos em contato. Encerrando a conversa ...'
            elif 'N' in lista_mensagem[2] or 'n' in lista_mensagem[2]:
                resposta = "Você está interessado no nosso serviço de criação Sites/Softwares ou em saber " \
                           "mais sobre o desenvolvedor essa aplicação? Digite 'software' para a primeira opção e " \
                           "'desenvolvedor' para a segunda"
            else:
                resposta = "Desculpe, não consegui entender, digite novamente"
            return resposta

        elif len(lista_mensagem) == 4:
            if "@" in lista_mensagem[3]:
                resposta = 'Obrigado, entraremos em contato. Encerrando a conversa ...'
            elif 'Software' in lista_mensagem[3] or 'software' in lista_mensagem[3] :
                resposta = "Deixe seu email que entraremos em contato!"
            elif 'Desenvolvedor' in lista_mensagem[3] or 'desenvolvedor' in lista_mensagem[3]:
                resposta = "Vou redireciona-lo para meu Site-Portifolio, me permite?"
            else:
                resposta = "Desculpe, não consegui entender, digite novamente"
            return resposta

        elif len(lista_mensagem) == 5:
            if "@" in lista_mensagem[4]:
                resposta = 'Obrigado, entraremos em contato. Encerrando a conversa ...'
            elif 'desenvolvedor' in lista_mensagem[3] or 'Desenvolvedor' in lista_mensagem[3] and "s" in lista_mensagem[4] or "S" in lista_mensagem[4]:
                resposta = "redirecionar"
            else:
                resposta = "Desculpe, não consegui entender, digite novamente"
            return resposta


