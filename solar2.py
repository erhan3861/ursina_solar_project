from ursina import *


# ------------------------------------ ana bölüm ------------------
def update():
    sun.x += (held_keys["d"] - held_keys["a"]) * 0.1
    sun.y += (held_keys["w"] - held_keys["s"]) * 0.1
    control(panel)
    control(ayak)

    # takip kodları
    if takip:
        for p in panel_list:
            p.look_at_2d(sun, axis="z")

    
def control(e):
    if e.color == color.lime:
        e.x += (held_keys["2"] - held_keys["1"]) * 0.1
        e.y += (held_keys["6"] - held_keys["3"]) * 0.1
        e.z += (held_keys["8"] - held_keys["5"]) * 0.1


def select(e):
    if e.color == color.white:
        e.color = color.lime
    else:
        e.color = color.white

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

sun = Entity(model="sphere", scale=2,  color=color.yellow, y=10, texture="sun_texture")

ground = Entity(model="plane", scale=200,  texture="grass", collider="box")

panel = Entity(position=Vec3(-1.1, 1.2, 2), model="cube", scale=(2, 0.15, 4), texture="solar_texture", collider="box")
panel.on_click = lambda : select(panel)

ayak = Entity(position=Vec3(-1.6, 1.2, 0), model="panel_ayak", collider="box")
ayak.on_click = lambda : select(ayak)

panel_list = [panel]

for i in range(1,11):
    panel_yeni = duplicate(panel, x = panel.x - i * 5)
    ayak_yeni = duplicate(ayak, x = ayak.x - i * 5)
    panel_list.append(panel_yeni)

EditorCamera()

p = PointLight(parent=sun, color = color.white) # güneş
a = AmbientLight(color = color.rgba(100, 100, 100, 10)) # ortam

app.run()

# print(nesne1.ornek) # AttributeError: 'Nesne' object has no attribute
# 'ornek'

