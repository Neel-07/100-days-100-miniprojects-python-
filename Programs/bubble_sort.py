import tkinter as tk
import random
import time

def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                update_bars(data, ['skyblue' if x != j and x != j + 1 else 'red' for x in range(len(data))])
                time.sleep(0.3)
                root.update_idletasks()

def update_bars(data, colors):
    canvas.delete('all')
    bar_width = 20
    spacing = 5
    x_offset = 10
    for i, height in enumerate(data):
        x0 = i * (bar_width + spacing) + x_offset
        y0 = canvas_height - height * 5
        x1 = (i + 1) * (bar_width + spacing) + x_offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colors[i])
        canvas.create_text(x0 + 10, y0 - 10, anchor=tk.SW, text=str(data[i]))

def start_sorting():
    global data
    bubble_sort(data)
    update_bars(data, ['skyblue' for _ in range(len(data))])

def generate_data():
    global data
    data = random.sample(range(1, 15), 10)
    update_bars(data, ['skyblue' for _ in range(len(data))])

root = tk.Tk()
root.title("Bubble Sort Visualization")
root.geometry("400x300")

canvas_height = 250
canvas_width = 300
canvas = tk.Canvas(root, height=canvas_height, width=canvas_width)
canvas.pack()

generate_button = tk.Button(root, text="Generate Data", command=generate_data)
generate_button.pack()

start_button = tk.Button(root, text="Start Sorting", command=start_sorting)
start_button.pack()

data = random.sample(range(1, 15), 10)
update_bars(data, ['skyblue' for _ in range(len(data))])

root.mainloop()

