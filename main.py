from tkinter import *
from netflixsearch import netflix_data_search

root = Tk()
root.title('NetFlix Top 10')
root.resizable(False, False)

title_font = ('Pursia', 15)
info_font = ('Pursia', 14, 'bold')
display_font = ('Pursia', 12)
# Canvas width and height, with easy center value
can_w = 400
can_h = 340
center = can_w/2

my_canvas = Canvas(root, width=can_w, height=can_h)
my_canvas.pack(fill='both', expand=True)
my_canvas.create_text(center, can_h-15, text='Thank you for using NetFlix Genny')
my_canvas.create_text(center, 20, text='Netflix Top 10!!', font=title_font)
# Info bar
my_canvas.create_text(45, 50, text='Number:', font=info_font)
my_canvas.create_text(160, 50, text='Title', font=info_font)
my_canvas.create_text(280, 50, text='Streak', font=info_font)
my_canvas.create_text(360, 50, text='Views', font=info_font)


# Get and display data
def get_data(btn):
    pos = 80
    gen_data = netflix_data_search()
    for datas in range(0, len(gen_data)):
        my_canvas.create_text(30, pos, text=f'{gen_data[datas][0][0]:>3}', font=display_font)
        my_canvas.create_text(160, pos, text=f'{gen_data[datas][1][0]:^15}', font=display_font)
        my_canvas.create_text(280, pos, text=f'{gen_data[datas][2][0]:>2}', font=display_font)
        my_canvas.create_text(360, pos, text=f'{gen_data[datas][3][0]:<9}', font=display_font)
        pos += 20
    btn.destroy()


# Generate Button
gen_btn = Button(root, text='Generate', bg='grey', command=lambda: get_data(gen_btn))
my_canvas.create_window(center, can_h-80, width=75, height=25, window=gen_btn)

# Exit Button
exit_btn = Button(root, text='Exit', bg='red', command=lambda: root.destroy())
my_canvas.create_window(center, can_h-40, width=65, height=25, window=exit_btn)

root.mainloop()
