from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang.builder import Builder


class MenuBox(AnchorLayout):
    box = Builder.load_file("./design/menu.kv")
