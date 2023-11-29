import tkinter as tk
import random
import time

WIDTH, HEIGHT = 800, 600
PAUSE_AMOUNT = 0.03
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
DIRECTIONS = ['up_right', 'up_left', 'down_right', 'down_left']

def move_logo(logo):
    original_direction = logo['direction']
    x, y = logo['x'], logo['y']
    if x == 0 and y == 0:
        logo['direction'] = 'down_right'
    elif x == 0 and y == HEIGHT - 50:
        logo['direction'] = 'up_right'
    elif x == WIDTH - 50 and y == 0:
        logo['direction'] = 'down_left'
    elif x == WIDTH - 50 and y == HEIGHT - 50:
        logo['direction'] = 'up_left'
    elif x == 0 and logo['direction'] == 'up_left':
        logo['direction'] = 'up_right'
    elif x == 0 and logo['direction'] == 'down_left':
        logo['direction'] = 'down_right'
    elif x == WIDTH - 50 and logo['direction'] == 'up_right':
        logo['direction'] = 'up_left'
    elif x == WIDTH - 50 and logo['direction'] == 'down_right':
        logo['direction'] = 'down_left'
    elif y == 0 and logo['direction'] == 'up_left':
        logo['direction'] = 'down_left'
    elif y == 0 and logo['direction'] == 'up_right':
        logo['direction'] = 'down_right'
    elif y == HEIGHT - 50 and logo['direction'] == 'down_left':
        logo['direction'] = 'up_left'
    elif y == HEIGHT - 50 and logo['direction'] == 'down_right':
        logo['direction'] = 'up_right'

    if logo['direction'] != original_direction:
        logo['color'] = random.choice(COLORS)

    if logo['direction'] == 'up_right':
        logo['x'] += 2
        logo['y'] -= 1
    elif logo['direction'] == 'up_left':
        logo['x'] -= 2
        logo['y'] -= 1
    elif logo['direction'] == 'down_right':
        logo['x'] += 2
        logo['y'] += 1
    elif logo['direction'] == 'down_left':
        logo['x'] -= 2
        logo['y'] += 1

    canvas.coords(logo['id'], logo['x'], logo['y'])

def animate():
    for logo in logos:
        move_logo(logo)
    canvas.after(10, animate)

root = tk.Tk()
root.title('Bouncing DVD Logo')
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
canvas.pack()

logos = []
for i in range(5):
    x = random.randint(0, WIDTH - 50)
    y = random.randint(0, HEIGHT - 50)
    logos.append({
        'x': x,
        'y': y,
        'direction': random.choice(DIRECTIONS),
        'color': random.choice(COLORS),
        'id': canvas.create_text(x, y, text='DVD', fill=random.choice(COLORS), font=('Arial', 14, 'bold'))
    })

animate()
root.mainloop()
