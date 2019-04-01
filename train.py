import screen_capture.region_of_interest as ri
import screen_capture.screen_capture as sc
import robotic_automation.robot as rb
import io_recognition.ocr as oc

import curses

screen_capture = sc.ScreenCapture()
robot_tools = rb.Robot()

stdscr = curses.initscr()

# game-over select
reg = ri.select_region()
screen_capture.create_new_region("over", reg)

# game-region select
reg = ri.select_region()
screen_capture.create_new_region("game", reg)

# score select
reg = ri.select_region()
screen_capture.create_new_region("score", reg)

while True:
    key = stdscr.getch()
    if key == 27:
        curses.endwin()
        break

    regions = screen_capture.get_next()
    number = oc.ocr_number(regions["score"])
