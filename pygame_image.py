import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #練習1
    rbg_img = pg.transform.flip(bg_img, True, False) #練習8
    kk_img = pg.image.load("fig/3.png") #練習3
    kk_img = pg.transform.flip(kk_img, True, False) #練習3
    kk_rct = kk_img.get_rect() #練習10-1
    kk_rct.center = 300, 200 #練習10-2
    screen.blit(kk_img, kk_rct) 
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed() #練習10-3
        if key_lst[pg.K_UP]: #練習10-4
            kk_rct.move_ip((0, -1))
        if key_lst[pg.K_DOWN]: #練習10-4
            kk_rct.move_ip((0, +1))
        if key_lst[pg.K_LEFT]: #練習10-4
            kk_rct.move_ip((-1, 0))
        if key_lst[pg.K_RIGHT]: #練習10-4
            kk_rct.move_ip((+1, 0))

        x = tmr % 3200 #練習5 背景画像移動用変数/練習9 ループ
        screen.blit(bg_img, [-x, 0]) #練習2 
        screen.blit(rbg_img, [-x + 1600, 0]) #練習7,8
        screen.blit(bg_img, [-x + 3200, 0]) #練習9
        #screen.blit(kk_img, [300, 200]) #練習4
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習6 FPSの変更

 
        



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()