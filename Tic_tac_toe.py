import os
import time
import getch
import random
import copy

##Class for tictac
class tictac:
	
	def __init__(self):
		self.list=['1','2','3','4','5','6','7','8','9']
		self.row1=[0,1,2]
		self.row2=[3,4,5]
		self.row3=[6,7,8]
		self.dia1=[0,4,8]
		self.dia2=[2,4,6]
		self.col1=[0,3,6]
		self.col2=[1,4,7]
		self.col3=[2,5,8]
	
	def row_match(self):				##matches row
		if self.list[0]==self.list[1]==self.list[2] or self.list[3]==self.list[4]==self.list[5] or self.list[6]==self.list[7]==self.list[8]:
			return True
		else:
			return False		

	def column_match(self):     		##matches column
		if self.list[0]==self.list[3]==self.list[6] or self.list[1]==self.list[4]==self.list[7] or self.list[2]==self.list[5]==self.list[8]:
			return True
		else:
			return False			

	def cross_match(self):            ##matches diagonal
		if self.list[0]==self.list[4]==self.list[8] or self.list[2]==self.list[4]==self.list[6]:
			return True
		else:
			return False
##Game over!!
	def won(self):			
		if self.row_match() or self.column_match() or self.cross_match():
			return True
		else:
			return False
	def game_over(self):
		x=0
		for i in self.list:
			if i=='X' or i=='O':
				x+=1
		if x==9:
			return True
		else:
			return False

##Printing tic tac
def printing(list):
	print(f"  {list[0]}  |  {list[1]}  |  {list[2]} \n________________\n  {list[3]}  |  {list[4]}  |  {list[5]} \n________________\n  {list[6]}  |  {list[7]}  |  {list[8]} ")

##Robot algoritm
def robot(list,turn):
	bool=True
	print("==================\nRobot's turn...\n==================\n")
	printing(list.list)
	if turn==1:
		i=int(random.choice(['0','2','4','6','8']))
		list.list[i]='O'
		time.sleep(0.5 )
		return 3
	#win situation
	(aa,bb,cc,dd,ee,xx,yy,zz,o_pos)=counter('O',list)
	(a,b,c,d,e,x,y,z,x_pos)=counter('X',list)
	pos=o_pos+x_pos
	for i in list.list:
		if indexing(0,1,2,aa,'O',list):
			bool=False
			break
		if indexing(3,4,5,bb,'O',list):
			bool=False
			break
		if indexing(6,7,8,cc,'O',list):
			bool=False
			break
		if indexing(0,4,8,dd,'O',list):
			bool=False
			break
		if indexing(2,4,6,ee,'O',list):
			bool=False
			break
		if indexing(0,3,6,xx,'O',list):
			bool=False
			break
		if indexing(1,4,7,yy,'O',list):
			bool=False
			break
		if indexing(2,5,8,zz,'O',list):
			bool=False
			break
#protect	
		if indexing(0,1,2,a,'X',list):    
			bool=False
			break
		if indexing(3,4,5,b,'X',list):
			bool=False
			break
		if indexing(6,7,8,c,'X',list):
			bool=False
			break
		if indexing(0,4,8,d,'X',list):
			bool=False
			break
		if indexing(2,4,6,e,'X',list):
			bool=False
			break
		if indexing(0,3,6,x,'X',list):
			bool=False
			break
		if indexing(1,4,7,y,'X',list):
			bool=False
			break
		if indexing(2,5,8,z,'X',list):
			bool=False
			break
	if bool:
		list.list[int(simulate(pos,list))]='O'
	os.system('clear')
	printing(tic.list)


##Count for 'O' and 'X'
def counter(char,list):
	count=a=b=c=d=e=x=y=z=0
	position=[]
	for i in list.list:
		if i==char:
			position.append(count)
			if count in list.row1:
				a+=1
			if count in list.row2:
				b+=1
			if count in list.row3:
				c+=1
			if count in list.dia1:
				d+=1
			if count in list.dia2:
				e+=1
			if count in list.col1:
				x+=1
			if count in list.col2:
				y+=1
			if count in list.col3:
				z+=1
		count+=1
	return a,b,c,d,e,x,y,z,position

##Setting index of 'O'
def indexing(i1,i2,i3,a,check,list):
	if a==2:
		for i in [i1,i2,i3]:
			if list.list[i]!=check and list.list[i] in ['1','2','3','4','5','6','7','8','9']:
				list.list[i]='O'
				return True
		return False
	else:
		return False

#simulates game
def simulate(pos,list):
	lis=['0','1','2','3','4','5','6','7','8']
	win=[]
	l_win=[]
	for i in pos:
		lis.remove(str(i))
	predict=[]
	for p in permutation(lis):
		predict.append(p)
	for q in predict:
		if pred(q,list):
			win.append(q)
	if len(win)==0:
		win=permutation(lis)
	if len(win)>1:
		win=random.choice(win)
		return win[0]
	return win[0][0]

##Check if prediction wins
def pred(q,list):
	i=0
	cop=copy.copy(list.list)
	p=copy.copy(q)
	for i in range(0,len(q),2):
		cop[int(q[i])]='O'
		p.remove(q[i])
	for a in p:
		cop[int(a)]='X'
	if cop[0]==cop[1]==cop[2] or cop[3]==cop[4]==cop[5] or cop[6]==cop[7]==cop[8] or cop[0]==cop[3]==cop[6] or cop==cop[4]==cop[7] or cop[2]==cop[5]==cop[8] or cop[0]==cop[4]==cop[8] or cop[2]==cop[4]==cop[6]:
		return True
	else:
		return False
			
##Give all combinations
def permutation(list):
	if len(list)==0:
		return []
	if len(list)==1:
		return [list]
	l=[]
	for i in range(len(list)):
		m=list[i]
		remlist=list[:i]+list[i+1:]
		for p in permutation(remlist):
			l.append([m]+p)
	return l

##Player function
def player(tic):
	print("=============\nYour turn...\n=============\n")
	printing(tic.list)
#	a='1'
	a=input("\nGive the position(1-9) for your sign : ")
	if a not in list('123456789'):
		print("\n!!!!Please enter between 1 to 9!!!!")
		time.sleep(0.8)
		return True
	a=int(a)
	tic.list[a-1]="X"
	os.system('clear')
	printing(tic.list)

##check if game is over
def over(tic,a):
	if a==0:
		c="Player"
	elif a==1:
		c="Robot"
	if tic.game_over() or tic.won():
		if tic.won():
			print(f"{c} won")
		else:
			print("Match tied")
		return True
			
############ Main Function ###########

tic=tictac()
#turn=1
turn=random.randint(0,1)			#if 0 1st turn is player's and if 1 1st turn will be robot's
if turn==0:
	while 1:
		os.system('clear')
		if(player(tic)):
			continue
		a=0
		if over(tic,a):
			break
		os.system('clear')
		robot(tic,turn)
		a=1
		if over(tic,a):
			break
		time.sleep(0.5)
else:
	while 1:
		os.system('clear')
		turn=robot(tic,turn)
		a=1
		if over(tic,a):
			break
		time.sleep(0.5)
		os.system('clear')
		if(player(tic)):
			continue
		a=0
		if over(tic,a):
			break
