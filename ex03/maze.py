import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm
def key_down(event):
    global key
    global tmr
    global jid
    key = event.keysym
    
def key_up(event):
    global key
    global cx, cy, mx, my, tori

    key = ""
    
    
def start_tk():
    canvas.create_rectangle(100, 100, 200, 200, fill="#48B060", outline="#48B060")
def gole_tk():
    canvas.create_rectangle(1400, 800, 1300, 700, fill="#ff0000", outline="#ff0000")



    

def count_up():
    global tmr
    global jid
    lable ["text"] = tmr
    tmr +=  1
    jid = root.after(1000, count_up)




def main_proc():
    global cx, cy, mx, my, tori

    if key == "Up": 
        cy -= 20
    if key == "Down": cy += 20
    if key == "Left": cx -= 20
    if key == "Right": cx += 20
    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1
    if key == "t":tori = tk.PhotoImage(file="fig/7.png")
    if key == "r":
        mx = 1
        my = 1


    if maze_lst[mx][my] == 1: # 移動先が壁だったら
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1        
    cx, cy = mx*100+50, my*100+50
    canvas.coords("kokaton", cx, cy)
    root.after(100, main_proc)
    
    if mx == 13:
        if my == 7:
            canvas.create_text(
            1400 // 2,
            900 // 2,
            font=("", 80),
            text="ゲームクリア！"
            )
        else:
            pass
    else:
        pass

    

if __name__ == "__main__":
    root = tk.Tk()
    lable = tk.Label(root, text="-",font=("",80))
    lable.pack()
    tmr = 0
    jid = None
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()
    maze_lst = mm.make_maze(15, 9)
    # print(maze_lst)
    mm.show_maze(canvas, maze_lst)
    start_tk()
    gole_tk()


    cx, cy = 300, 400
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    tori = tk.PhotoImage(file="fig/8.png")
    canvas.create_image(cx, cy, image=tori, tag="kokaton")
    key = ""

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()