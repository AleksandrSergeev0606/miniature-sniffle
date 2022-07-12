from translator import translator

lang =0
while lang != 1 or lang != 2:
    print("Выбирите язык ввода: 1 - Русский; 2 - Английский")
    lang = int(input())
    if lang == 1:
        print("Введите текст на русском")
        break
    if lang == 2:
        print("Введите текст на английском")
        break
    else:
        print("Введено неверное значение!")
text_input = str(input())
res = translator(lang, text_input)
