#선형리스트 응용예제2-1

# l = [('다현',200),('정연',150),('쯔위',90),('사나',30),('지효',15)]
#
#
# name = input('추가할 친구 --> ')
# cnt = int(input('카톡 횟수 --> '))
#
# for i in range(len(l)):
#     if l[i][1] < cnt:
#         l.append(None)
#         for j in range(len(l)-1, i, -1):
#             l[j] = l[j-1]
#         l[i] = (name,cnt)
#         break
#
# print(l)


#선형리스트 응용예제2-2

# x = [[7,300], [-4,20], [5,0]]
#
#
# def print_x(x):
#     str = "P(x) = "
#
#     for i in range(len(x)):
#         term = x[i][1]
#         coef = x[i][0]
#
#         if (coef >= 0):
#             str += "+"
#         str = str + f'{coef}x^{term} '
#
#     return str
#
# def cal(n):
#     sum = 0
#     for i in range(len(x)):
#         term = x[i][1]
#         coef = x[i][0]
#
#         sum = sum + coef * n ** term
#     return sum
#
# print(print_x(x))
# print(cal(int(input('X 값 --> '))))


#단순 연결 리스트 응용예제3-1

# class Node:
#     def __init__(self):
#         self.link = None
#         self.data = None
#
# def print_node():
#     print(head.data, end = ' ')
#     current = head
#     while True:
#         if current.link == None:
#             return
#         current = current.link
#         print(current.data, end = ' ')
#
#
# name = input('이름 --> ')
# email = input('이메일 --> ')
#
# node = Node()
# node.data = [name,email]
# head = node
# print_node()
#
# while True:
#     print()
#     name = input('이름 --> ')
#     email = input('이메일 --> ')
#     node = Node()
#     node.data = [name, email]
#
#     if node.data[1] < head.data[1]:
#         node.link = head
#         head = node
#         print_node()
#         break
#
#     current = head
#     while True:
#         if current.link == None:
#             break
#         pre = current
#         current = current.link
#         if node.data[1] < current.data[1]:
#             pre.link = node
#             node.link = current
#             print_node()
#             break
#
#     current.link = node
#     print_node()

#단순 연결 리스트 응용예제3-2
# from random import randint
# class Node:
#     def __init__(self):
#         self.n = None
#         self.l = None
#
# number = []
#
# while len(number) < 6:
#     num = randint(1, 45)
#     if num in number:
#         continue
#     else:
#         number.append(num)
#
# for i in range(5):
#     for j in range(i+1,6):
#         if number[i] > number[j]:
#             number[i], number[j] = number[j], number[i]
#
#
# node = Node()
# head = node
# node.n = number[0]
# current = node
#
# for i in range(1,6):
#     node = Node()
#     node.n = number[i]
#     current.l = node
#
#     current = node
#
# current = head
# for i in range(6):
#     print(current.n, end = ' ')
#     current = current.l









#정렬기본 응용예제 11-1

# scoreAry = [['선미', 88], ['초아', 99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]
#
# def sort_ary():
#     for i in range(len(scoreAry)-1):
#         for j in range(i+1, len(scoreAry)):
#             if scoreAry[j][1] < scoreAry[i][1]:
#                 scoreAry[j][1], scoreAry[i][1] = scoreAry[i][1] , scoreAry[j][1]
#
# def parter():
#     for i in range(len(scoreAry)//2):
#         print(f'{scoreAry[i][0]} : {scoreAry[len(scoreAry)-1-i][0]}')
#
# sort_ary()
# parter()

#정렬기본 응용예제 11-2
# ary2 = [[55, 33, 250, 44],
# 		 [88,  1,  67, 23],
# 		 [199,222, 38, 47],
# 		 [155,145, 20, 99]]
# ary1 = []
#
# for i in range(4):
#     for j in range(4):
#         ary1.append(ary2[i][j])
#
# print(f'정렬 전 --> {ary1}')
#
# for i in range(16):
#     for j in range(i+1, 16):
#         if ary1[i] > ary1[j]:
#             ary1[i], ary1[j] = ary1[j], ary1[i]
#
#
# print(f'정렬 후 --> {ary1}')
#
# mid = ary1[16//2]
# print(f'중앙값 --> {mid}')




#동적 계획법 응용예제 14-2
# r_cnt = 0
# dp_cnt = 0
# def fibo(n):
#     global r_cnt
#     r_cnt += 1
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#
#     return fibo(n-1) + fibo(n-2)
#
#
#
#
# def dp_fibo(n):
#     l = [0, 1]
#     global  dp_cnt
#     dp_cnt = 0
#     for i in range(2,n+1):
#         l.append(None)
#         l[i] = l[i-1] + l[i-2]
#         dp_cnt +=1
#     return l[n]
#
#
# print(fibo(30))
# print(f'재귀 횟수 {r_cnt}')
# print(dp_fibo(30))
# print(f'동적 횟수 {dp_cnt}')
























