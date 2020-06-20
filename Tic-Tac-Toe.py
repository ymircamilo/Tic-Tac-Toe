#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import os

mtx_aux = [["M","M","M"],["M","M","M"],["M","M","M"]]
mtx = np.array(mtx_aux)

def trikiPlay(x, y, piece):
	mtx[x,y] = piece

def printMatrix():
	for i in mtx:
		for j in i:
			print(F"{j} ", end="")
		print("")

def horizontalCheck():
	for i in mtx:
		if np.array_equal(["X", "X", "X"], i) or np.array_equal(["O", "O", "O"], i): return True
		else: return False

def verticalCheck():
	v_aux = ["","",""]
#	v_aux = np.array(v)
	for i in [0, 1, 2]:
		for j in [0, 1, 2]:
			v_aux[j] = mtx[j,i]
		print(v_aux)
#		if np.array_equal(["X", "X", "X"], v_aux) or np.array_equal(["O", "O", "O"], v_aux): return True
#		else: return False
		

def endGame():
	verticalCheck()
	if horizontalCheck() or verticalCheck():
		return True
	else: return False

#main
player1 = "X"
player2 = "O"
current_player = "X"
while True:
	print ("Please enter the X coordinate: ", end="")
	x_coor = int(input())
	print ("Please enter the Y coordinate: ", end="")
	y_coor = int(input())
#	print(F"X:{x_coor} and Y:{y_coor}")
	if 3 > x_coor > -1 and 3 > y_coor > -1:
		t = mtx[x_coor, y_coor]
		if t == "M":
			os.system('cls||clear')
			trikiPlay(x_coor, y_coor, current_player)
			printMatrix()
			if current_player == "X":
				current_player = "O"
			else:
				current_player = "X"
		else:
#			os.system('cls||clear')
			print("That's NOT a VALID POSITION, please TRY AGAIN!")	
	else:
		os.system('cls||clear')
		print("Coordinate OUT of range, please TRY AGAIN!")
	if (endGame()):
		print("Ganó")
		break
print("Terminó")

