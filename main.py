import os, sys
import readchar
from random import *

def auto_gen(mat):
	if str(0) not in str(mat):
		for i in range(4):
			for j in range(3):
				if mat[i][j] == mat[i][j+1]:
					return
		for j in range(4):
			for i in range(3):
				if mat[i][j] == mat[i+1][j]:
					return
		print("GAME OVER!!")
		f = open("High_Score.txt","w")
		f.write(str(hi_sc))
		f.close()
		sys.exit()
	
	if str(2048) in str(mat):
		print("YOU WIN!!")

	while(1):
		i = randint(0,3)
		j = randint(0,3)

		if mat[i][j] == 0:
			mat[i][j] = 2
			break

def swipe_left(mat,sc):
	for i in range(4):
		k = 3
		while(k != 1):
			for j in range(k):
				if mat[i][j] == 0:
					mat[i][j], mat[i][j+1] = mat[i][j+1], mat[i][j]
			k = k - 1
		for j in range(3):
			if mat[i][j] == mat[i][j+1] and mat[i][j+1] != 0:
				mat[i][j] += mat[i][j]
				mat[i][j+1] = 0
				sc = sc + mat[i][j]
		k = 3
		while(k != 1):
			for j in range(k):
				if mat[i][j] == 0:
					mat[i][j], mat[i][j+1] = mat[i][j+1], mat[i][j]
			k = k - 1
	return sc

def swipe_right(mat,sc):
	for i in range(4):
		k = 3
		while(k != 1):
			j = k
			while j > 0:
				if mat[i][j] == 0:
					mat[i][j], mat[i][j-1] = mat[i][j-1], mat[i][j]
				j = j - 1
			k = k - 1
		for j in reversed(range(4)):
			if j > 0 and mat[i][j] == mat[i][j-1] and mat[i][j-1] != 0:
				mat[i][j] += mat[i][j]
				mat[i][j-1] = 0
				sc = sc + mat[i][j]
		k = 3
		while(k != 1):
			j = k
			while j > 0:
				if mat[i][j] == 0:
					mat[i][j], mat[i][j-1] = mat[i][j-1], mat[i][j]
				j = j - 1
			k = k - 1
	return sc

def swipe_down(mat,sc):
	for j in range(4):
		k = 3
		while(k != 1):
			i = k
			while i > 0:
				if mat[i][j] == 0:
					mat[i][j], mat[i-1][j] = mat[i-1][j], mat[i][j]
				i = i - 1
			k = k - 1
		for i in reversed(range(4)):
			if i > 0 and mat[i][j] == mat[i-1][j] and mat[i-1][j] != 0:
				mat[i][j] += mat[i][j]
				mat[i-1][j] = 0
				sc = sc + mat[i][j]
		k = 3
		while(k != 1):
			i = k
			while i > 0:
				if mat[i][j] == 0:
					mat[i][j], mat[i-1][j] = mat[i-1][j], mat[i][j]
				i = i - 1
			k = k - 1
	return sc

def swipe_up(mat,sc):
	for j in range(4):
		k = 3
		while(k != 1):
			for i in range(k):
				if mat[i][j] == 0:
					mat[i][j], mat[i+1][j] = mat[i+1][j], mat[i][j]
			k = k - 1
		for i in reversed(range(4)):
			if i > 0 and mat[i][j] == mat[i-1][j] and mat[i-1][j] != 0:
				mat[i][j] += mat[i][j]
				mat[i-1][j] = 0
				sc = sc + mat[i][j]
		k = 3
		while(k != 1):
			for i in range(k):
				if mat[i][j] == 0:
					mat[i][j], mat[i+1][j] = mat[i+1][j], mat[i][j]
			k = k - 1
	return sc

def printmat(mat):
	for i in range(4):
		rows = "|\t"
		for j in range(4):
			if mat[i][j] == 0:
				rows = rows + " |\t"
			else:
				rows = rows + str(mat[i][j]) + "|\t"
		print(rows)

matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
flag = 1
score = 0

f = open("High_Score.txt","r")
hi_sc = int(f.readline())
f.close()

auto_gen(matrix)

while(1):
	print("Press the arrow keys to swipe:")
	printmat(matrix)
		
	swipe = readchar.readkey()
	
	if swipe == readchar.key.LEFT:
		score = swipe_left(matrix,score)
		print("You pressed LEFT")
	elif swipe == readchar.key.UP:
		score = swipe_up(matrix,score)
		print("You pressed UP")
	elif swipe == readchar.key.RIGHT:
		score = swipe_right(matrix,score)
		print("You pressed RIGHT")
	elif swipe == readchar.key.DOWN:
		score = swipe_down(matrix,score)
		print("You pressed DOWN")
	else:
		print("Not an arrow key")

	if score > hi_sc:
		hi_sc = score

	auto_gen(matrix)
	print("Your Score: " + str(score) + "\tHigh Score: " + str(hi_sc))
	print("--------------------------------------")
