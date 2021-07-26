from uzwords import words
from difflib import get_close_matches

def checkWord(word,words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    available = False # bunday so'z mavjud emas

    if word in matches:
        available = True # mavjud
        matches = word
    elif 'ҳ' in word:
        word = word.replace('ҳ', 'х')
        matches.update(get_close_matches(word, words))
    elif 'х' in word:
        word = word.replace('х', 'ҳ')
        matches.update(get_close_matches(word, words))

    return {'available': available, 'matches': matches}

if __name__ == '__main__':
    print(checkWord("ҳато"))
    print(checkWord("тариҳ"))
    print(checkWord("хато"))
    print(checkWord("олма"))
    print(checkWord("ҳат"))
    print(checkWord("ҳайт"))




