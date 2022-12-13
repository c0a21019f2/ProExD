import pygame as pg
import random
import sys
import time

#クリアー後の文字の入れ替えの処理のための変数95行目から使う
times_now = 0 #現在のtimeの取得
times_mirai = 0 #現在から1秒後のtimeの取得
flagu = 0 #クリアー前後のフラグ

def check_bound(obj_rct, scr_rct):#壁に当たる爆弾ごとの判定
    # 第1引数：こうかとんrectまたは爆弾rect
    # 第2引数：スクリーンrect
    # 範囲内：+1／範囲外：-1
    yoko1, tate1 = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko1 = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate1 = -1
    return yoko1, tate1
    yoko2, tate2 = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko2 = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate2 = -1
    return yoko2, tate2
    yoko3, tate3 = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko3 = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate3 = -1
    return yoko3, tate3
def main():
    global times_mirai, times_now, flagu
    clock =pg.time.Clock()
    # 練習１
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1000, 600))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()
    # 練習３
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    scrn_sfc.blit(tori_sfc, tori_rct) #こうかとんのblit
    
    #タイマーの初期設定
    counter, text = 10, '10'.rjust(3)
    pg.time.set_timer(pg.USEREVENT,1000)
    font = pg.font.SysFont('Consolas',30)
    
    
    # 練習５
    bomb_sfc = pg.Surface((20, 20)) # 正方形の空のSurface
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct1 = bomb_sfc.get_rect()
    bomb_rct1.centerx = random.randint(0, scrn_rct.width)
    bomb_rct1.centery = random.randint(0, scrn_rct.height)
    bomb_rct2 = bomb_sfc.get_rect()
    bomb_rct2.centerx = random.randint(0, scrn_rct.width)
    bomb_rct2.centery = random.randint(0, scrn_rct.height)
    bomb_rct3 = bomb_sfc.get_rect()
    bomb_rct3.centerx = random.randint(0, scrn_rct.width)
    bomb_rct3.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct1) #爆弾1のblit
    scrn_sfc.blit(bomb_sfc, bomb_rct2) #爆弾2のblit
    scrn_sfc.blit(bomb_sfc, bomb_rct3) #爆弾3のblit

    vx1, vy1 = +1, +1
    vx2, vy2 = +1, +1
    vx3, vy3 = +1, +1

    # 練習２
    key_dct = pg.key.get_pressed() # 辞書型

    #ライフの設定
    life = 100
    

    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) #背景のblit
        for event in pg.event.get():
            if event.type == pg.USEREVENT:
                counter -= 1
                if counter > 0:
                    text = str(counter).rjust(3) 
                else:
                    times_now = time.time()

                    times_mirai = time.time() + 1 if times_mirai == 0 else times_mirai
                    if times_now < times_mirai:
                        text = 'gameclear!'.rjust(3)
                    else:
                        text = 'EXIT is please Esc PUSH'.rjust(3) 
                        flagu = 1
                                        
                
            if event.type == pg.QUIT:
                return
        # 練習4
        key_dct = pg.key.get_pressed() # 辞書型
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            # どこかしらはみ出ていたら
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1   
                
            #ゲームクリア時に抜けられる 
        if key_dct[pg.K_ESCAPE]: 
            if flagu == 1:
                return
                    
        scrn_sfc.blit(tori_sfc, tori_rct) #こうかとんのblit
        # 練習６
        bomb_rct1.move_ip(vx1, vy1)
        scrn_sfc.blit(bomb_sfc, bomb_rct1) #爆弾1をスクリーンにblit
        yoko1, tate1 = check_bound(bomb_rct1, scrn_rct)
        bomb_rct2.move_ip(vx2, vy2)
        scrn_sfc.blit(bomb_sfc, bomb_rct2) #爆弾2をスクリーンにblit
        yoko2, tate2 = check_bound(bomb_rct2, scrn_rct)
        bomb_rct3.move_ip(vx3, vy3)
        scrn_sfc.blit(bomb_sfc, bomb_rct3) #爆弾3をスクリーンにblit
        yoko3, tate3 = check_bound(bomb_rct3, scrn_rct)
        vx1 *= yoko1
        vy1 *= tate1
        vx2 *= yoko2
        vy2 *= tate2
        vx3 *= yoko3
        vy3 *= tate3

        # 練習８
        if tori_rct.colliderect(bomb_rct1):
            life -= 1
            #デバック用
            #print("通った")
            if life < 0:
                return
            
        if tori_rct.colliderect(bomb_rct2):
            life -= 1
            if life < 0:
                return
        if tori_rct.colliderect(bomb_rct3):
            life -= 1
            if life < 0:
                return
        #デバック用   
        #print(life)
        #タイマー実装
        scrn_sfc.blit(font.render("lefttime:"+text, True, (0, 0, 0)), (0, scrn_rct.left))
        pg.display.flip()
        scrn_sfc.blit(font.render("liftlife:"+str(life), True, (0,0,0)), (0,scrn_rct.left+30))

        pg.display.update()
        clock.tick(1000)#1000fpsの時を刻む

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()