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

for i in range(59):
	now_boad = boads[-1]
	blank = now_boad.blank
	if now_boad.turn == "":
		break
	while rounds == i:
		rnd = random.randint(0,len(blank)-1)
		row = blank[rnd] / 8
		col = blank[rnd] % 8
		color = now_boad.turn
		masu = now_boad.boad[row][col]
		if now_boad.chk_puttable(masu,color):
			next_boad = now_boad.put(row,col)
			boads.append(next_boad)
			rounds = rounds + 1
#boads[-1].print_boad()
print(boads[-1].game_result())
