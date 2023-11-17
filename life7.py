# ##hw life 7
import pygame as pg
import numpy as np
from random import randint

fps=30
wig,high= 400, 400
size=10
y=0
r_w =40
r_h = 40

alive= (0, 255, 0)
dead = (0, 0, 0)

class life(object):
    def __init__(self, w, h, xy, sp):
        self.w=wig 
        self.h =high
        self.xy= size
        self.scr = self.h,self.w
        self.screen = pg.display.set_mode(self.scr)
        self.cellw = self.w/self.xy
        self.cellh = self.h/self.xy
        self.sp= fps
        self.input_mode = True
        self.fin=False
        self.matrica=0
    
    
    def grid(self, cellw, cellh):
        matrica = [ [0]*self.cellh for i in range(self.cellw) ]
        for i in range(self.cellw):
            for j in range(self.cellh):
                matrica [i,j] = randint(0,1)
                
        return self.matrica
    
    def draw_grid(self):
        cz=self.xy
        for x in range(self.cellh):
            for y in range(self.cellw):
                rect = pg.Rect(x*cz, y*cz, cz, cz)
                if self.matrica[x][y] == 1:
                    pg.draw.rect(self.screen,(100,0,0), rect)
                else:
                    pg.draw.rect(self.screen, (0, 100,0), rect)


    def rules(self):
        nmatrica = np.zeros(self)
        
        for i in range(self.cellh):
            for j in range(self.cellw):
                sneigh=0
                left = (j-1) % self.xy
                right = (j+1) % self.xy
                up = (i-1) % self.xy
                down = (i+1) % self.xy

                neighbors = [self.matrica[i, left], self.matrica[i, right],
                            self.matrica[up, j], self.matrica[down, j],
                            self.matrica[up, left], self.matrica[up, right],
                            self.matrica[down, left], self.matrica[down, right]]
                sneigh = sum(neighbors)

                if self.matrica[i, j] == 1:
                    if 2 <= sneigh <= 3:
                        nmatrica[i, j] = 1 
                    else: 0
                if self.matrica:
                    if sneigh == 3 :
                        nmatrica[i, j] = 1
                    else: 0

        self.matrica = nmatrica
    
    def run(self):
        pg.init()
        clock = pg.time.Clock()
        while not self.fin:
            clock.tick(self.fps)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.fin = True

            self.update_state()
            self.draw_grid()

            pg.display.flip()

        pg.quit()

if __name__ == "__main__":
    main()
