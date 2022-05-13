import requests
from .models import TeleSettings


def sendTelegram(tg_name, tg_phone, tg_id):
	if TeleSettings.objects.get(pk=1):
		settings = TeleSettings.objects.get(pk=1)
		token = str(settings.tg_token)
		chat_id = str(settings.tg_chat)
		text = str(settings.tg_message)
		api = 'https://api.telegram.org/bot'
		method = api + token + '/sendMessage'
		if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
			part1 = text[:text.find('{')]
			middletext = text[text.find('}') + 1:text.rfind('{')]
			part2 = middletext[:middletext.find('{')]
			part3 = middletext[middletext.find('}') + 1:]
			part4 = text[text.rfind('}'):-1]

			text_slice = part1 + tg_name + part2 + tg_phone + part3 + tg_id + part4

		else:
			text_slice = text

		try:
			req = requests.post(method, data={
				'chat_id': chat_id,
				'text': text_slice
				})
		except:
			pass
		finally:
			if req.status_code != 200:
				print('Ошибка отправки')
			elif req.status_code == 500:
				print('Ошибка 500')
			else:
				print('Сообщение отправлено!')

	else:
		pass
		

