with open("raw_data.txt", "r") as file:
	datas = file.read().split("\n")

with open("AllDataClean.txt", encoding="utf8", mode = "w") as file:
	header = ["sbd", "tên", "dd", "mm", "yy", "toán", "ngữ văn", "khxh", "khtn", "lịch sử", "địa lí", "gdcd", "sinh học", "vật lí", "hóa học", "tiếng anh"]
	for i in range(len(header)):
		if i != len(header) - 1:
			file.write(header[i] + ",")
		else:
			file.write(header[i])
	file.write("\n")

sbd = 2000000

for data in datas:
	try:
		data  = data.split("\\n")
		sbd += 1
		# remove \r and \t
		for i in range(len(data)):
			data[i] = data[i].replace("\\r", "")
			data[i] = data[i].replace("\\t", "")

		# remove tags
		for i in range(len(data)):
			tags = []
			for j in range(len(data[i])):
				if data[i][j] == "<":
					begin = j
				if data[i][j] == ">":
					end = j
					tags.append(data[i][begin:end+1])

			for tag in tags:
				data[i] = data[i].replace(tag, "")

		# remove leading whitespace
		for i in range(len(data)):
			data[i] = data[i].strip()

		# remove empty line
		unempty_lines = []
		for i in range(len(data)):
			if data[i] != "":
				unempty_lines.append(data[i])
		data = unempty_lines

		# choose relevant information
		name = data[7]
		dob = data[8]
		scores = data[9]

		# load unicode table
		chars = [] # special characters
		codes = [] # code of special characters

		file = open("unicode.txt", encoding="utf8")
		unicode_table = file.read().split("\n")



		for code in unicode_table:
			x = code.split(" ")
			chars.append(x[0])
			codes.append(x[1])

		# replace special characters in name and scores
		for i in range(len(chars)):
			name = name.replace(codes[i], chars[i])
			scores = scores.replace(codes[i], chars[i])

		name_count = name.count("&#")
		scores_count = scores.count("&#")
		for i in range(name_count):
			index = name.find("&#")
			name = name[:index] + chr(int(name[index+2:index+5])) + name[index+6:]

		for i in range(scores_count):
			index = scores.find("&#")
			scores = scores[:index] + chr(int(scores[index+2:index+5])) + scores[index+6:]

		name = name.lower()
		scores = scores.lower()
		dob = dob.split("/")
		dd = dob[0]
		mm = dob[1]
		yy = dob[2]
		data = [str(sbd), name, dd, mm, yy]

		scores = scores.replace(":", "")
		scores = scores.replace("khxh ","khxh   ")
		scores = scores.replace("khtn ","khtn   ")
		scores = scores.split("   ")

		subjects = ["toán", "ngữ văn", "khxh", "khtn", "lịch sử", "địa lí", "gdcd", "sinh học", "vật lí", "hóa học", "tiếng anh"]
		for sub in subjects:
			if sub in scores:
				index = scores.index(sub)
				data.append(scores[index+1])
			else: 
				data.append("-1")
			

		with open("AllDataClean.txt", encoding="utf8", mode = "a") as file:
			for i in range(len(data)):
				if i != len(data) - 1:
					file.write(data[i] + ",")
				else:
					file.write(data[i])
			file.write("\n")
	except:
		print(sbd)



