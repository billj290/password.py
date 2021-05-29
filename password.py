password = input('請輸入密碼: ')
if password == 'a123456':
		print('登入成功!')
if password != 'a123456':
	y = 2
	while y > 0:
		print('密碼錯誤, 還有', y, '次機會')
		input('請輸入密碼: ')
		y = y - 1
		