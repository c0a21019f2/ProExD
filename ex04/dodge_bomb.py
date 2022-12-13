import pygame as pg
import sys
def main():
    clock = pg.time.Clock()
    
    
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    
    tori_sfc = pg.image.load("fig/pg_bg.jpg")
    
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 400,300
    scrn_sfc.blit(tori_sfc, tori_rct)#scrn_sfcにtori_rctに従ってtori_sfcに張り付ける
    #tmr = 32
    #fonto = pg.font.Font(tmr, 80)
    #txt = fonto.render(str(tmr), True, WHITE)
    #scrn_sfc.blit(txt, (300,200))
    
    pg.display.update()
    clock.tick(0.1)#10秒

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
