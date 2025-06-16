filt_mat = ['блять', 'пизда', 'хуй', 'еблан', 'сука', 'нахуй']

def censor(word):
    if len(word) > 2:
        return word[0] + '*' * (len(word) - 2) + word [-1]
    return word

def txt_filt(text):
    words = text.split()
    bad_wrds = False
    for i in range(len(words)):
        lower_word = words[i].lower()
        chistka_slova = lower_word.strip('.,!?:;- ')
        if chistka_slova in filt_mat:
            words[i] = censor(words[i])
            bad_wrds = True
    return ' '.join(words), bad_wrds

txt_from_user = input('Введите ваш текст! ')
if not txt_from_user:
    print('Тексат нет!')
else:
    filt_txt, censor_needs = txt_filt(txt_from_user)

    if not censor_needs:
        print('Чистый текст, мата нет!')
    else:
        print(f"Отфильтрованный текст: {filt_txt}")