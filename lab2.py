#### PPT 예제 코딩
#### Lab 코딩

#### PPT 예제 코딩
#### slide 4
'''
professor = "Chulsoo Kim"
print(professor)
a = 7
b = 5
print(a + b)
a = 7
b = 5
print("a + b")
'''
#### slide 11
'''
a = 1
b = 1
print(a ,b)

a = 1.5
b = 1.5
print(a, b)

a = "ABC"
b = "101010"
print(a, b)

a = True
b = False
print(a, b)
'''
#### Lab 코딩

#### Lab 1 - 1
'''
def check_word(str1, str2, index):
	for i in range(len(str2)):
		if (str2[i] != str1[index + i]):
			return 0
	return 1

str1 = input()
str2 = input()
result = []

for i in range(len(str1)):
	if (check_word(str1, str2, i) == 1):
		result.append(i + 1)
if (len(result) == 0):
	print(-1)
else:
	print(result)
'''

### Lab 1-2
'''
def del_or_not(str1 , str2):
	if((str1 == "NORTH" and str2 == "SOUTH") or (str1 == "SOUTH" and str2 == "NORTH") or (str1 == "EAST" and str2 == "WEST") or (str1 == "WEST" and str2 == "EAST")):
		return 1
	else:
		return 0


str = input()
split_list = str[1 : len(str) - 1].split(', ')
for i in range(len(split_list)):
	split_list[i] = split_list[i][1:len(split_list[i]) - 1]
list = split_list
i = 0
while (i < len(list) - 1 and len(list) > 1):
	if(del_or_not(list[i], list[i + 1]) == 1):
		del list[i : i + 2]
		i = 0
	else:
		i += 1
print(list)
'''

### Lab 1-3
'''
arr = [0,-1,3,1,2]
arr = sorted(arr)

def find_num(arr, num):
	for i in arr:
		if (i == num):
			return 0
	return 1
			

for i in range(len(arr)):
	if(arr[i] > 0):
		if(find_num(arr, arr[i] + 1) == 1):
			print(arr[i] + 1)
			break
'''

### Lab 1-4
'''
line = int(input())
num = 0
for i in range(1, line + 1):
	for k in range(line - i):
		print(" ",end = '')
	num = i % 10 
	k = 0
	while(k < i):
		print((num + k) % 10, end = '')
		k += 1
	k -= 1
	while(k > 0):
		print((num + k - 1) % 10,end = '')
		k -= 1
	print("")
'''