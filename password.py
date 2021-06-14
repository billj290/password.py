psw = 'a123456'
y = 3 #能夠嘗試的機會
while y > 0:
	y = y - 1
	x = input('請輸入密碼: ')
	if x != psw:
		print('密碼錯誤')
		if y > 0:
			print('尚有', y, '次機會')
		else:
			print('沒機會鎖帳號!')
	else:
		print('登入成功')
		break