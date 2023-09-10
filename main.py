from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from kivy.core.window import Window
Window.size = (270, 585)

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

from random import randint


class Container(GridLayout):
    def get_color(self):
        try:
            r, g, b = self.input.text.split()

            r = int(r[2:]) / 255
            g = int(g[2:]) / 255
            b = int(b[2:]) / 255
        except ValueError:
            r, g, b = 0, 0, 0

        Window.clearcolor = (r, g, b, 1)
    
    def rand_color(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        self.input.text = f'r={r} g={g} b={b}'
        self.get_color()


class GetRGBApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    GetRGBApp().run()
