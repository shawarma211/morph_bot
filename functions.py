import pymorphy2
morph = pymorphy2.MorphAnalyzer()


def declination(word):#склонение существительного
    parsing = morph.parse(word)[0]
    if (parsing.tag.gender == 'masc' or parsing.tag.gender == 'femn') and (parsing.normal_form[-1] == 'а' or parsing.normal_form[-1] == 'я'):
        return '\n     1 склонение'
    elif parsing.normal_form[-1] == 'ь':
        return '\n     3 склонение'
    return '\n     2 склонение'


def iscommon(word):#нарицательное существительное/прилагательное
    if {'Name'} in word.tag or {'Surn'} in word.tag or {'Patr'} in word.tag or {'Geox'} in word.tag or {'Geox'} in word.tag:
        return '\n     собственное'
    return '\n     нарицательное'


def gender(word):#определяет род у прилагательных/существительного
    if {'masc'} in word.tag:
        return '\n     мужской род'
    elif {'femn'} in  word.tag:
        return '\n     женский род'
    elif {'neut'} in  word.tag:
        return '\n     средний род'
    return ''


def isqual(word):#че то у прилагательного
    if {'Poss'} in word.tag:
        return '\n     притяжательное'
    elif {'Qual'} in word.tag:
        return '\n     качественное'
    return '\n     относительное'


def isactv(word):#залог причастия
    if {'actv'} in word.tag:
        return'\n     действительное'
    return '\n     страдательное'


def iscomp(word):#какая форма прилагательного
    if word.tag.POS == 'ADJS':
        return '\n     краткая форма'
    else:
        return '\n     полная форма'


def issupr(word):#степень превосходности у прилагательного
    if {'Qual'} in word.tag:
        if {'COMP'} in word.tag:
            return '\n     сравнительная'
        elif {'Supr'} in word.tag:
            return '\n     превосходная'
        return ''
    return ''


def isperf(word):#степень превосходности у причастия\
    if word.tag.POS=='PRTS':
        return '\n     краткая форма'
    return '\n     полная форма'  


def isreflection(word):#возвратность для глагола
    b = False
    if word[-2]+word[-1] =='сь' or word[-2]+word[-1] =='ся':
        b = True
        return '\n     возвратное'
    return '\n     невозвратное'
    

def time(word):#время для глагола/причастия
    if {'pres'} in word.tag:
        return '\n     настоящее'
    elif {'futr'} in word.tag:
        return '\n     будущее'
    elif {'past'} in word.tag:
        return '\n     прошедшее'
    return '' 


def person(word):#лицо для глагола
    if {'1per'} in word.tag:
        return '\n     1 лицо'
    elif {'2per'} in word.tag:
        return '\n     2 лицо'
    elif {'3per'} in word.tag:
        return '\n     3 лицо'
    return ''


def conjugation(word):#спряжение для глагола
    exceptions_for_1 = ['гнать', 'держать', 'терпеть', 'обидеть', 'видеть', 'слышать', 'ненавидеть', 'зависеть', 'вертеть', 'дышать', 'смотреть']
    exceptions_for_2 = ['брить', 'стелить']
    if ('ить' in word or word in exceptions_for_1) and (word not in exceptions_for_2):
        return '\n     2 спряжение'
    return '\n     1 спряжение'