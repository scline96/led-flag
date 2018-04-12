#!/usr/bin/env python
# Display a menu
from samplebase import SampleBase
from rgbmatrix import graphics
import time

class RunMenu(SampleBase):
    def __init__(self, *args, **kwargs):
            super(RunMenu, self).__init__(*args, **kwargs)
            
    def run(self):
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            font = graphics.Font()
            font.LoadFont("6x10.bdf")
            green = graphics.Color(0, 128, 0)
            black = graphics.Color(0, 0, 0)

            while True:
                offscreen_canvas.Clear()
                len = graphics.DrawText(offscreen_canvas, font, 2, 30, green, black, "Run Text")
                len = graphics.DrawText(offscreen_canvas, font, 2, 20, black, green, "Run Game")
                
                time.sleep(10)


                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


#main
if __name__ == "__main__":
    run_menu = RunMenu()
    if (not run_menu.process()):
        run_menu.print_help()
