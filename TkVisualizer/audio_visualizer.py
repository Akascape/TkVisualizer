import tkinter as tk
import random

class TkAudioVisualizer(tk.Frame):
    def __init__(self,
                 master: any,
                 gradient: list=["cyan","blue"],
                 bar_color: str="white",
                 bar_width: int=7,
                 **kwargs):
        
        tk.Frame.__init__(self, master)
        self.viz = draw_bars(self, gradient[0], gradient[1], bar_width, bar_color, relief="sunken", **kwargs)
        self.viz.pack(fill="both", expand=True)
        
    def start(self):
        """ start the vizualizer """
        if not self.viz._running:
            self.viz._running = True
            self.viz.update()
        
    def stop(self):
        """ stop the visualizer """
        self.viz._running = False
    
class draw_bars(tk.Canvas):
    '''A gradient frame which uses a canvas to draw the background'''
    def __init__(self, parent, color1, color2,  bar_width, bar_color, **kwargs):
        tk.Canvas.__init__(self, parent, bg=bar_color, bd=0, highlightthickness=0, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self._bar_width = bar_width
        self._running = False
        self.after(100, lambda: self._draw_gradient())
        self.bind("<Configure>", lambda e: self._draw_gradient() if not self._running else None)
    
    def _draw_gradient(self, event=None):
        '''Draw the gradient spectrum '''
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width+10
        
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit
         
        for i in range(0, limit, self._bar_width):
            bar_height = random.randint(int(limit/8),int(limit/2.5))
            if not self._running:
                bar_height = height
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))

            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(i,0,i,bar_height, tags=("gradient",), width=self._bar_width, fill=color)
            
        self.lower("gradient")
        
        if self._running:
            self.after(150, self._draw_gradient)
            
    def update(self):
        self._draw_gradient()
