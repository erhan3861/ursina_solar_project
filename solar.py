from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Nesne(Entity):
    "Bu sınıf oyun sahnesindeki nesneleri yönetmemizi sağlar."
    def __init__(self, position=(0,0,0), **kwargs):
        # super() kelimesi miras aldığımız sınıfı ifade eder.
        super().__init__() # burada Entity sınıfını yazmış olduk.
        self.position = position
        self.selection = False
        self.collider = "box" # çarpışmayı algılar

        for key, value in kwargs.items():
            setattr(self, key, value)

    def on_click(self):
        "Bu metot nesneye tıklama işlemini kontrol eder."
        if self.color == color.white:
            self.color = color.lime
            self.selection = True
        else:
            self.color = color.white
            self.selection = False

    def update(self):
        "Bu metot nesnenin durumunu günceller."   
        if self.selection: # eğer nesne seçiliyse
            self.x += (held_keys["2"] - held_keys["1"]) * 0.1
            self.y += (held_keys["6"] - held_keys["3"]) * 0.1
            self.z += (held_keys["8"] - held_keys["5"]) * 0.1

# ------------------------------------ ana bölüm ------------------
def update():
    sun.x += (held_keys["d"] - held_keys["a"]) * 0.1
    sun.y += (held_keys["w"] - held_keys["s"]) * 0.1

    # takip kodları
    if takip:
        for p in panel_list:
            p.look_at_2d(sun, axis="z")

takip = False 
def input(key):
    global takip
    if key == "t":
        takip = not takip

    if key == "middle mouse down":
        print(panel.position)
        print(ayak.position)

app = Ursina()

Sky()

sun = Entity(model="sphere", scale=2,  color=color.yellow, y=10)

ground = Entity(model="plane", scale=200,  texture="grass", collider="box")

panel = Nesne(position=Vec3(-0.5, 1.3, -0.1), model="cube", scale=(2, 0.15, 4), texture="solar_texture")

ayak = Nesne(position=Vec3(0, 1.2, 0), model="panel_ayak")

panel_list = []
for i in range(1,11):
    panel_yeni = duplicate(panel, x = panel.x - i * 5)
    ayak_yeni = duplicate(ayak, x = ayak.x - i * 5)
    panel_list.append(panel_yeni)

EditorCamera()

app.run()

# print(nesne1.ornek) # AttributeError: 'Nesne' object has no attribute
# 'ornek'
