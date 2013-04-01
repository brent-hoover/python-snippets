#!/usr/bin/env python
#
# [SNIPPET_NAME: Drawing With Cairo]
# [SNIPPET_CATEGORIES: PyGTK, Cairo]
# [SNIPPET_DESCRIPTION: Create a drawing with cairo]
# [SNIPPET_AUTHOR: Jurjen Stellingwerff <jurjen@stwerff.xs4all.nl>]
# [SNIPPET_LICENSE: GPL]

# example cairo_demo.py

import pygtk
pygtk.require('2.0')
import gtk
import math
import cairo

class DrawingAreaExample:
    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Drawing With Cairo")
        window.connect("destroy", lambda w: gtk.main_quit())
        self.area = gtk.DrawingArea()
        self.area.set_size_request(380, 300)
        window.add(self.area)
        self.area.connect("expose-event", self.expose)
        self.area.show()
        window.show()

    def expose(self, area, event):
        self.context = area.window.cairo_create()
        self.context.rectangle(event.area.x, event.area.y, event.area.width,
            event.area.height)
        self.context.clip()
        self.context.scale(event.area.width/380.0, event.area.height/300.0)
        self.draw_point(10,10)
        self.draw_points(110, 10)
        self.draw_line(210, 10)
        self.draw_lines(310, 10)
        self.draw_segments(10, 100)
        self.draw_rectangles(110, 100)
        self.draw_arcs(210, 100)
        self.draw_pixmap(310, 100)
        self.draw_polygon(10, 200)
        self.draw_rgb_image(110, 200)
        self.context.move_to(210, 290)
        self.context.show_text("Try to resize the window")
        return False

    def point(self, x, y):
        self.context.arc(x, y, 1, 0.0, 2.0 * math.pi)
        self.context.fill()

    def draw_point(self, x, y):
        self.point(x+30, y+30)
        self.context.move_to(x+5, y+50)
        self.context.show_text("Point")
        return

    def draw_points(self, x, y):
        points = [(x+10,y+10), (x+10,y), (x+40,y+30),
                 (x+30,y+10), (x+50,y+10)]
        for px,py in points:
            self.point(px,py)
        self.context.move_to(x+5, y+50)
        self.context.show_text("Points")
        return

    def draw_line(self, x, y):
        self.context.move_to(x+10, y+10)
        self.context.line_to(x+20, y+30)
        self.context.stroke()
        self.context.move_to(x+5, y+50)
        self.context.show_text("Line")
        return

    def draw_lines(self, x, y):
        points = [(x+10,y), (x+40,y+30),
                  (x+30,y+10), (x+50,y+10)]
        self.context.move_to(x+10, y+10)
        for px,py in points:
            self.context.line_to(px, py)
        self.context.set_line_width(4.5)
        self.context.stroke()
        self.context.save()
        self.context.set_source_rgb(1, 1, 0.7)
        self.context.translate(1.5, 1)
        self.context.move_to(x+10, y+10)
        for px,py in points:
            self.context.line_to(px, py)
        self.context.set_line_width(1.5)
        self.context.stroke()
        self.context.restore()
        self.context.set_line_width(2)
        self.context.move_to(x+5, y+50)
        self.context.show_text("Lines")
        return

    def draw_segments(self, x, y):
        segments = ((x+20,y+10, x+20,y+70), (x+60,y+10, x+60,y+70),
            (x+10,y+30 , x+70,y+30), (x+10, y+50 , x+70, y+50))
        for fx, fy, tx, ty in segments:
            self.context.move_to(fx, fy)
            self.context.line_to(tx, ty)
        self.context.stroke()
        self.context.move_to(x+5, y+90)
        self.context.show_text("Segments")
        return

    def draw_rectangles(self, x, y):
        self.context.save()
        self.context.set_source_rgb(.6, 0, 0)
        self.context.rectangle(x, y, 80, 70)
        self.context.stroke()
        self.context.restore()
        rectangles = ((x+10, y+10, 20, 20), (x+50, y+10, 20, 20), (x+20, y+50, 40, 10))
        for px, py, h, w in rectangles:
            self.context.rectangle(px, py, h, w)
            self.context.fill()
        self.context.move_to(x+5, y+90)
        self.context.show_text("Rectangles")
        return

    def draw_arcs(self, x, y):
        self.context.set_line_width(1)
        arcs = [(False, x+45, y+35, 35),
            (True, x+35, y+25, 5),
            (True, x+55, y+25, 5)]
        for fill, px, py, r in arcs:
            self.context.move_to(px+r, py)
            self.context.arc(px, py, r, 0, 2*math.pi)
            if fill:
                self.context.fill()
            else:
                self.context.set_source_rgb(1, 1, 0.5)
                self.context.fill_preserve()
                self.context.set_source_rgb(0, 0, 0)
                self.context.stroke()
        self.context.move_to(x+45, y+35)
        s = 1.66
        self.context.save()
        self.context.scale(1, s)
        self.context.arc(x+45, (y+35)/s, 15, 30*math.pi/180, 150*math.pi/180)
        self.context.restore()
        self.context.save()
        self.context.move_to(x+5, y+90)
        self.context.select_font_face("serif", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        self.context.show_text("Arcs")
        self.context.restore()
        return

    def draw_pixmap(self, x, y):
        try:
            img = cairo.ImageSurface.create_from_png("gtk.png")
        except Exception, e:
            print e
            exit(1)
        self.context.save()
        self.context.set_source_surface(img, x+5, y+15)
        self.context.paint()
        self.context.restore()
        self.context.move_to(x+5, y+90)
        self.context.show_text("Pixmap")
        return

    def draw_polygon(self, x, y):
        points = [(x+10,y+20), (x+40,y+70),
                  (x+30,y+30), (x+50,y+40)]
        self.context.move_to(x+10, y+60)
        for px,py in points:
            self.context.line_to(px, py)
        self.context.fill()
        self.context.move_to(x+5, y+90)
        self.context.show_text("Polygon")
        return

    def draw_rgb_image(self, x, y):
        s = 80
        h = 40
        self.context.save()
        linpat = cairo.LinearGradient(x, y, x+s, y+s)
        linpat.add_color_stop_rgb(0.0, 1, 1, 1)
        linpat.add_color_stop_rgb(1.0, 0, 1, 0)
        self.context.set_source(linpat)
        self.context.move_to(x,y)
        self.context.line_to(x,y+s)
        self.context.line_to(x+s,y+s)
        self.context.line_to(x+s,y)
        self.context.fill()
        linpat = cairo.LinearGradient(x, y+s, x+s, y)
        linpat.add_color_stop_rgba(0.0, 0, 0, 1, 1)
        linpat.add_color_stop_rgba(0.5, 1, 0, 1, 0)
        linpat.add_color_stop_rgba(1.0, 1, 0, 0, 1)
        self.context.set_source(linpat)
        self.context.move_to(x,y)
        self.context.line_to(x,y+s)
        self.context.line_to(x+s,y+s)
        self.context.line_to(x+s,y)
        self.context.fill()
        self.context.restore()
        self.context.save()
        self.context.move_to(x+5, y+92)
        self.context.set_font_size(11.5)
        self.context.show_text("RGB Image")
        self.context.restore()
        return

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    DrawingAreaExample()
    main()

