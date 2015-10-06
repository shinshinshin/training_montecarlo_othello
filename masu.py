#!/usr/bin/python
#-*- coding: utf-8 -*-

#othello with monte carlo algorism

class Masu:
	def __init__(self, row, col, state = ""):
		self.row = row
		self.col = col
		self.state = state
		self.point = 0

	#direction for a masu
	def set_direc(self):
		all_direc = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
		self.direc = all_direc
		if self.row == 0:
			self.direc = filter(lambda elem: elem[0] != -1, self.direc)
		elif self.row == 7:
			self.direc = filter(lambda elem: elem[0] != 1, self.direc)

		if self.col == 0:
			self.direc = filter(lambda elem: elem[1] != -1, self.direc)
		elif self.col == 7:
			self.direc = filter(lambda elem: elem[1] != 1, self.direc)



