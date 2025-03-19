from .common import gen_spec, Lio_solver
from wonderwords import RandomWord
from random import randint, shuffle


@Lio_solver
def gen_word():
    num= randint(1,2)
    r = RandomWord()
    s = r.word(include_parts_of_speech=["nouns"], word_max_length=7, word_min_length=4)
    num = min(num,len(s))
    return s[:num].upper() + s[num:]

def gen_pass():
    li = [str(randint(0,9)), str(randint(0,9)), str(randint(0,9)), gen_spec(), gen_word(), gen_word()]
    shuffle(li)
    return ''.join(li)
