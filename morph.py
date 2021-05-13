import pymorphy2
import functions
morph = pymorphy2.MorphAnalyzer()


class Morph:
    def __init__(self, word):
        self.word = word.lower()
        self.first_parsings = morph.parse(self.word)
        self.parsing = None
        self.signs = {'masc': 'мужской род', 'femn': 'женский род', 'neut': 'средний род',\
                 'nomn': 'именительный', 'gent': 'родительный', 'datv': 'дательный', 'accs': 'винительный',\
                 'ablt': 'творительный', 'loct': 'предложный', 'sing':'единственное число', 'plur':'множественное число', 'indc':'изъявительное наклонение',\
                 'impr':'повелительное наклонение', 'pres':'настоящее время', 'past':'прошедшее время','futr':'будущее время', '1per':'1 лицо','2per':'2 лицо',\
                 '3per':'3 лицо', 'actv':'действительное', 'pssv':'страдательное', 'perf':'совершенный вид', 'impf':'несовершенный вид', 'anim':'одушевлённое',\
                 'inan':'неодушевлённое', 'tran':'переходный', 'intr':'непереходый'}


    def morph(self):
        parsings = []
        for parsing in self.first_parsings:
            if parsing[3] >= 0.5:
                parsings.append(self.parsingq(parsing)) 
        if len(parsings) == 0:
            parsings.append(self.parsingq(self.first_parsings[0]))
        for parsing in parsings:
            if parsings[0] == parsing:
                parsings.remove(parsings[0]) 
        return parsings 


    def parsingq(self, parsing): #выбираем какую часть речи разобрать
        if parsing.tag.POS=='NOUN':
            return self.noun(parsing)
        elif parsing.tag.POS=='GRND':
            return self.grnd(parsing)
        elif parsing.tag.POS =='ADVB':
            return self.advb(parsing)
        elif parsing.tag.POS=='VERB':
            return self.verb(parsing)
        elif parsing.tag.POS=='INFN':
            return self.infn(parsing)
        elif parsing.tag.POS=='ADJF' or parsing.tag.POS=='ADJS' or {'COMP'} in parsing.tag:
            return self.adjf(parsing)
        elif parsing.tag.POS=='PRTF' or parsing.tag.POS == 'PRTS':
            return self.prtf(parsing)
        elif parsing.tag.POS =='NPRO':
            return self.npro(parsing)
        elif parsing.tag.POS == 'NUMR':
            return 'числительное'
        elif parsing.tag.POS == 'PREP':
            return 'предлог'
        elif parsing.tag.POS == 'CONJ':
            return 'частица'
        elif parsing.tag.POS == 'INTJ':
            return 'междометие'
        else:
            return 'такого не знаю'



    def noun(self, parsing): #существительное, работет
        self.parsing = '1.часть речи:\nимя существительное'
        self.parsing += f'\n\n2.начальная форма:\n{parsing.normal_form}'
        self.parsing += '\n\n3.постоянные признаки: '
        self.parsing += f'\n- {self.signs[parsing.tag.animacy]}'
        self.parsing += functions.gender(parsing)
        self.parsing += functions.iscommon(parsing)
        self.parsing += functions.declination(parsing.normal_form)
        self.parsing += '\n\n4.непостоянные признаки: '
        self.parsing += f'\n- {self.signs[parsing.tag.case]} падеж'
        self.parsing += f'\n- {self.signs[parsing.tag.number]}'
        return self.parsing



    def adjf(self, parsing):#прилагательное, работает
        self.parsing = '1.часть речи:\nприлагательное'
        self.parsing += f'\n\n2.начальная форма:\n{parsing.normal_form}'
        self.parsing += '\n\n3.постоянные признаки:'
        self.parsing += functions.isqual(parsing)
        self.parsing += '\n\n4.непостоянные признаки:'
        self.parsing += functions.issupr(parsing)
        self.parsing += functions.iscomp(parsing)
        if functions.iscomp == '\nполная форма':
            self.parsing += f'\n- {self.signs[parsing.tag.case]} падеж'
        self.parsing += f'\n- {self.signs[parsing.tag.number]}'
        self.parsing += functions.gender(parsing)
        return self.parsing



    def npro(self, parsing):
        self.parsing = '1.часть речи:\nместоимение'
        self.parsing += f'\n\n2.начальная форма:\n{parsing.normal_form}'
        self.parsing += '\n\n3.постоянные признаки:'
        self.parsing += functions.discharges(parsing.normal_form)
        self.parsing += functions.person(parsing)
        self.parsing += '\n\n4.непостоянные признаки:'
        self.parsing += f'\n- {self.signs[parsing.tag.case]} падеж'
        self.parsing += functions.gender(parsing)
        if parsing.tag.number in self.signs:
            self.parsing += f'\n- {self.signs[parsing.tag.number]}'
        return self.parsing


    def verb(self, parsing):# глагол, работает
        self.parsing = '1.часть речи:\nглагол'
        self.parsing += f'\n\n2.начальная форма:\n{parsing.normal_form}'
        self.parsing += '\n\n3.постоянные признаки: '
        self.parsing += f'\n- {self.signs[parsing.tag.aspect]}'
        self.parsing += functions.isreflection(parsing.normal_form)
        self.parsing += f'\n- {self.signs[parsing.tag.transitivity]}'
        self.parsing += functions.conjugation(parsing.normal_form)
        self.parsing += '\n\n4.непостоянные признаки: '
        self.parsing += f'\n- {self.signs[parsing.tag.mood]}'
        self.parsing += functions.time(parsing)
        self.parsing += f'\n- {self.signs[parsing.tag.number]}'
        self.parsing += functions.person(parsing)
        if {'past'} in parsing.tag:
            self.parsing += f'\n- {self.signs[parsing.tag.gender]}'
        return self.parsing



    def infn(self, parsing): #   инфнитив, работает
        self.parsing = '1.часть речи:\nглагол'
        self.parsing += f'\n\n2.начальная форма:\n{parsing.normal_form}'
        self.parsing += '\n\n3.постоянные признаки: '
        self.parsing += f'\n- {self.signs[parsing.tag.aspect]}'
        self.parsing += functions.conjugation(parsing.normal_form)
        self.parsing += functions.isreflection(parsing.normal_form)
        if 'tran' in parsing.tag:
            self.parsing += f'\n- переходный'
        elif 'intr' in parsing.tag:
            self.parsing += f'\n- непереходный'
        self.parsing += '\n\n3.непостоянные признаки:\n- инфинитив(неизменяемая форма)'
        return self.parsing

    def numeral(self, parsing):
        pass


    def grnd(self, parsing): #   деепричастие, работает
        self.parsing ='1.часть речи:\nдеепричастие'
        self.parsing += f'\n\n2.начальная форма:\n{parsing.normal_form}'
        self.parsing += '\n\n3.постоянные признаки: '
        self.parsing += f'\n- {self.signs[parsing.tag.aspect]}'
        self.parsing += functions.isreflection(parsing.normal_form)
        self.parsing += f'\n- {self.signs[parsing.tag.transitivity]}'
        self.parsing+='\n- неизменяемое'
        return self.parsing



    def advb(self, parsing):#   наречие, работает
        self.parsing = '\n1.часть речи:\nнаречие'
        self.parsing += f'\n\n2.начальная форма:\n{parsing.normal_form}'
        self.parsing += '\n\n3.постоянные признаки:\nнеизменяемое'
        return self.parsing



    def prtf(self, parsing):#  причастие, работает
        self.parsing = '1.часть речи:\nпричастие'
        self.parsing += f'\n\n2.начальная форма:\n{parsing.normal_form}'
        self.parsing += '\n\n3.постоянные признаки:'
        self.parsing += functions.isactv(parsing)
        self.parsing += f'\n- {self.signs[parsing.tag.aspect]}'
        self.parsing += functions.time(parsing)
        self.parsing += functions.isreflection(parsing.normal_form)
        self.parsing += '\n\n4.непостоянные признаки:'
        self.parsing += functions.isperf(parsing)
        if parsing.tag.case in self.signs:
            self.parsing += f'\n- {self.signs[parsing.tag.case]} падеж'
        self.parsing += f'\n- {self.signs[parsing.tag.number]}'
        self.parsing += f'\n- {self.signs[parsing.tag.gender]}'
        return self.parsing