#### PPT 예제 코딩
#### Lab 코딩

#### PPT 예제 코딩
#### slide 4

#### slide 11


#### Lab 코딩
#### Lab 3-1
'''
class Note(object):
	def __init__(self, contents = None):
		self.contents = contents

	def write_contents(self, contents):
		self.contents = contents

	def remove_all(self):
		self.contents = " "

	def __str__(self):
		return self.contents

class NoteBook(object):
	def __init__(self, title):
		self.title = title
		self.page_number = 1
		self.notes = {}

	def add_note(self, note, page = 0):
		if (self.page_number < 300):
			if (page == 0):
				self.notes[self.page_number] = note
				self.page_number += 1
			else:
				self.notes[page] = note
				self.page_number += 1
		else:
			print("the page is filled")

	def remove_note(self, page_number):
		if (page_number in self.notes.keys()):
			return self.notes.pop(page_number)
		else:
			print("The page does not exist.")

	def get_number_of_pages(self):
		return len(self.notes)

# lab - print_note()만들기
	def print_note(self, page_number):
		if (page_number in self.notes.keys()):
			print(self.notes[page_number])
		else:
			print("해당 페이지는 존재하지 않습니다")

#lab - get_number_of_page_characters() 만들기
	def get_number_of_page_characters(self, page_number):
		if (page_number in self.notes.keys()):
			print(len(str(self.notes[page_number])))
		else:
			print("해당 페이지는 존재하지 않는다")
#lab - get_number_of_all_characters() 만들기
	def get_number_of_all_characters(self):
		len_of_notebook = 0
		for text in self.notes.values():
			len_of_notebook += len(str(text))
		print("All characters are %d" %len_of_notebook)

note1 = Note("명언 모음집")
note2 = Note("as long as there is life,there is hope.-Kikero")
note3 = Note("외강내유 - 겉으로 강의를 보고 속으로 유튜브를 본다 -승헌-")
note4 = Note("참을 인 3번면 호구 -동주-")
note5 = Note("Chatgpt 돌리면 다 나와 -옆자리 2022315062 김희준-")
note6 = Note("ADD Test ADD Test ADD Test")

wise_saying_notebook = NoteBook("wise saying notebook")

wise_saying_notebook.add_note(note1)
wise_saying_notebook.add_note(note2)
wise_saying_notebook.add_note(note3)
wise_saying_notebook.add_note(note4)
wise_saying_notebook.add_note(note5)
wise_saying_notebook.add_note(note6)

#print_note출력화긴
wise_saying_notebook.print_note(5)
# 5페이지 지우고 확인 (없을때 출력) 
wise_saying_notebook.remove_note(5)
wise_saying_notebook.print_note(5)
#왜 get_number_of_page만 print를 따로 해야하는가? -- ppt는 다름
print(wise_saying_notebook.get_number_of_pages())

#get_number_of_page_characters 페이지가 존재할 때
wise_saying_notebook.get_number_of_page_characters(6)
#get_number_of_page_charactors 페이지가 존재하지 않을 때
wise_saying_notebook.get_number_of_page_characters(7)

#get_number_of_all_characters()
wise_saying_notebook.get_number_of_all_characters()
'''
#### Lab 3 - 2
'''
class Transcript(object):
	def __init__(self, korean, english, math):
		self.transcript = {
				"korean" : korean ,
				"english" : english ,
				"math" : math
		}
# Lab 3-2  - write() 만들기
	def write(self, korean, english, math):
		self.transcript["korean"] = korean
		self.transcript["english"] = english
		self.transcript["math"] = math
# Lab 3-2 - reset() 만들기
	def reset(self):
		self.transcript["korean"] = 0
		self.transcript["english"] = 0
		self.transcript["math"] = 0

	def __str__(self):
		return str(self.transcript)

class TranscriptBook(object):
	def __init__(self, transcript_max : int = 30):
		self.transcript_dict = {}
		self.transcript_num = 0
		self.transcript_max = transcript_max
#Lab 3-2 add_transcipt() 만들기
	def add_transcript(self, student_id, transcript, grade = 1, class_num = 1):
		if (self.transcript_num < 30):
			if isinstance(transcript, Transcript): #transcipt가 Transcript의 형식인지 확인하는 함수 
				self.transcript_dict[student_id] = {"transcript" : transcript, "grade" :  grade, "class_num" : class_num}
				self.transcript_num += 1
		else:
			print("30명 넘었슈")

#Lab 3-2 reverse_transcript() 만들기
	def reverse_transcipt(self, student_id, korean, english, math):
		if (student_id in self.transcript_dict.keys()):
			self.transcript_dict[student_id]["transcript"].write(korean, english, math)
		else:
			print("student id : %d does not exist" %student_id)

#Lab 3-2 delete_transcript() 만들기
	def delete_transcript(self,student_id):
		if (student_id in self.transcript_dict.keys()):
			self.transcript_dict.pop(student_id) #안에 transcript따로 지워줘야하는가?
			self.transcript_num -= 1
			print("Transcript of student id %d is deleted" % student_id)
		else:
			print("student id : %d does not exist." %student_id)

#Lab 3-2 get_transcript() 만들기
	def get_transcript(self, student_id):
		if (student_id in self.transcript_dict.keys()):
			print("student_id : %d" %student_id)
			print("grade : %d" %self.transcript_dict[student_id]["grade"])
			print("classnum : %d" %self.transcript_dict[student_id]["class_num"])
			print("score : " + str(self.transcript_dict[student_id]["transcript"]))
		else:
			print("student_id %d does not exist" %student_id)

#Lab 3-2 get_transcript_num() 만들기
	def get_transcript_num(self):
		print("transcript_num: %d" %self.transcript_num)
#Lab 3-2 show_all() 만들기
	def show_all(self):
		print("Show all transcript ! \n==================================================")
		for id in self.transcript_dict.keys():
			self.get_transcript(id)
			print("==================================================")

#student1 = Transcript(0, 0, 0)
#student1.write(30, 50, 60)
#student1.reset()
#print(student1.transcript.items())
#print(student1)

book = TranscriptBook()
book.add_transcript(
	student_id = 1,
	transcript = Transcript(korean = 10 , english = 20, math = 30),
	grade = 1,
	class_num = 1
)
book.add_transcript(
	student_id = 2,
	transcript = Transcript(korean = 100, english = 100, math = 100),
	grade = 1,
	class_num = 1
)
book.add_transcript(
	student_id = 2022310834,
	transcript = Transcript(korean = 60, english = 89, math = 100),
	grade = 3,
	class_num = 53
)
book.reverse_transcipt(
	student_id = 1,
	korean = 100,
	english = 90,
	math = 70
)
#print(book.transcript_dict)
#book.delete_transcript(1)
#print(book.transcript_dict)

#book.get_transcript(student_id = 1)
#book.get_transcript(student_id = 2)

#book.get_transcript_num()
book.show_all()
'''
#Lab 3-3
'''
class YearMonth:
	def __init__(self, year, month):
		self.year = year
		self.month = month
		self.days_in_month = self.calculate_days_in_month()

#Lab 3-3 calculate_days_in_month() 만들기
	def calculate_days_in_month(self):
		month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		return int(month_list[self.month - 1] + (self.is_leap_year(self.year)) * (self.month % 12 == 2) )

#Lab 3-3 is_leap_year() 만들기
	def is_leap_year(self, year):
		return ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)

#Lab 3-3 day_of_week() 만들기
	def day_of_week(self, year, month, day):
		if month <= 2:
			month += 12
			year -= 1
		K = year % 100
		J = year // 100
		return int((day + (13 * (month + 1)) // 5 + K + (K//4) + (J//4) + 5*J) % 7)

# Lab 3-3 display() 만들기
	def display(self):
		day_list = [["  "] * 7 for _ in range(5)]              # 0으로 초기화된 5X7 2차 list
		print("Year: %d, Month: %d" %(self.year, self.month))
		print("Su Mo Tu We Th Fr Sa")
		week = 0
		for i in range(1, self.days_in_month + 1):
			new_index = (self.day_of_week(self.year, self.month, i) + 6) % 7
			day_list[week][new_index] = str(i)
			if new_index == 6:
				week += 1
		for i in range(5):
			for j in range(7):
				if len(day_list[i][j]) == 1:
					print(" " + day_list[i][j] + " ", end = "\n" if j == 6 else "")
				else:
					print(day_list[i][j] + " ", end = "\n" if j == 6 else "")


#사용자오부터 년과 월을 입력받기
year = int(input("Enter year: "))
month = int(input("Enter month: "))

#YearMonth 객체 생성
ym = YearMonth(year, month)

#연과 월 출력
ym.display()
#print(ym.is_leap_year(year))
#print(ym.calculate_days_in_month())
#print(ym.days_in_month)
#print(ym.day_of_week(year, month, 1))
'''

















	