from translate import Translator
from langdetect import detect

print("Введите текст")
text = str(input())
lang = str(detect(text))
print("Язык ввода", lang)
tr = Translator(to_lang='ru', from_lang=lang)
text_output = tr.translate(text)
print(text_output)