from translate import Translator

lang = input('Available Langs:(e.g. en, ja, ko, pt, pt-br, zh, zh-TW, ...)\nWhich one Lang?: ')
langs = ['e.g.', 'en', 'ja', 'ko', 'pt', 'pt-br', 'zh', 'zh-TW']
verification = False

for itens in langs:
	if itens == lang:
		verification = True
		break

if verification:
	text = input('Type text for translate: ')
	translator = Translator(to_lang=f'{lang}')
	translation = translator.translate(text)	
	print(f'Text: {translation}')
else:
	print('[Erro] None lang found!')