import pymorphy2
import functions
morph = pymorphy2.MorphAnalyzer()


class Morph:
    def __init__(self, word):
        self.word = word.lower()
        self.first_parsings = morph.parse(self.word.split()[0])
        self.parsing = None
        self.signs = {'nomn': 'именительный', 'gent': 'родительный', 'datv': 'дательный', 'accs': 'винительный',\
                 'ablt': 'творительный', 'loct': 'предложный', 'sing':'единственное число', 'plur':'множественное число', 'indc':'изъявительное наклонение',\
                 'impr':'повелительное наклонение', 'perf':'совершенный вид', 'impf':'несовершенный вид', 'anim':'одушевлённое',\
                 'inan':'неодушевлённое', 'tran':'переходный', 'intr':'непереходый'}


    def template_parsings(self):
        if self.word == 'имя существительное':
            return '1.часть речи\nимя существительное\nобщее грамматическое значение: предмет\n\n2.начальная форма\nименительный падеж, единственное число\n\n3.постоянные признаки:\n- нарицательное или собственное\n- одушевленное или неодушевленное\n- род\n- склонение\n\n4.непостоянные признаки:\n- падеж\n- число\n\n5.Синтаксическая роль'
        elif self.word == 'имя прилагательное':
            return '1.часть речи\nимя прилагательное\nобщее грамматическое значение: признак предмета\n\n2.начальная форма:\nименительный падеж, единственное число, мужской род\n\n3.постоянные признаки:\n- качественное, относительное или притяжательное\n\n4.непостоянные признаки:\n- степень сравнения\n- краткая или полная форма\n- падеж\n- число\n- род\n\n5.синтаксическая роль'
        elif self.word == 'имя числительное':
            return '1.часть речи\nимя числительное\nобщее грамматическое значение: количество или порядок предметов при счёте\n\n2.начальная форма:\nименительный падеж\n\n3.постоянные признаки:\n- простое или составное\n- количественное или порядковое\n- разряд(для количественных)\n\n4.непостоянные признаки:\n- падеж\n- число(если есть)\n- род(если есть)\n\n5.синтаксическая роль'
        elif self.word == 'местоимение':
            return '1.часть речи\nместоимение\nобщее грамматическое значение: указание на предмет, объект, признак или количество, не называя их\n\n2.начальная форма\nименительный падеж, единственное число\n\n3.постоянные признаки:\n- разряд\n- лицо(у личных местоимений)\n\n4.непостоянные признаки:\n- падеж\n- число(если есть)\n- род(если есть)\n\n5.синтаксическая роль'
        elif self.word == 'глагол':
            return '1.часть речи\nглагол\nобщее грамматическое значение: означает действие или состояние предмета\n\n2.начальная форма\nнеопределённая форма\n\n3.постоянные признаки:\n- вид\n- спряжение\n- переходность\n\n4.непостоянные признаки:\n- наклонение\n- число\n- время(если есть)\n- лицо(если есть)\n- род(если есть)\n\n5.синтаксическая роль'
        elif self.word == 'наречие':
            return '1.часть речи\nнаречие\nобщее грамматическое значение: означает признак действия предмета или другого признака\n\n2.начальная форма:\nнеизменяемое\n\n3.постоянные признаки:\n- сравнительная или превосходная степень сравнения (если есть)\n- группа по значению\n\n4.синтаксическая роль'
        elif self.word == 'причастие':
            return '1.часть речи\nпричастие\nобщее грамматическое значение: означает признак предмета по действию\n\n2.начальная форма:\nименительный падеж, единственное число, мужской род\n\n3.постоянные признаки:\n- действительное или страдательное\n- время\n- вид\n\n4.непостоянные признаки:\n- полная или краткая форма(у страдательных)\n- падеж(в полной форме),\n- число\n- род\n\n5.синтаксическая роль'
        elif self.word == 'деепричастие':
            return '1.часть речи\nдеепричастие\nобщее грамматическое значение: означает добавочное действие при основном действии, выраженном глаголом\n\n2.начальная форма:\nнеизменяемое\n\n3.постоянные признаки:\n- вид\n- переходность\n- возвратность\n\n4.синтаксическая роль'
        return self.morph()


    def morph(self):
        parsings = []
        for parsing in self.first_parsings:
            if parsing[3] >= 0.5:
                parsings.append(self.parsingq(parsing)) 
        if len(parsings) == 0:
            parsings.append(self.parsingq(self.first_parsings[0]))
        if len(parsings) > 1 and parsings[0] == parsings[1]:
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
        self.parsing = '1.часть речи:\nимя существительное\nобщее значение: предмет'
        self.parsing += f'\n\n2.начальная форма:\n{parsing.normal_form}'
        self.parsing += '\n\n3.постоянные признаки: '
        self.parsing += functions.iscommon(parsing)
        self.parsing += f'\n- {self.signs[parsing.tag.animacy]}'
        self.parsing += functions.gender(parsing)
        self.parsing += functions.declination(parsing.normal_form)
        self.parsing += '\n\n4.непостоянные признаки: '
        self.parsing += f'\n- {self.signs[parsing.tag.case]} падеж'
        self.parsing += f'\n- {self.signs[parsing.tag.number]}'
        return self.parsing



    def adjf(self, parsing):#прилагательное, работает
        self.parsing = '1.часть речи:\nимя прилагательное\nобщее грамматическоен значение: признак предмета'
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
        self.parsing = '1.часть речи:\nместоимение\nобщее грамматическое значение: указание на предмет, объект, признак или количество, не называя их'
        self.parsing += f'\n\n2.начальная форма:\n{parsing.normal_form}'
        self.parsing += '\n\n3.постоянные признаки:'
        self.parsing += functions.discharges(parsing.normal_form)
        if functions.discharges(parsing.normal_form) == '\n- личное':
            self.parsing += functions.person(parsing)
        self.parsing += '\n\n4.непостоянные признаки:'
        self.parsing += f'\n- {self.signs[parsing.tag.case]} падеж'
        self.parsing += functions.gender(parsing)
        if parsing.tag.number in self.signs:
            self.parsing += f'\n- {self.signs[parsing.tag.number]}'
        return self.parsing



    def verb(self, parsing):# глагол, работает
        self.parsing = '1.часть речи:\nглагол\nобщее грамматическое значение: означает действие или состояние предмета'
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
            self.parsing += functions.gender(parsing)
        return self.parsing



    def infn(self, parsing): #   инфнитив, работает
        self.parsing = '1.часть речи:\nглагол\nобщее грамматическое значение: означает действие или состояние предмета'
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
        return 'Числительное'

    
    def grnd(self, parsing): #   деепричастие, работает
        self.parsing ='1.часть речи:\nдеепричастие\nобщее грамматическое значение: означает добавочное действие при основном действии, выраженном глаголом'
        self.parsing += f'\n\n2.начальная форма:\n{parsing.normal_form}'
        self.parsing += '\n\n3.постоянные признаки: '
        self.parsing += f'\n- {self.signs[parsing.tag.aspect]}'
        self.parsing += functions.isreflection(parsing.normal_form)
        self.parsing += f'\n- {self.signs[parsing.tag.transitivity]}'
        self.parsing+='\n- неизменяемое'
        return self.parsing



    def advb(self, parsing):#   наречие, работает
        self.parsing = '\n1.часть речи:\nнаречие\nобщее грамматическое значение: означает признак действия предмета или другого признака'
        self.parsing += f'\n\n2.начальная форма:\n{parsing.normal_form}'
        self.parsing += '\n\n3.постоянные признаки:\nнеизменяемое'
        return self.parsing



    def prtf(self, parsing):#  причастие, работает
        self.parsing = '1.часть речи:\nпричастие\nобщее грамматическое значение: означает признак предмета по действию'
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
        self.parsing += functions.gender(parsing)
        return self.parsing