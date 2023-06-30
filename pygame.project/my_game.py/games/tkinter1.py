# from ursina import *

# app = Ursina()

# from ursina.prefabs.platformer_controller_2d import PlatformerController2d
# class CustomPlatformerController(PlatformerController2d):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.gravity = 2.0  # 중력 값 조정

# player = CustomPlatformerController(y=0.1, z=.01, scale_y=1, max_jumps=1000)

# ground = Entity(model='quad', scale_x=5, collider='box', color=color.blue)

# ground.y = -2

# quad = load_model("quad",use_deepcopy=True)

# level_parent = Entity(model=Mesh(vertices=[],uvs=[]),Texture="white_cube")

# app.run()
# from ursina import *



# app = Ursina()

# window.fps_counter.enable = False

# camera.orthographic = True
# camera.fov = 4
# camera.position = (1, 1)
# Text.default_resolution *= 2
# butten = Button(text='hi')
# cursor = Tooltip("i'm siwoo", color=color.black,enabled=True)
# def on_enter():
    
#     cursor.enabled = True
# def on_exit():
    
#     cursor.enabled = False
# butten.on_mouse_enter = on_enter
# butten.on_mouse_exit = on_exit


# app.run()


