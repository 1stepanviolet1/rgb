from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang.builder import Builder
from kivy.properties import BooleanProperty

from options import Pool


class PoolBox(AnchorLayout):
    box = Builder.load_file('./design/pool.kv')
    pool = Pool(maxlen=7)

    is_set = BooleanProperty(False)

    def set_pool(self):
        if self.is_set == False:
            return
        
        for i, val in enumerate(self.pool, 1):
            self.box.ids[f"line{i}"].text = val
        
        self.is_set = False
    
    def add_values(self, r, g, b):
        self.pool.appendleft(f"r={r} g={g} b={b}")
        self.is_set = True

pool_box = PoolBox()
