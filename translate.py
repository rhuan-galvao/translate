from translate import Translator

langs = ('e.g.', 'en', 'ja', 'ko', 'pt', 'pt-br', 'zh', 'zh-TW')
lang = input('Available Languages: {0}\nWhich one Language?: '.format(langs))

if lang in langs:
	text = input('Type text for translate: ')
	translator = Translator(to_lang=lang)
	translation = translator.translate(text)	
	print('Text: {0}'.format(translation))
else:
	print('[Error] Language not found!')

	