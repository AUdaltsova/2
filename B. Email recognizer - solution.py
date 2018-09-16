import re
a = input()
res = re.split(r'\@', a)
a = res[1]
res = re.split(r'\.', a)
if len(res) >= 2:
	if str(res[-1]) == 'com' or str(res[-1]) == 'de' or str(res[-1]) == 'cn' or str(res[-1]) == 'uk' or str(res[-1]) == 'net' or str(res[-1]) == 'org' or str(res[-1]) == 'info' or str(res[-1]) == 'ru' or str(res[-1]) == 'nl' or str(res[-1]) == 'tk':
		print('yes')
	else:
		print('no')
else:
	print('no')
#used most popular TLDs, considering the server providing the adress can be anything(hse, yandex, google, yahoo, mail etc.)
