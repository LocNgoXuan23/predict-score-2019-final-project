# read file 
with open("test.txt", encoding="utf8") as file:
	data = file.read().split("\n")

header = data[0]
students = data[1:]


header = header.split(",")
subjects = header[5:]

for i in range(len(students)):
	students[i] = students[i].split(",")

students.pop()
total_student = len(students)

not_take_exam = [0,0,0,0,0,0,0,0,0,0,0]

for i in range(len(students)):
# for i in range(2):
	for j in range(len(subjects)):
		if students[i][j+4] == "-1":
			not_take_exam[j] += 1


not_take_exam_percentage = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(subjects)):
	not_take_exam_percentage[i] = round(not_take_exam[i]*100/total_student, 2)


#plot barchart
import matplotlib.pyplot as plt
import numpy

figure, axis = plt.subplots()

y_pos = numpy.arange(len(subjects))

plt.bar(y_pos, not_take_exam_percentage)
plt.xticks(y_pos, subjects)

axis.set_ylim(0,100)

plt.ylabel('Percentage')
plt.title('số học sinh bỏ thi hoặc không đăng kí')

rects = axis.patches
# Make some labels.
for rect, label in zip(rects, not_take_exam):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 2, label, ha='center', va='bottom')

plt.show()