import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    ton = pg.image.load("ex01/fig/3.png")
    ton = pg.transform.flip(ton, True, False)
    ls = []
    for i in range(20):
        if i <= 10:
            ls.append(pg.transform.rotozoom(ton, i, 1.0))
        else:
            ls.append(pg.transform.rotozoom(ton, (20-i), 1.0))
    #ls = [ton, pg.transform.rotozoom(ton, 10, 1.0)]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200
        if x < 1600:
            screen.blit(bg_img, [-x, 0])
            screen.blit(pg.transform.flip(bg_img,True,False), [1600-x, 0])
        else:
            screen.blit(bg_img, [3200-x, 0])
            screen.blit(pg.transform.flip(bg_img,True,False), [1600-x, 0])
        screen.blit(ls[tmr%20], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()