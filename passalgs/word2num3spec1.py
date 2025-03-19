from wonderwords import RandomWord
from random import choice, randint, sample, shuffle
from .common import gen_spec, Lio_solver

def gen_number():
    num = randint(1,999)
    num_str = str(num)
    if num < 10 :
        return '00' + num_str
    if num <100:
        return '0' + num_str
    return num_str

#@Lio_solver
def gen_word():
    num= randint(1,3)
    r = RandomWord()
    s = r.word(include_parts_of_speech=["nouns", "adjectives", "verbs"], word_max_length=7, word_min_length=3)
    s_list= list(s)
    
    if num >= len(s):
        return s.upper()
    
    random_inx = sample(range(len(s)), num)
    for i in random_inx:
        s_list[i]= s_list[i].upper()
        
    return ''.join(s_list)
    
    
def gen_spec():
    return choice(('!','#',"_",'-','+','=','%','$'))

def gen_pass():
    li = [gen_word(), gen_word(), gen_number(), gen_spec()]
    shuffle(li)
    return ''.join(li)