#!/usr/bin/env python

import curses


x = 0
screen = curses.initscr()

#sub window inside the main screen
begin_x = 10 ; begin_y = 2
height = 5 ; width = 50
subscreen = screen.subwin(height, width, begin_y, begin_x)

while x != ord('4'):

	screen.clear()

	subscreen.clear()
	subscreen.box()
#like printf
	subscreen.addstr(2, 2, "codigo ascii del caracter presionado %d" % (x))
	subscreen.refresh()

	screen.border(0)
	screen.addstr(8, 2, "Please enter a number...")
	screen.addstr(9, 4, "1 - Who Am I")
	screen.addstr(10, 4, "2 - Actual Directory")
	screen.addstr(11, 4, "3 - Show disk space")
	screen.addstr(12, 4, "4 - Exit")
	screen.refresh()

	x = screen.getch()


curses.endwin()

