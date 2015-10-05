#!/usr/bin/python
#-*- coding: utf-8 -*-

#othello with monte carlo algorism

def other_color(color):
	if color == "white":
		return "black"
	elif color == "black":
		return "white"
	else:
		return None

