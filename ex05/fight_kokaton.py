import random #randomモジュールのインポート
import sys    #sysモジュールのインポート
import time   #timeモジュールのインポート

import pygame as pg #pygameモジュールをpgとしてインポート

times_now = 0 #現在のtimeの取得の保管
times_mirai = 0 #現在から5秒後のtimeの取得の保管

class Screen:#Screenの表示
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect() 

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


class Bird:#こうかとんの初期設定
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]  
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)                    


class Bomb:#爆弾の初期設定
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)
        

class GameCount:#爆弾の接触毎にこうかとんの画像の表示
    def __init__(self, image_path, ratio, xy):
        self.sfc = pg.image.load(image_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0 , ratio)#ratio = 10.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy #0,0
    
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

class Shot:#弾丸の表示
    def __init__(self, image_path, ratio, vx, vy):
        self.sfc = pg.image.load(image_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0 , ratio)#ratio = 10.0
        self.rct = self.sfc.get_rect()
        self.rct.move_ip(vx, vy)      
          
    def update(self, scr:Screen):
        self.blit(scr)
    
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)


def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def main():
    global times_mirai
    global times_now

    clock =pg.time.Clock()

    # 練習１
    scr = Screen("負けるな！こうかとん", (1600,900), "fig/pg_bg.jpg")
    
    # 練習３
    kkt = Bird("fig/6.png", 2.0, (900,400))
    kkt.update(scr)
    
    bombs = []
    colors = ["red", "green", "blue", "yellow", "magenta"]
    for i in range(5):
        color = colors[i]
        vx = random.choice([-1 , +1])
        vy = random.choice([-1 , +1])
        bombs.append(Bomb(color, 10, (vx , vy), scr))   
    
    # 練習２
    while True:        
        scr.blit()
        key_dct = pg.key.get_pressed() # 辞書型

        if key_dct[pg.K_SPACE]:    
            shot = Shot("fig/shot.gif", 2.0, kkt.rct.centerx - 30, kkt.rct.centery - 100)
            shot.update(scr)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        kkt.update(scr)
        for bomb in bombs:
            bomb.update(scr)
            if kkt.rct.colliderect(bomb.rct):
                times_now = time.time()
                times_mirai = time.time() + 5 if times_mirai == 0 else times_mirai
                if times_now < times_mirai:
                    count = GameCount("fig/3.png", 10.0, (800,450))
                    count.blit(scr)
                else:
                    return
        
        pg.display.update()#displayのアップデート
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()  #pygameを初期化
    main()     #ゲームの実行
    pg.quit()  #pygemeの終了
    sys.exit() #プログラムの終了