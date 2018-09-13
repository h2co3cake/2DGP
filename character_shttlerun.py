from pico2d import *
open_canvas()
grass = load_image('grass.png')
character1 = load_image('animation_sheet.png')
character2 = load_image('run_animation.png')

x = 0
frame = 0

while (1):

    while (x < 800):
        clear_canvas()
        grass.draw(400, 30)
        character2.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x += 20
        delay(0.05)
        get_events()

    while(0 < x):
        clear_canvas()
        grass.draw(400, 30)
        character1.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 20
        delay(0.05)
        get_events()

