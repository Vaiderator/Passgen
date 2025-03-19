from random import choice

def gen_spec():
    return choice(('!','#',"_",'-','+','=','%','$'))

def Lio_solver(func):
    def wrapper():
        res = func()
        res = list(res)
        credit = 0
        for i in range(len(res)):
            if res[i] == 'l':
                res[i]='L'
                credit-=1
            elif res[i] == 'I':
                res[i]='i'
                credit+=1
            elif res[i] =='O':
                res[i]='o'
                credit+=1
            elif credit > 0:
                res[i]=res[i].upper()
                credit-=1
            elif credit < 0 and res[i] not in ['i','L','o']:
                res[i]=res[i].lower()
                credit+=1
        
        return ''.join(res)
    
    return wrapper