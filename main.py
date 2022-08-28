import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, filedialog
import get_posts
import lootdl


def helloCallBack(picked):
   messagebox.showinfo(picked)

path =''

my_dir='' # string to hold directory path 
def my_fun(): 
    my_dir = filedialog.askdirectory() # select directory 
    print(my_dir)
    l1.config(text=my_dir) # update the text of Label with directory path



def select():
    curItems = tree.selection()
    list = []
    list.append([str(tree.item(i)['values'][1]) for i in curItems])
    # text="\n".join([str(tree.item(i)['values'][1]) for i in curItems])
    # print(text)
    my_dir = filedialog.askdirectory()
    path = my_dir + '/'
    for url in list[0]:
        lootdl.grab(url, path)

root = tk.Tk()
root.title('Audio Scene - Drumkit Downloader')
buttons = ttk.Frame(root)
buttons.pack(side=tk.TOP, anchor=tk.NW, pady = 5, padx= 5)
# button1= ttk.Button(buttons, text= "Select Download Folder", cursor="hand2", command=lambda:my_fun())
# button1.pack(side = tk.LEFT)
l1=tk.Label(buttons,text="Trending Drumkits",width=30,font=('14'),borderwidth=2,relief="groove",background='white')
l1.pack()

dl_btn = ttk.Button(root, text="Download", command= lambda: select())
dl_btn.pack(side=tk.BOTTOM, anchor=tk.SE, pady=[10], padx=[10])
tree = ttk.Treeview(root, height=10)

tree['show'] = 'headings'
tree['columns'] = ('Name', 'Link', 'Author', 'Votes')
tree.heading("#1", text='Name', anchor='w')
tree.column("#1", stretch="no", width=400)
tree.heading("#2", text='Link', anchor='w')
tree.column("#2", stretch="no", width=160)
tree.heading("#3", text='Author', anchor='w')
tree.column("#3", stretch="no", width=160)
tree.heading("#4", text='Votes', anchor='w')
tree.column("#4", stretch="yes", width=80)
tree.pack()

drumkit_list = get_posts.get_data()
for x in drumkit_list:
    tree.insert("", "end", values=x)

tree.bind(dl_btn, lambda e: select())

root.mainloop()