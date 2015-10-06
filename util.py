#!/usr/bin/python
#-*- coding: utf-8 -*-

#othello with monte carlo algorism

from boad import *
import math
import random

def other_color(color):
	if color == "white":
		return "black"
	elif color == "black":
		return "white"
	else:
		return None

def one_game(boad):
	boads = list()
	boads.append(boad)
	for i in range(len(boad.blank)):
		now_boad = boads[-1]
		blank = now_boad.blank
		tmp_blank = list(blank)
		flg = True
		if now_boad.turn == "":
			break
		while flg:
			rnd = random.randint(0,len(tmp_blank)-1)
			row = tmp_blank[rnd] / 8
			col = tmp_blank[rnd] % 8
			color = now_boad.turn
			masu = now_boad.boad[row][col]
			if now_boad.chk_puttable(masu,color):
				next_boad = now_boad.put(row,col)
				boads.append(next_boad)
				flg = False
			else:
				tmp_blank.pop(rnd)
				if len(tmp_blank) == 0:
					flg = False
					now_boad.turn = ""
	return boads
