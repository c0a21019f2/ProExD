import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}ボタンが押されました]")

root = tk.Tk()
root.title("お試しモード")
root.geometry("500x200")

label = tk.Label(
    text="らべるん",font=("", 20)
    
)
#click = tkm.showerror("警告","だめー")
label.pack()




button = tk.Button(root, text="草")
button.bind("<1>", button_click)
button.pack()
"""
image = tk.PhotoImage(file="download.jpg")
canvas = tk.Canvas(width=50,height=80)
canvas.create_image(24,36,image=image)
canvas.pack()
"""

entry = tk.Entry(root, width=30)
entry.insert(tk.END, "fugapiyo")
entry.pack()


root.mainloop()