url_head = "http://www.biquge.com.tw/"

for c in range(0, 2):
	for i in range(1, 10):
		url = url_head + str(c) + '_'
		if c == 0:
			url += str(i)
		else:
			url += str(c*1000 + i)
		print url
