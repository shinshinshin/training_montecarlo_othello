#!/usr/bin/python
#-*- coding: utf-8 -*-

#othello with monte carlo algorism

from boad import *

boad = Boad()
boads = one_game(boad)

last = boads[-1]
last.print_boad()
black_num = len(filter(lambda masu: masu.state == "black",last.all_masu))
white_num = len(filter(lambda masu: masu.state == "white",last.all_masu))
print(black_num,white_num)
print(last.game_result())
