import subprocess

start = 10000010
end = 10000015
with open("raw_data_test.txt", "w") as file:
	for i in range(start, end):
		data = subprocess.check_output('curl https://vietnamnet.vn/vn/giao-duc/tra-cuu-diem-thi-thpt/?y=2020&sbd=' + str(i))
		if i == end-1:
			file.write(str(data))
		else:
			file.write(str(data) + "\n")



