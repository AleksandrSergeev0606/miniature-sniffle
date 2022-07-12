from translate import Translator
from langdetect import detect

def translator(lang, text_input):
    if lang == 1:
        tr = Translator(to_lang='en', from_lang='ru')
    if lang == 2:
        tr = Translator(to_lang='ru', from_lang='en')
    text_output = tr.translate(text_input)
    assert isinstance(text_output, str)
    print(text_output)
    print(detect(text_input))
