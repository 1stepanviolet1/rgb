import gc
gc.collect()

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout

from kivy.core.window import Window
Window.clearcolor = (.07, .07, .07, 1)
#Window.size = (270, 585)

from menu_box import MenuBox
from rgb_box import RgbBox
from pool_box import pool_box


class Container(AnchorLayout):
    padding = [30, 30, 30, 30]

    menu_box = MenuBox()
    rgb_box = RgbBox()
    pool_box = pool_box

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.menu_box.box.btn_to_rgb.bind(
            on_release=self.go_to_rgb
        )

        self.rgb_box.box.btn_to_menu.bind(
            on_release=self.go_to_menu
        )

        self.menu_box.box.btn_to_pool.bind(
            on_release=self.go_to_pool
        )

        self.pool_box.box.btn_to_menu.bind(
            on_release=self.go_to_menu
        )

        self.add_widget(self.menu_box.box)
    
    def go_to_rgb(self, _=None):
        self.clear_widgets()
        self.add_widget(self.rgb_box.box)
    
    def go_to_menu(self, _=None):
        self.clear_widgets()
        self.add_widget(self.menu_box.box)
    
    def go_to_pool(self, _=None):
        self.clear_widgets()
        self.pool_box.set_pool()
        self.add_widget(self.pool_box.box)
        

class RGBApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    RGBApp().run()
