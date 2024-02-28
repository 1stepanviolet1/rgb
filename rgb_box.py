from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang.builder import Builder
from kivy.properties import OptionProperty

from kivy.core.window import Window

from options import get_rand_values


class RgbBox(AnchorLayout):
    enabled_color_display = OptionProperty(
        'off', 
        options=['on', 'off']
    )

    box = Builder.load_file("./design/rgb.kv")
    plug_box = AnchorLayout()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.box.btn_show_color.bind(
            on_press=self.show_color,
            on_release=self.to_rgb
        )

        self.box.btn_rand_color.bind(
            on_release=self.rand_color
        )

        self.box.btn_get_color.bind(
            on_release=self.get_color
        )

    def get_color(self, _=None):
        input_r = self.box.input_r
        input_g = self.box.input_g
        input_b = self.box.input_b

        try:
            r = int(input_r.text) / 255
            g = int(input_g.text) / 255
            b = int(input_b.text) / 255
        except ValueError:
            r, g, b = 0, 0, 0

        Window.clearcolor = (r, g, b, 1)
    
    def rand_color(self, _=None):
        r, g, b = get_rand_values()

        self.box.input_r.text = f'{r}'
        self.box.input_g.text = f'{g}'
        self.box.input_b.text = f'{b}'

        self.get_color()
    
    def show_color(self, _=None):
        if self.enabled_color_display == 'on':
            return 
        
        self.box.remove_widget(self.box.interactive_box)
        self.box.add_widget(self.plug_box)

        self.enabled_color_display = 'on'
    
    def to_rgb(self, _=None):
        if self.enabled_color_display == 'off':
            return 
        
        self.box.remove_widget(self.plug_box)
        self.box.add_widget(self.box.interactive_box)

        self.enabled_color_display = 'off'
        