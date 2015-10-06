#!/usr/bin/python
#-*- coding: utf-8 -*-

#othello with monte carlo algorism

from util import *
from boad import *
import random
import math

#盤面状態表示
boad = Boad()

boads = list()
boads.append(boad)
rounds = 0

for i in range(60):
	now_boad = boads[-1]
	blank = now_boad.blank
	tmp_blank = list(blank)
	if now_boad.turn == "":
		break
	while rounds == i:
		rnd = random.randint(0,len(tmp_blank)-1)
		row = tmp_blank[rnd] / 8
		col = tmp_blank[rnd] % 8
		color = now_boad.turn
		masu = now_boad.boad[row][col]
		if now_boad.chk_puttable(masu,color):
			next_boad = now_boad.put(row,col)
			boads.append(next_boad)
			rounds = rounds + 1
		else:
			tmp_blank.pop(rnd)
			if len(tmp_blank) == 0:
				now_boad.turn = ""
				break
last = boads[-1]
last.print_boad()
black_num = len(filter(lambda masu: masu.state == "black",last.all_masu))
white_num = len(filter(lambda masu: masu.state == "white",last.all_masu))
print(black_num,white_num)
print(last.game_result())
