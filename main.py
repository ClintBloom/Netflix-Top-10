from tkinter import *
from tkinter import Tk
from netflixsearch import netflix_data_search


root = Tk()
root.title('NetFlix Top 10')
root.resizable(False, False)


can_w = 400
can_h = 340
center = can_w/2

my_canvas = Canvas(root, width=can_w, height=can_h)
my_canvas.pack(fill='both', expand=True)
my_canvas.create_text(can_w/2, can_h-15, text='Thank you for using NetFlix Genny')
my_canvas.create_text(can_w/2, 20, text='Netflix Top 10!!', font=('Pursia', 15))


def get_data(btn):
    pos = 60
    gen_data = netflix_data_search()
    for datas in range(0, len(gen_data)):
        my_canvas.create_text(200, pos, text=gen_data[datas])
        pos += 20
    btn.destroy()


# Buttons
gen_btn = Button(root, text='Generate', bg='grey', command=lambda: get_data(gen_btn))
my_canvas.create_window(center, can_h-80, width=75, height=25, window=gen_btn)


# Exit Button
exit_btn = Button(root, text='Exit', bg='red', command=lambda: root.destroy())
my_canvas.create_window(center, can_h-40, width=65, height=25, window=exit_btn)

root.mainloop()