# -*- coding: utf-8 -*-
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Game2048(object):
    _GAME_URL = 'http://gabrielecirulli.github.io/2048/'

    def __init__(self):
        self._browser = webdriver.Firefox()
        self._browser.get(self._GAME_URL)
        self._grid = None

    def __del__(self):
        self._browser.close()

    @property
    def grid(self):
        """
        :return: List of list with none or int elements
        """
        if not self._grid is None:
            return self._grid

        self._grid = [[None]*4 for x in xrange(4)]

        tiles = self._browser.find_elements_by_class_name('tile')

        for tile in tiles:
            position_search_obj = re.search('tile-position-\d-\d',
                                            tile.get_attribute('class'))
            position_str = position_search_obj.group()

            x, y = [int(x) - 1 for x in re.findall('\d', position_str)]
            value = int(tile.find_element_by_class_name('tile-inner').text)

            self.grid[x][y] = value

        return self.grid

    @property
    def score(self):
        score_div = self._browser.find_element_by_class_name('score-container')
        return int(re.findall('\d+', score_div.text)[0])

    def start_new_game(self):
        self._grid = None
        restart_button = self._browser.find_element_by_class_name(
            'restart-button'
        )
        restart_button.click()

    def _move(self, key):
        self._grid = None
        html = self._browser.find_element_by_tag_name('html')
        html.send_keys(key)

    def move_up(self):
        self._move(Keys.ARROW_UP)

    def move_down(self):
        self._move(Keys.ARROW_DOWN)

    def move_left(self):
        self._move(Keys.ARROW_LEFT)

    def move_right(self):
        self._move(Keys.ARROW_RIGHT)

