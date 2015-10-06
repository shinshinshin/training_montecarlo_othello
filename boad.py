#!/usr/bin/python
#-*- coding: utf-8 -*-

#othello with monte carlo algorism

from util import *
from masu import Masu

class Boad:
	def __init__(self,base = None):
		self.boad = [None] * 8
		if base is None:
			for i in range(8):
				self.boad[i] = [None] * 8
				for j in range(8):
					self.boad[i][j] = Masu(i,j)
			self.boad[3][3].state = self.boad[4][4].state = "black"
			self.boad[4][3].state = self.boad[3][4].state = "white"
			self.blank = range(64)
			self.blank.remove(3*8+3)
			self.blank.remove(3*8+4)
			self.blank.remove(4*8+3)
			self.blank.remove(4*8+4)
		else:
			for i in range(8):
				self.boad[i] = [None] * 8
				for j in range(8):
					self.boad[i][j] = Masu(i,j,base.boad[i][j].state)

		self.all_masu = reduce(lambda a,b: a+b, self.boad)
		self.set_turn(base)

	def select_next(self):
		try_num = 1000
		candidate = list()
		for masu in self.all_masu:
			if masu.chk_puttable(masu,other_color(self.turn)):
				candidate.append(masu)

	def game_result(self):
		black_num = len(filter(lambda masu: masu.state == "black",self.all_masu))
		white_num = len(filter(lambda masu: masu.state == "white",self.all_masu))
		if black_num > white_num:
			return "black"
		elif black_num == white_num:
			return "draw"
		else:
			return "white"
	
	def set_turn(self,base):
		if base is None:
			self.turn = "black"
		else:
			turn = other_color(base.turn)
			if turn == "black":
				if self.blackable():
					self.turn = "black"
				elif self.whitable():
					self.turn = "white"
				else:
					self.turn = ""
			if turn == "white":
				if self.whitable():
					self.turn = "white"
				elif self.blackable():
					self.turn = "black"
				else:
					self.turn = ""

	def blackable(self):
		for masu in self.all_masu:
			if self.chk_puttable(masu,"black"):
				return True
		return False

	def whitable(self):
		for masu in self.all_masu:
			if self.chk_puttable(masu,"white"):
				return True
		return False

	def chk_puttable(self,masu,color):
		if masu.state != "":
			return False
		masu.set_direc()
		for direc in masu.direc:
			first_masu = self.get_nth_direc(masu,direc,1)
			if first_masu.state == other_color(color):
				for i in range(2,8):
					nth_masu = self.get_nth_direc(masu,direc,i)
					if nth_masu is None:
						break
					if nth_masu.state == "":
						break
					if nth_masu.state == color:
						return True
		return False

	def reverse(self,next_boad,masu):
		masu.set_direc()
		flg = False
		for direc in masu.direc:
			first_masu = self.get_nth_direc(masu,direc,1)
			n = 0
			if first_masu.state == other_color(masu.state):
				for i in range(2,8):
				 nth_masu = self.get_nth_direc(masu,direc,i)
				 if nth_masu is None:
					 break
				 if nth_masu.state == "":
					 break
				 if nth_masu.state == masu.state:
					 n = i
					 break
			if n > 0:
				flg = True
				for i in range (n):
					nth_masu = next_boad.get_nth_direc(masu,direc,i)
					nth_masu.state = masu.state
		if flg:
			return next_boad
		else:
			return None
	
	def get_nth_direc(self,masu,direc,n):
		row = masu.row + direc[0] * n
		col = masu.col + direc[1] * n
		if 0 <= row <= 7:
			if 0 <= col <= 7:
				return self.boad[row][col]
		return None

	def put(self,row,col):
		next_boad = Boad(self)
		piece = Masu(row,col,self.turn)
		next_boad = self.reverse(next_boad,piece)
		next_boad.blank = list(self.blank)
		next_boad.blank.remove(row*8+col)
		return next_boad

	def print_boad(self):
		for row in range(8):
			row_str = ""
			for col in range(8):
				masu = self.boad[row][col]
				if masu.state== "black":
					row_str += "b"
				elif masu.state== "white":
					row_str += "w"
				else:
					row_str += "-"
			print(row_str)
