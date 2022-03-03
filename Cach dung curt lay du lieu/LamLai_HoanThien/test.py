with open("AllDataClean.txt", encoding="utf8") as file:
	data = file.read().split("\n")

header = data[0]
students = data[1:]
students.pop()

total_student = len(students)

header = header.split(",")

subjects = header[5:]

for i in range(total_student):
	students[i] = students[i].split(",")


first_name_list = []
count_first_name = []

for s in students:
	d = s[1].split(" ")
	first_name = d[0]


	if first_name not in first_name_list:
		first_name_list.append(first_name)
		count_first_name.append(1)
	else:
		count_first_name[first_name_list.index(first_name)] += 1


for i in range(len(count_first_name)-1):
	for j in range(len(count_first_name)):
		if count_first_name[i] > count_first_name[j]:
			temp = count_first_name[i]
			count_first_name[i] = count_first_name[j]
			count_first_name[j] = temp

			temp = first_name_list[i]
			first_name_list[i] = first_name_list[j]
			first_name_list[j] = temp

print(first_name_list)
print(count_first_name)


# data = ["nguyễn quỳnh như", "phan nguyễn hoài như", "nguyễn trần quỳnh như", "phan tâm như" , "trần ngọc quỳnh như"]
# first_name_list = []
# count_first_name = []

# for i in range(len(data)):
# 	d = data[i].split(" ")
# 	first_name = d[0]
# 	try:
# 		index = first_name_list.index(first_name)
# 		print("xx")
# 	except:
# 		index = -1

# 	print(index)
# 	print(first_name)

# 	if index == -1:
# 		first_name_list.append(first_name)
# 		count_first_name.append(1)
# 	else:
# 		count_first_name[index] += 1



# print(first_name_list)
# print(count_first_name)

# s = ["loc", "linh"]
# try:
# 	print(s.index("loc"))
# except: 
# 	print(-1)

