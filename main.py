from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder

from kivy.core.window import Window
Window.size = (270, 585)

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

from random import randint


class Container(AnchorLayout):
    rgb_box = Builder.load_file("./design/get_rgb.kv")
    show_color_box = Builder.load_file("./design/show_color.kv")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rgb_box.btn_show_color.bind(
            on_release=self.show_color
        )

        self.rgb_box.btn_rand_color.bind(
            on_release=self.rand_color
        )

        self.rgb_box.btn_get_color.bind(
            on_release=self.get_color
        )

        self.show_color_box.btn_to_rgb.bind(
            on_release=self.to_rgb
        )

        self.add_widget(self.rgb_box)

    def get_color(self, _=None):
        input_r = self.rgb_box.input_r
        input_g = self.rgb_box.input_g
        input_b = self.rgb_box.input_b

        try:
            r = int(input_r.text.strip()) / 255
            g = int(input_g.text.strip()) / 255
            b = int(input_b.text.strip()) / 255
        except ValueError:
            r, g, b = 0, 0, 0

        Window.clearcolor = (r, g, b, 1)
    
    def rand_color(self, _=None):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        self.rgb_box.input_r.text = f'{r}'
        self.rgb_box.input_g.text = f'{g}'
        self.rgb_box.input_b.text = f'{b}'

        self.get_color()
    
    def show_color(self, _=None):
        self.clear_widgets()
        self.add_widget(self.show_color_box)
    
    def to_rgb(self, _=None):
        self.clear_widgets()
        self.add_widget(self.rgb_box)


class GetRGBApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    GetRGBApp().run()
