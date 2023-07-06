import flet as ft


class Message:
    def __init__(self, username: str, text: str, message_type: str):
        self.username = username
        self.text = text
        self.message_type = message_type


def main(page: ft.Page):
    pass


ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)
