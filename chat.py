import flet as ft


class Message:
    def __init__(self, user: str, text: str):
        self.user = user
        self.text = text


# class ChatMessage(ft.Row):
#     def __init__(self, message: Message):
#         super().__init__()
#         self.vertical_alignment = "start"  # type: ignore
#         self.controls = [
#             ft.CircleAvatar(
#                 content=ft.Text(self.get_initials(message.username)),
#                 color=ft.colors.WHITE,
#                 bgcolor=self.get_avatar_color(message.username),
#             ),
#             ft.Column(
#                 [
#                     ft.Text(message.username, width=700),
#                     ft.Text(message.text, selectable=True, width=500),
#                 ]
#             ),
#         ]

#     def get_initials(self, username: str) -> str:
#         return username[:1].capitalize()

#     def get_avatar_color(self, username: str) -> str:
#         colors_lookup = [
#             ft.colors.AMBER,
#             ft.colors.BLUE,
#             ft.colors.BROWN,
#             ft.colors.CYAN,
#             ft.colors.DEEP_ORANGE,
#             ft.colors.DEEP_PURPLE,
#             ft.colors.GREEN,
#             ft.colors.INDIGO,
#             ft.colors.LIME,
#             ft.colors.ORANGE,
#             ft.colors.PINK,
#             ft.colors.PURPLE,
#             ft.colors.RED,
#             ft.colors.TEAL,
#             ft.colors.YELLOW,
#         ]

#         return colors_lookup[hash(username) % len(colors_lookup)]


def main(page: ft.Page):
    page.title = "ChadGPT-flet"
    chat = ft.Column()
    new_message = ft.TextField()

    def on_message(message: Message):
        chat.controls.append(ft.Text(f"{message.user}: {message.text}"))
        page.update()

    page.pubsub.subscribe(on_message)

    def send_click(e):
        page.pubsub.send_all(Message(user=page.session_id, text=new_message.value))
        new_message.value = ""
        page.update()

    page.add(
        chat, ft.Row([new_message, ft.ElevatedButton("Send", on_click=send_click)])
    )


ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)
