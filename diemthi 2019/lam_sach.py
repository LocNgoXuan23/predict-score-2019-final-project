with open("raw_data_test.txt", "r") as files:
	datas = files.read().split("\n")
with open("test_2.txt", "w", encoding="utf-8") as file:
	file.write("")

sbd = 10000010-1

for data in datas:
	try:
		sbd += 1
		data = data.split("\\n")
		for i in range(len(data)):
			tags = []
			for j in range(len(data[i])):
				if data[i][j] == "<":
					begin = j
				if data[i][j] == ">":
					end	= j
					tags.append(data[i][begin:end+1])

			for k in range(len(tags)):
				data[i] = data[i].replace(tags[k], "")


		for i in range(len(data)):
			data[i] = data[i].strip()

		with open("unicode (1).txt", encoding="utf8") as file:
			unicode_table = file.read().split("\n")

		codes = []
		chars = []
		for code in unicode_table:
			code = code.split(" ")
			chars.append(code[0])
			codes.append(code[1])

		for i in range(len(data)):
			for j in range(len(codes)):
				data[i] = data[i].replace(codes[j], chars[j])

		# data = data[100]
		data = data[99]
		# begin_sbd = data.find("thiSố báo danh: ") + len("thiSố báo danh: ")
		# end_sbd = data.find("ToánVănNgoại")
		# sbd = data[begin_sbd:end_sbd]

		begin = data.find("báo danh: ") + 9
		end = data.find("FTin tức")
		data = data[begin:end]
		f = data.find("Toán")
		h = data.find("Toán", f+1)

		data = data[h:]
		subject = ["Toán", "Ngữ văn", "Ngoại ngữN1:", "Ngoại ngữN2:", "Ngoại ngữN3:", "Ngoại ngữN4:", "Ngoại ngữN5:", "Ngoại ngữN6:", "Ngoại ngữ", "Vật lí", "Hóa học", "Sinh học", "Lịch sử", "Địa lí", "GDCD"]
		data = data + " "
		scores_list = [sbd]
		for s in subject:
			begin = data.find(s) + len(s)
			if data[begin].isdigit():
				if data[begin:begin+2] == "10":
					scores_list.append("10")
				elif data[begin+1] == ".":
					scores_list.append(data[begin:begin+4])
				elif data[begin+1] != ".":
					scores_list.append(data[begin])
			else:
				scores_list.append("-1")
		
		data =scores_list
		for i in range(len(data)):
			data[i] = str(data[i]).replace("V", "")
			data[i] = str(data[i]).replace("N", "")
			data[i] = str(data[i]).replace("H", "")
			data[i] = str(data[i]).replace("S", "")
			data[i] = str(data[i]).replace("L", "")
			data[i] = str(data[i]).replace("Đ", "")
			data[i] = str(data[i]).replace("G", "")


		with open("test_2.txt", "a", encoding="utf-8") as file:
			for i in range(len(data)):
				if i == len(data) - 1:
					file.write(str(data[i]))
				else:
					file.write(str(data[i]) + ",")
			file.write("\n")
	except:
		print(sbd)









# s = "locloclongloc"

# s = s.replace("long", "Xxx")

# print(s)









