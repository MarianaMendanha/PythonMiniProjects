import flet as ft


def main(pagina):
    texto = ft.Text("Marizap")

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        print(f"Enviou no Tunel: {mensagem}")
        # adiciona a mensagem no chat
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        print("Enviar mensagem")
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")
        # # adiciona a mensagem no chat
        # texto_mensagem = ft.Text(campo_mensagem.value)
        # chat.controls.append(texto_mensagem)
        # limpa o campo de mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(
        label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])

    def entrar_chat(evento):
        print("Entrar no chat")
        # fechar pop up, tirar botao e título
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        # criar chat
        pagina.add(chat)
        # texto_entrada = ft.Text(f"{nome_usuario.value} entrou no chat")
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        # chat.controls.append(texto_entrada)
        # campo de mensagem
        # pagina.add(campo_mensagem)
        # botao de enviar
        # pagina.add(botao_enviar)
        pagina.add(linha_enviar)
        pagina.update()

    titulo_popup = ft.Text("Bem vindo ao Marizap")
    nome_usuario = ft.TextField(label="Escreva seu nome")
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(evento):
        print("abrir o chat")
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)


ft.app(target=main, view=ft.WEB_BROWSER)
