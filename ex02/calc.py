import tkinter as tk
import tkinter.messagebox as tkm


count = 0

#練習3
def button_click(event):
    global count
    count += 1

    btn = event.widget
    num = btn["text"]
    if num == "=":
        siki = entry.get()#数式の文字列
        result = eval(siki)
        entry.delete(0, tk.END)#文字列の削除
        entry.insert(tk.END, result)
    elif num == "C":
        
        entry.delete(0,1)
    elif num == "AC":
        entry.delete(0, tk.END)
    
    elif num == "%":
        siki = entry.get()#数式の文字列
        result = int(siki)/100
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    elif num == "CE":
        entry.delete(count-2, count-1)
        count -= 2
    else:
        entry.insert(tk.END, num)#[=]以外のボタン

    #tkm.showinfo("", f"{num}ボタンがクリックされました")
    #練習6
    
    

#練習1
root = tk.Tk()
root.title("calc.py")
root.geometry("400x700")

#練習4
entry = tk.Entry(root, justify="right", width=10, font=("",40))
entry.grid(row = 0, column=0, columnspan=3)

#練習2
r, c = 2, 0
for num in range(9, -1, -1):
    button = tk.Button(root, text=f"{num}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)

    c += 1
    if c%3 == 0:
        r += 1
        c = 0

#練習5

operators = ["", "="]
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1

    if c%3 == 0:
        r += 1
        c = 0
operators_add = [ "/", "*", "-","+"]
r = 2

for ope in operators_add:
    c = 3
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c )
    button.bind("<1>", button_click)
    r += 1
    
operators_d = ["%","CE","AC", "C"]
r = 1
c = 0

for ope in operators_d:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c )
    button.bind("<1>", button_click)
    c += 1

root.mainloop()