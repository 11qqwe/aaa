try:
	import requests,random
except Exception as AbuTariq:exit(AbuTariq)
red = '\033[1;31m'
Green = '\033[2;32m'
cyan = '\033[2;36m'
def Userlist():
	list = '1zx2cv4bn5ma3sdfg6hj8klqw7er9tyui0op'
	return ''.join(random.choice(list) for i in range(ask))
def Daddy_AbuTariq():
	while True:
		userr = Userlist()
		url = f'https://api.c2me.cc/b/nick_available?checksum=375868606731542156&nick={userr}&o=H15qN4msIPPS2DGu9hgtwAJ19OCUnluB'
		headers = {
			'Host': 'api.c2me.cc',
			'Accept': '*/*',
			'Accept-Language': 'ar-JO;q=1, en-JO;q=0.9',
			'Connection': 'close',
			'Accept-Encoding': 'gzip, deflate',
			'User-Agent': 'Connected2/1.301.2112140025 (iPhone; iOS 13.5; Scale/2.00)',
			}
		req = requests.get(url,headers=headers).text
		if '"status": "available"' in req:
			print(Green+f'متاح --> @{userr} ✅')
			kaito = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=\n available user connected2 \n-----------------\n \n @{userr}\n\n-----------------\n By : @ik48x')
			z = requests.post(kaito)
		elif '"status": "unavailable"' in req:
			print(red+f'غير متاح --> @{userr} ❌')
def main():
	global ask,token,id
	if __name__ == "__main__":
		print('''
	──▄▀▀▀▄───────────────
	──█───█─────────────── 	- By : 0x101
	─███████─────────▄▀▀▄─  - t.me/ik48x
	░██─▀─██░░█▀█▀▀▀▀█░░█░  - AbuTariq
	░███▄███░░▀░▀░░░░░▀▀░░
		''')
		token = input(cyan+'[=] توكن بوتك في تيليجرام --> :')
		id = input(cyan+'[=] ايديك في تيليجرام --> :')
		ask = int(input(cyan+'[#] اختر عدد احرف اليوزر --> :'))
		Userlist()
		Daddy_AbuTariq()
main()