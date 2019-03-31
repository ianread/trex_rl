import pyautogui as _pag

class Robot(object):
    def __init__(self):
        super()
    def click_region(self, region):
        click_x = int(region['x'] + (region['width'] / 2))
        click_y = int(region['y'] + (region['height'] / 2))
        _pag.moveTo(click_x, click_y, duration=0.25)
        _pag.click(click_x, click_y, button='left')

    def press_down(self):
        _pag.press('down')

    def press_up(self):
        _pag.press('up')

    def press_space(self)
        _pag.press('space')

