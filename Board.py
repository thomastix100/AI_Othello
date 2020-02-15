# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:31:26 2018

@author: eumartinez

"""


from tkinter import *


class App:
       
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.height=600
        self.width=600
        self.grid_column=8
        self.grid_row=8
        self.canvas = Canvas(self.frame, height=self.height, width=self.width)
        self.cellwidth = int(self.canvas["width"])/self.grid_column
        self.cellheight = int(self.canvas["height"])/self.grid_row
        self.draw_grid()
        self.canvas.pack()
        self.model=[[0 for x in range(self.grid_column)] for y in range(self.grid_row)]
        self.player = 1
        self.pos=(0,0)
        self.initial_data()
        
        
        def handler(event, self=self):
            return self.__onClick(event)
        
        self.canvas.bind('<Button-1>', handler)
        
        
        self.hi_there = Button(self.frame, text="Jugar", command=self.start_Game)
        self.hi_there.pack(side=LEFT)
        
    
    def draw_grid(self):
        for i in range(self.grid_row):
            for j in range(self.grid_column):
                #Dibuja los cuadrados en las diferentes posiciones
                x1 = i * self.cellwidth
                y1 = j * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")

        self.draw_initial_sheet()


    def initial_data(self):
        self.model[3][3]=1
        self.model[4][4]=1
        self.model[3][4]=2
        self.model[4][3]=2
        self.player = 2


    def draw_initial_sheet(self):
        x=3*self.cellwidth
        y=3*self.cellheight
        self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='white')
        x=4*self.cellwidth
        y=4*self.cellheight
        self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='white')
        x=3*self.cellwidth
        y=4*self.cellheight
        self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='black')
        x=4*self.cellwidth
        y=3*self.cellheight
        self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='black')

        
        #Se captura donde se dio el clip
    def drawChip(self):
        x=self.pos[1]*self.cellwidth
        y=self.pos[0]*self.cellheight
        #Dibuja un obalo segun el jugador
        if(self.player ==1):
            
            self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='white')
            self.player=2
        else:
            self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='black')
            self.player=1
            
    #Toma un vector y lo que hace es dibujar todas las fichas encerradas segun el jugador
    def drawChips(self):
        for i in range(len(self.model)):
            row=self.model[i]
            for j in range(len(row)):
                val=self.model[i][j]
                x=j*self.cellwidth
                y=i*self.cellheight
                if(val ==1):
                    self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='white')
                elif(val ==2):
                    self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='black')
            
            #Calcula donde dimos click y modifica el modelo
    def __onClick(self, event):
        
            i=int(event.y/self.cellheight)
            j=int(event.x/self.cellwidth)
            self.pos =(i,j)
            if self.model[i][j]==0:
                self.model[i][j]=self.player
            if(self.player==1):
                self.player=2
            else:
                self.player=1
            print(self.model)
            
            self.drawChips()
        
       
    
    def  start_Game(self):
        #Hay que llamar a la clase Triki
        print('start game')
        
        

root = Tk()
app = App(root)
root.mainloop()