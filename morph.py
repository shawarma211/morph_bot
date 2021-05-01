import pymorphy2
import functions
morph = pymorphy2.MorphAnalyzer()


class Morph:
    def __init__(self, word):
        self.word = word.lower()
        self.first_parsings = morph.parse(self.word)[0]
        self.parsing = None
        self.signs = {'masc': 'мужской род', 'femn': 'женский род', 'neut': 'средний род',\
                 'nomn': 'именительный', 'gent': 'родительный', 'datv': 'дательный', 'accs': 'винительный',\
                 'ablt': 'творительный', 'loct': 'предложный', 'sing':'единственное число', 'plur':'множественное число', 'indc':'изъявительное наклонение',\
                 'impr':'повелительное наклонение', 'pres':'настоящее время', 'past':'прошедшее время','futr':'будущее время', '1per':'1 лицо','2per':'2 лицо',\
                 '3per':'3 лицо', 'actv':'действительное', 'pssv':'страдательное', 'perf':'совершенный вид', 'impf':'несовершенный вид', 'anim':'одушевлённое',\
                 'inan':'неодушевлённое', 'tran':'переходный', 'intr':'непереходый'}




    def parsingq(self): #выбираем какую часть речи разобрать
        if self.first_parsings.tag.POS=='NOUN':
            return self.noun()
        elif self.first_parsings.tag.POS=='GRND':
            return self.grnd()
        elif self.first_parsings.tag.POS =='ADVB':
            return self.advb()
        elif self.first_parsings.tag.POS=='VERB':
            return self.verb()
        elif self.first_parsings.tag.POS=='INFN':
            return self.infn()
        elif self.first_parsings.tag.POS=='ADJF' or self.first_parsings.tag.POS=='ADJS' or {'COMP'} in self.first_parsings.tag:
            return self.adjf()
        elif self.first_parsings.tag.POS=='PRTF' or self.first_parsings.tag.POS == 'PRTS':
            return self.prtf()
        else: 
            return 'такого не знаю'



    def noun(self): #существительное, работет
        self.parsing = '1) часть речи:\n     имя существительное'
        self.parsing += f'\n2) начальная форма:\n     {self.first_parsings.normal_form}'
        self.parsing += '\n2) постоянные признаки: '
        self.parsing += f'\n     {self.signs[self.first_parsings.tag.animacy]}'
        self.parsing += functions.gender(self.first_parsings)
        self.parsing += functions.iscommon(self.first_parsings)
        self.parsing += functions.declination(self.first_parsings.normal_form)
        self.parsing += '\n3) непостоянные признаки: '
        self.parsing += f'\n     {self.signs[self.first_parsings.tag.case]} падеж'
        self.parsing += f'\n     {self.signs[self.first_parsings.tag.number]}'
        return self.parsing



    def adjf(self):#прилагательное, работает
        self.parsing = '1) часть речи:\n     прилагательное'
        self.parsing += f'\n2) начальная форма:\n     {self.first_parsings.normal_form}'
        self.parsing += '\n3) постоянные признаки:'
        self.parsing += functions.isqual(self.first_parsings)
        self.parsing += '\n4) непостоянные признаки:'
        self.parsing += functions.issupr(self.first_parsings)
        self.parsing += functions.iscomp(self.first_parsings)
        if functions.iscomp == '\n     полная форма':
            self.parsing += f'\n     {self.signs[self.first_parsings.tag.case]} падеж'
        self.parsing += f'\n     {self.signs[self.first_parsings.tag.number]}'
        self.parsing += functions.gender(self.first_parsings)
        return self.parsing



    def verb(self):# глагол, работает
        self.parsing = '1) часть речи:\n     глагол'
        self.parsing += f'\n2) начальная форма:\n     {self.first_parsings.normal_form}'
        self.parsing += '\n3)постоянные признаки: '
        self.parsing += f'\n     {self.signs[self.first_parsings.tag.aspect]}'
        self.parsing += functions.isreflection(self.first_parsings.normal_form)
        self.parsing += f'\n     {self.signs[self.first_parsings.tag.transitivity]}'
        self.parsing += functions.conjugation(self.first_parsings.normal_form)
        self.parsing += '\n4) непостоянные признаки: '
        self.parsing += f'\n     {self.signs[self.first_parsings.tag.mood]}'
        self.parsing += functions.time(self.first_parsings)
        self.parsing += f'\n     {self.signs[self.first_parsings.tag.number]}'
        self.parsing += functions.person(self.first_parsings)
        if {'past'} in self.first_parsings.tag:
            self.parsing += f'\n     {self.signs[self.first_parsings.tag.gender]}'
        return self.parsing



    def infn(self): #   инфнитив, работает, нет возвратности 
        self.parsing = '1) часть речи:\n     глагол'
        self.parsing += f'\n2) начальная форма:\n     {self.first_parsings.normal_form}'
        self.parsing += '\n3) постоянные признаки: '
        self.parsing += f'\n     {self.signs[self.first_parsings.tag.aspect]}'
        self.parsing += functions.conjugation(self.first_parsings.normal_form)
        self.parsing += functions.isreflection(self.first_parsings.normal_form)
        self.parsing += f'\n     {self.signs[self.first_parsings.tag.transitivity]}'
        self.parsing += '\n3) непостоянные признаки:\n     инфинитив(неизменяемая форма)'
        return self.parsing



    def grnd(self): #   деепричастие, работает
        self.parsing ='1) часть речи:\n     деепричастие'
        self.parsing += f'\n2) начальная форма:\n     {self.first_parsings.normal_form}'
        self.parsing += '\n3) постоянные признаки: '
        self.parsing += f'\n     {self.signs[self.first_parsings.tag.aspect]}'
        self.parsing += functions.isreflection(self.first_parsings.normal_form)
        self.parsing += f'\n     {self.signs[self.first_parsings.tag.transitivity]}'
        self.parsing+='\n     неизменяемое'
        return self.parsing



    def advb(self):#   наречие, работает
        self.parsing = '\n1) часть речи:\n     наречие'
        self.parsing += f'\n2) начальная форма:\n     {self.first_parsings.normal_form}'
        self.parsing += '\n3) постоянные признаки:\n     неизменяемое'
        return self.parsing



    def prtf(self):#  причастие, работает
        self.parsing = '1) часть речи:\n   причастие'
        self.parsing += f'\n2) начальная форма:\n    {self.first_parsings.normal_form}'
        self.parsing += '\n3) постоянные признаки: '
        self.parsing += functions.isactv(self.first_parsings)
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.aspect]}'
        self.parsing += functions.time(self.first_parsings)
        self.parsing += functions.isreflection(self.first_parsings.normal_form)
        self.parsing += '\n4) непостоянные признаки: '
        self.parsing += functions.isperf(self.first_parsings)
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.case]} падеж'
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.number]}'
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.gender]}'
        return self.parsing
