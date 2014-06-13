# -*- coding: utf-8 -*-
import operator
import itertools
import unittest

from game2048lib import Game2048


class TestGame(unittest.TestCase):
    def test_connection(self):
        game = Game2048()
        self.assertIn('2048', game._browser.title)

    def test_get_grid(self):
        game = Game2048()
        grid = game.grid

        self.assertEquals(len(grid), 4)

        for row in grid:
            self.assertEquals(len(row), 4)
            for cell in row:
                if not cell is None:
                    self.assertIsInstance(cell, int)

        # every started game has got only 2 numbers
        int_list = [x for x in itertools.chain(*grid) if not x is None]
        self.assertEquals(len(int_list), 2)

    def test_start_new_game(self):
        game = Game2048()

        first_grid = game.grid

        game.start_new_game()

        second_grid = game.grid

        is_different =reduce(
            operator.or_,
            [x != y for x, y in  itertools.izip(
                itertools.chain(*first_grid),
                itertools.chain(*second_grid)
            )]
        )
        self.assertTrue(is_different)

    def test_score(self):
        game = Game2048()

        self.assertEquals(game.score, 0)

    def test_change_score_after_moves(self):
        game = Game2048()

        game.move_left()
        game.move_down()
        game.move_right()
        game.move_up()

        self.assertGreater(game.score, 0)
