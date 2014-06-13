game2048lib
===========

Library for playing 2048(http://gabrielecirulli.github.io/2048/) from python


Setup library
-------------

```
    $ pip install git+https://github.com/Zapix/game2048lib
```


Example of usage
----------------

```python
    >>> from game2048lib import Game2048
    >>> game = Game2048()
    >>> game.move_left()
    >>> game.score
    4
```


Documentation
-------------

*game2048lib.Game2048* - class of game. Game starts when creates instance of this class

*game2048lib.Game2048.grid* - current grid of game. List of list. example:

```python
    >>> game.grid
    [
        [4, None, None, None],
        [2, None, None, None],
        [None, None, 4, None],
        [None, None, None, None]
    ]
```

*game2048lib.Game2048.score* - current score of game

*game2048lib.Game2048.start_new_game()* - method for starting new game

*game2048lib.Game2048.move_up()* - move up

*game2048lib.Game2048.move_left()* - move left

*game2048lib.Game2048.move_down()* - move down

*game2048lib.Game2048.move_right()* - move right
