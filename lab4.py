#### PPT 예제 코딩
#### Lab 코딩
#### Lab 4-1
'''
import numpy as np

def add (a, b):
	return a + b

def solution(num_len):
	arr = np.random.randint(0,101, size = num_len)
	#arr = [2,1,3,4,1]
	#arr = [5,0,2,7]
	print(arr)
	arr = arr.tolist()
	ans_b = []
	ans_a = []

	if len(arr) < 2 or len(arr) > 100:
		print("numbers의 길이는 2 이상 100 이하여야 합니다.")
	elif max(arr) > 100 or min(arr) < 0:
		print("numbers의 모든 수는 0 이상 100 이하여야 합니다.")
	else:
		for num1 in range(len(arr)):
			for num2 in range(len(arr)):
				if num1 == num2:
					continue
				ans_b.append(add(arr[num1], arr[num2]))
		ans_b = list(set(ans_b))
		while len(ans_b) > 0:
			min_val = min(ans_b)
			ans_a.append(min_val)
			ans_b.remove(min_val)
			
		print(ans_a)

num_len = int(input())
solution(num_len)
'''
#### Lab 4-2
'''
import random

def check_str1(str1):
	for i in str1:
		if not (i >= 'a' and i <= 'z'):
			return 0
	return 1

def how_much_rep(str1, char1):
	count = 0
	ans = []
	for i in range(len(str1)):
		if str1[i] == char1:
			count += 1
			if i == len(str1) - 1:
				ans.append(count)
		else:
			ans.append(count)
			count = 0
		
	return max(ans)

def solution():
	alpa = "abcdefghijklmnopqrstuvwxyz"
	ans = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	str1 = []
	max = 0
	index = -1
#	for i in range(random.randint(1, 101)):
#		str1.append(alpa[random.randint(0, 25)])
#	str1 = "aaabbcddddee"
#	str1 = "banana"
#	str1 = "mississippi"
#	str1 = "aabbbcccc"
	str1 = "Abvsd"
	if check_str1(str1) == 0:
		print("입력 문자열은 소문자 알파벳만 포함해야 합니다.")
		return
	for i in range(len(alpa)):
		ans[i] = how_much_rep(str1, alpa[i])
	print(str1)
	for i in range(len(ans)):
		if ans[i] > max:
			max = ans[i]
			index = i
	print("(\"%s\", %d)" %(alpa[index], ans[index]))

solution()
'''
####Lab 4-3
'''
import numpy as np
def check_multiply(arr1, arr2):
	return arr1.shape[1] == arr2.shape[0]
def check_num(arr1, arr2):
	bool1 = np.all(arr1 >= -10) and np.all(arr1 <= 20)
	bool2 = np.all(arr2 >= -10) and np.all(arr2 <= 20)
	return bool1 and bool2
def check_size(arr1, arr2):
	bool1 = (arr1.shape[0] >= 2 and arr1.shape[0] <= 100) and (arr1.shape[1] >= 2 and arr1.shape[1] <= 100)
	bool2 = (arr2.shape[0] >= 2 and arr2.shape[0] <= 100) and (arr2.shape[1] >= 2 and arr2.shape[1] <= 100)
	return bool1 and bool2
def solution(arr1, arr2):
	if (check_multiply(arr1, arr2) == False):
		print("행렬의 곱셈이 불가능합니다.")
		return
	if (check_num(arr1, arr2) == False):
		print("행렬의 원소는 -10 이상 20 이하의 자연수여야 합니다.")
		return
	if (check_size(arr1, arr2) == False):
		print("행렬의 크기는 최소 2x2 이상이어야 합니다.")
		return
	print(arr1 @ arr2 )

#arr1 = np.random.randint(-10, 21, size = (np.random.randint(2, 101), np.random.randint(2, 101)))
#arr2 = np.random.randint(-10, 21, size = (np.random.randint(2, 101), np.random.randint(2, 101)))

#arr1 = np.array([[1,4], [3,2], [4,1]])
#arr2 = np.array([[3,3], [3,3]])

arr1 = np.array([[2,3,2],[4,2,4],[3,1,4]])
arr2 = np.array([[5,4,3],[2,4,1],[3,1,1]])

#print(check_multiply(arr1,arr2))
#print(check_num(arr1, arr2))
#print(check_size(arr1,arr2))
solution(arr1, arr2)
'''
#### Lab 4-4
'''
def solution(rsp):
	rsp_dict = {'0' : 5, '2' : 0, '5' : 2}
	rsp_list = list(rsp)
	print("\"",end = '')
	for i in rsp_list:
		print(rsp_dict[i], end = '')
	print("\"", end = '')
rsp = input()
solution(rsp)
'''