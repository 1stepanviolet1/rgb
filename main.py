from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang.builder import Builder
from kivy.properties import OptionProperty

from kivy.core.window import Window
Window.size = (270, 585)

from random import randint


class Container(AnchorLayout):
    padding = [15, 15, 15, 15]
    
    enabled_color_display = OptionProperty(
        'off', 
        options=['on', 'off']
    )

    rgb_box = Builder.load_file("./design/rgb.kv")
    plug_box = AnchorLayout()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rgb_box.btn_show_color.bind(
            on_press=self.show_color,
            on_release=self.to_rgb
        )

        self.rgb_box.btn_rand_color.bind(
            on_release=self.rand_color
        )

        self.rgb_box.btn_get_color.bind(
            on_release=self.get_color
        )

        self.add_widget(self.rgb_box)

    def get_color(self, _=None):
        input_r = self.rgb_box.input_r
        input_g = self.rgb_box.input_g
        input_b = self.rgb_box.input_b

        try:
            r = int(input_r.text) / 255
            g = int(input_g.text) / 255
            b = int(input_b.text) / 255
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
        if self.enabled_color_display == 'on':
            return 
        
        self.rgb_box.remove_widget(self.rgb_box.interactive_box)
        self.rgb_box.add_widget(self.plug_box)

        self.enabled_color_display = 'on'
    
    def to_rgb(self, _=None):
        if self.enabled_color_display == 'off':
            return 
        
        self.rgb_box.remove_widget(self.plug_box)
        self.rgb_box.add_widget(self.rgb_box.interactive_box)

        self.enabled_color_display = 'off'
        

class RGBApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    RGBApp().run()
