
def stop_word(list):
    stop = ['을', '에', '가가', '개', '의', '던', '았', '었', '은', '를', '는', '인', '데']

    new_input = ''
    for inp in list:
        if inp not in stop:
            new_input += inp

    return new_input
