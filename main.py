from tkinter import *
from tkinter import Label
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


# Get Data from Netflix top 10 website
# Each element is dependent of each other
class DataCreator:
    data = netflix_data_search()
    top_ten = []
    amount = 0
    pos = 60

    def __init__(self):
        for d in self.data:
            self.top_ten.append([Label(root, text=d[0][0], font=display_font),
                                Label(root, text=d[1][0], font=display_font),
                                Label(root, text=d[2][0], font=display_font),
                                Label(root, text=d[3][0], font=display_font)])

            self.top_ten[self.amount][0].place(x=20, y=self.pos)
            self.top_ten[self.amount][1].place(x=50, y=self.pos)
            self.top_ten[self.amount][2].place(x=270, y=self.pos)
            self.top_ten[self.amount][3].place(x=310, y=self.pos)
            self.pos += 21
            self.amount += 1


def btn_destroy(btn):
    btn.destroy()


# to be added
def clear_data():
    for main_list in DataCreator.top_ten:
        for label in main_list:
            label.destroy()
    DataCreator.top_ten.clear()


# Generate Button
gen_btn = Button(root, text='Generate', bg='grey', command=lambda: [DataCreator(), btn_destroy(gen_btn)])
my_canvas.create_window(center, can_h-80, width=75, height=25, window=gen_btn)

# Clear Button
clear_btn = Button(root, text='Clear', bg='grey', command=lambda: clear_data())
my_canvas.create_window(300, can_h-40, width=40, height=25, window=clear_btn)

# Exit Button
exit_btn = Button(root, text='Exit', bg='red', command=lambda: root.destroy())
my_canvas.create_window(center, can_h-40, width=65, height=25, window=exit_btn)

root.mainloop()
