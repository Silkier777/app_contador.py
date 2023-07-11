import flet as ft

def main(pagina: ft.Page):
    pagina.title = 'meu contador'
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER

def diminuir(event, caixa_texto):
    caixa_texto.value = str(int(caixa_texto.value) - 1)
    pagina.update()

def somar(event, caixa_texto):
    caixa_texto.value = str(int(caixa_texto.value) + 1)
    pagina.update()

pagina = ft.Page()  # Cria uma instância da classe ft.Page

# Criação dos botões
botao_menos = ft.IconButton(ft.icons.REMOVE, on_click=lambda event: diminuir(event, caixa_texto))
caixa_texto = ft.TextField(value='0', width=100, text_align=ft.TextAlign.CENTER)
botao_mais = ft.IconButton(ft.icons.ADD, on_click=lambda event: somar(event, caixa_texto))

pagina.add(
    ft.row([botao_menos, caixa_texto, botao_mais], alignment=ft.MainAxisAlignment.CENTER)
)

# Para visualizar no navegador
ft.app(target=main, pages=[pagina])