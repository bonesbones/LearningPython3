# _*_ coding:utf-8 _*_

def move (n,a,b,c):
#	if n < 3:
#		print ('error please make sure n >= 3')
#	else:


#本程序用于实现『汉诺塔』游戏，规则是上方的盘子必须小于下方的盘子。

	if n == 1:
		print ('move',a,'to',c)
		return
	move (n-1,a,c,b)
	print('move',a,'to',c)
	move(n-1,b,a,c)


move (4,'A','B','C')
