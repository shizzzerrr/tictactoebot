from os import system as clear
from time import sleep
import random 

wins = 0

def field(a,b,c,d,e,f,g,h,i):
	print(f'    1 | 2 | 3\n  -------------\na | {a} | {b} | {c} |\n  -------------\nb | {d} | {e} | {f} |\n  -------------\nc | {g} | {h} | {i} |\n  -------------\n')

def menu():
	global priority,a,b,c,d,e,f,g,h,i
	a,b,c,d,e,f,g,h,i = ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' '
	clear('cls')
	print('TicTacToe bot by shizzzerrr v1.0')
	input('Press "Enter" to start game :')

	if random.random() > 0.5:
		print('Bot has first turn.')
		priority = 1

	else:
		print('Player has first turn.')
		priority = 2

	sleep(3)

	clear('cls')

	game()

def rematch():
	global priority,a,b,c,d,e,f,g,h,i,wins
	a,b,c,d,e,f,g,h,i = ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' '
	clear('cls')
	print('TicTacToe bot by shizzzerrr v1.0')
	print(f'bot {wins}:0 player')
	print('Waiting 3 seconds...')
	sleep(3)
	if random.random() > 0.5:
		print('Bot has first turn.')
		priority = 1

	else:
		print('Player has first turn.')
		priority = 2

	clear('cls')

	game()		

def player_turn():
	global a,b,c,d,e,f,g,h,i
	turn = input('>>> ')
	if turn == 'a1' and a==' ':
		a = 'x'
	elif turn == 'a2' and b==' ':
		b = 'x'
	elif turn == 'a3' and c==' ':
		c = 'x'
	elif turn == 'b1' and d==' ':
		d = 'x'
	elif turn == 'b2' and e==' ':
		e = 'x'
	elif turn == 'b3' and f==' ':
		f = 'x'
	elif turn == 'c1' and g==' ':
		g = 'x'
	elif turn == 'c2' and h==' ':
		h = 'x'
	elif turn == 'c3' and i==' ':
		i = 'x'
	else:
		print('Incorrect coordinates.')
		player_turn()

def game():
	clear('cls')
	global priority,a,b,c,d,e,f,g,h,i,wins
	field(a,b,c,d,e,f,g,h,i)
	if a==b==c!=' ' or d==e==f!=' ' or g==h==i!=' ' or a==d==g!=' ' or b==e==h!=' ' or c==f==i!=' ' or a==e==i!=' ' or c==e==g!=' ':
		print('Bot wins.')
		wins+=1
		print('\nNew game? (y|n)')
		if input('>>> ') == 'y':
			rematch()
		else:
			clear('cls')
			exit()
	elif a!=' ' and b!=' ' and c!=' ' and d!=' ' and e!=' ' and f!=' ' and g!=' ' and h!=' ' and i!=' ':
		print('Draw.')
		print('\nNew game? (y|n)')
		if input('>>> ') == 'y':
			rematch()
		else:
			clear('cls')
			exit()
	else:
		if priority %2 == 0:
			print('Write coordinates of your turn. (examples : a1, b2, c1, a3.)')
			player_turn()
			priority += 1
			game()
		else:
			#ГОРИЗОНТАЛИ
			if a==b=='o' and c ==' ':
				c = 'o'
			elif a==c=='o' and b ==' ':
				b = 'o'
			elif b==c=='o' and a ==' ':
				a = 'o'

			elif d==e=='o' and f ==' ':
				f = 'o'
			elif e==f=='o' and d ==' ':
				d = 'o'
			elif d==f=='o' and e ==' ':
				e = 'o'

			elif g==h=='o' and i ==' ':
				i = 'o'
			elif h==i=='o' and g ==' ':
				g = 'o'
			elif g==i=='o' and h ==' ':
				h = 'o'
			#ВЕРТИКАЛИ 
			elif a==d=='o' and g ==' ':
				g = 'o'
			elif a==g=='o' and d ==' ':
				d = 'o'
			elif d==g=='o' and a ==' ':
				a = 'o'

			elif b==e=='o' and h ==' ':
				h = 'o'
			elif e==h=='o' and b ==' ':
				b = 'o'
			elif b==h=='o' and e ==' ':
				e = 'o'

			elif c==f=='o' and i ==' ':
				i = 'o'
			elif c==i=='o' and f ==' ':
				f = 'o'
			elif f==i=='o' and c ==' ':
				c = 'o'
			#ДИАГОНАЛИ 
			elif a==e=='o' and i ==' ':
				i = 'o'
			elif a==i=='o' and e ==' ':
				e = 'o'
			elif e==i=='o' and a ==' ':
				a = 'o'

			elif c==e=='o' and g ==' ':
				g = 'o'
			elif e==g=='o' and c ==' ':
				c = 'o'
			elif c==g=='o' and e ==' ':
				e = 'o'


			#ГОРИЗОНТАЛИ
			elif a==b=='x' and c ==' ':
				c = 'o'
			elif a==c=='x' and b ==' ':
				b = 'o'
			elif b==c=='x' and a ==' ':
				a = 'o'

			elif d==e=='x' and f ==' ':
				f = 'o'
			elif e==f=='x' and d ==' ':
				d = 'o'
			elif d==f=='x' and e ==' ':
				e = 'o'

			elif g==h=='x' and i ==' ':
				i = 'o'
			elif h==i=='x' and g ==' ':
				g = 'o'
			elif g==i=='x' and h ==' ':
				h = 'o'
			#ВЕРТИКАЛИ 
			elif a==d=='x' and g ==' ':
				g = 'o'
			elif a==g=='x' and d ==' ':
				d = 'o'
			elif d==g=='x' and a ==' ':
				a = 'o'

			elif b==e=='x' and h ==' ':
				h = 'o'
			elif e==h=='x' and b ==' ':
				b = 'o'
			elif b==h=='x' and e ==' ':
				e = 'o'

			elif c==f=='x' and i ==' ':
				i = 'o'
			elif c==i=='x' and f ==' ':
				f = 'o'
			elif f==i=='x' and c ==' ':
				c = 'o'
			#ДИАГОНАЛИ 
			elif a==e=='x' and i ==' ':
				i = 'o'
			elif a==i=='x' and e ==' ':
				e = 'o'
			elif e==i=='x' and a ==' ':
				a = 'o'

			elif c==e=='x' and g ==' ':
				g = 'o'
			elif e==g=='x' and c ==' ':
				c = 'o'
			elif c==g=='x' and e ==' ':
				e = 'o'

			else:
				if (a=='x' or c=='x' or g=='x' or i=='x') and e== ' ':
					e = 'o'
				elif a == ' ' and d==b==' ':
					a = 'o'
				elif c == ' ' and b==f==' ':
					c = 'o'
				elif g == ' ' and d==h==' ':
					g = 'o'
				elif i == ' ' and h==f==' ':
					i = 'o'
				elif a==' ':
					a= 'o'
				elif b==' ':
					b= 'o'
				elif c==' ':
					c= 'o'
				elif d==' ':
					d= 'o'
				elif e==' ':
					e= 'o'
				elif f==' ':
					f= 'o'
				elif g==' ':
					g= 'o'
				elif h==' ':
					h= 'o'
				elif i==' ':
					i= 'o'
			priority +=1
			game()

menu()
