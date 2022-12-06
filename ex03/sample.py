import tkinter as tk
import tkinter.messagebox as tkm

def count_up():
    global tmr
    global jid
    lable ["text"] = tmr
    tmr +=  1
    jid = root.after(1000, count_up)
    
def key_down(event):
    global jid
    print(jid)
    if jid is not None:#カウントアップ中にキーが押されたら
        #カウントアップ中でなければjid is None
        root.after_cancel(jid)
        jid = None#一回だけ
    else:
        jid = root.after(1000,count_up)#count_upが呼び出されるたび

        
    key = event.keysym

    #tkm.showinfo("キー押した",f"{key}キーが押されました")

    
if __name__ == "__main__":
    root = tk.Tk()
    lable = tk.Label(root, text="-",font=("",80))
    lable.pack()
    tmr = 0
    jid = None
    #count_up()
    root.bind("<KeyPress>", key_down)
    root.mainloop()