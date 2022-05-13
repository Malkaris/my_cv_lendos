from django.test import TestCase

# Create your tests here.
text = 'Имя {name} Телефон {phone} Ссылка на телеграм {telegram_id}'

a = text.find('{')
b = text.find('}')
e = text.rfind('{')
f = text.rfind('}')
part1 = text[:a]
middletext = text[b+1:e]
part2 = middletext[:middletext.find('{')]
part3 = middletext[middletext.find('}')+1:]
part4 = text[f:-1]

# print(part1)
# print(part2)
# print(part3)
print(part1 + '1' + part2 + '2' + part3 + '3' + part4)