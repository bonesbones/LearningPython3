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


"""move(n, a, b, c)这个函数不要理解为ABC三个柱子。
请这样理解，move函数，用来完成这么一个任务：

把n个盘子，从“源柱”通过“过渡柱”移动到“目标柱”上。
即move(n, source, bridge, destination)

为了完成这个任务，需要将此母任务分解为三个子任务：
1.把“源柱”上面的n-1个盘，移动到“过渡柱”
2.把“源柱”最下面的第n个盘移动到“目标柱”
3.把第一步中的n-1个盘从“过渡柱”移动到“目标柱”，任务完成。

第一步中“移动n-1个盘”子任务和“移动n个盘”母任务仅仅是目的柱的位置不一样。
子任务中源盘和母任务一样，过渡盘是母任务的目的盘，目的盘是母任务的过渡盘。所以调用函数应该是这样

# 把n-1个盘，从source通过destination移动到bridge
move(n-1, source, destination, bridge)
同理，第三步的函数应该是

# 把n-1个盘，从bridge通过source移动到destination
move(n-1, bridge, source，destination)
于是，三个步骤转换成程序就是

move(n-1, source, destination, bridge)
print (source,'-->', destination)
move(n-1, bridge, source， destination)
当只有一个盘的时候，直接移动，不存在子任务

if n == 1:
    print (source,'-->', destination)
最开始，源柱，过渡柱和目的柱，分别叫做A,B,和C。
所以move调用入口应该是：move(n, 'A', 'B', 'C')

这下好明白了吧。"""


