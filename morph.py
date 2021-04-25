import pymorphy2
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
        elif self.first_parsings.tag.POS=='ADJF' or self.first_parsings.tag.POS=='ADJS':
            return self.adjf()
        elif self.first_parsings.tag.POS=='PRTF' or self.first_parsings.tag.POS == 'PRTS':
            return self.prtf()
        else: 
            return 'такого не знаю'


    def noun(self): #существительное, работет
        self.parsing = '\n1) часть речи: имя существительное'
        self.parsing = f'2) начальная форма: {self.first_parsings.normal_form}'
        self.parsing += '\n2) постоянные признаки: '
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.animacy]}'
        if {'masc'} in self.first_parsings.tag:
            self.parsing += '\n    мужской род'
        elif {'femn'} in  self.first_parsings.tag:
            self.parsing += '\n    женский род'
        elif {'neut'} in self.first_parsings.tag:
            self.parsing += '\n    средний род'
        if {'Name'} in self.first_parsings.tag or {'Surn'} in self.first_parsings.tag or {'Patr'} in self.first_parsings.tag or {'Geox'} in self.first_parsings.tag or {'Geox'} in self.first_parsings.tag:
            self.parsing += '\n    собственное'
        else:
            self.parsing += '\n    нарицательное'
        if (self.first_parsings.tag.gender == 'masc' or self.first_parsings.tag.gender == 'femn') and (self.first_parsings.normal_form[-1]=='а' or 'neut'):
            self.parsing += '\n    1 склонение'
        elif self.first_parsings.normal_form[-1] == 'ь':
            self.parsing += '\n    3 склонение'
        else:
            self.parsing += '\n    2 склонение'
        self.parsing += '\n3) непостоянные признаки: '
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.case]} падеж'
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.number]}'
        return self.parsing
    

    def adjf(self):
        #TOODO
        pass


    def verb(self):# глагол, работает, нет возвратности 
        self.parsing = '\n1) часть речи: глагол'
        self.parsing = f'\n2) начальная форма: {self.first_parsings.normal_form}'
        self.parsing += '\n3)постоянные признаки: '
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.aspect]}'
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.transitivity]}'
        self.parsing += '\n3) непостоянные признаки: '
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.mood]}'
        if {'pres'} in self.first_parsings.tag:
            self.parsing += '\n    настоящее'
        elif {'futr'} in self.first_parsings.tag:
            self.parsing += '\n    будущее'
        elif {'past'} in self.first_parsings.tag:
            self.parsing += '\n    прошедшее'
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.number]}'
        if {'1per'} in self.first_parsings.tag:
            self.parsing += '\n    1 лицо'
        elif {'2per'} in self.first_parsings.tag:
            self.parsing += '\n    2 лицо'
        elif {'3per'} in self.first_parsings.tag:
            self.parsing += '\n    3 лицо'
        if {'past'} in self.first_parsings.tag:
            self.parsing += f'\n    {self.signs[self.first_parsings.tag.gender]}'
        return self.parsing
    

    def infn(self): #   инфнитив, работает, нет возвратности 
        self.parsing = '\n1) часть речи: глагол'
        self.parsing = f'2) начальная форма: {self.first_parsings.normal_form}'
        self.parsing += '\n3) постоянные признаки: '
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.aspect]}'
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.transitivity]}'
        self.parsing += '\n3) непостоянные признаки: \n    инфинитив(неизменяемая форма)'
        return self.parsing


    def grnd(self): #   деепричастие, работает, нет возвратности 
        self.parsing ='\n1) часть речи: деепричастие'
        self.parsing = f'2) начальная форма: {self.first_parsings.normal_form}'
        self.parsing += '\nпостоянные признаки: '
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.aspect]}'
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.transitivity]}'
        self.parsing+='\nнеизменяемая форма'
        return self.parsing


    def advb(self):#   наречие, работает, нет категории  
        self.parsing += '\n1) часть речи: наречие'
        self.parsing += '\n2) постоянные признаки: '
        self.parsing += '\n3) непостоянные признаки: '
        self.parsing += '\n    nнеизменяемое'
        return self.parsing


    def prtf(self):#  причастие, работает, нет возвратности 
        self.parsing = '\n1) часть речи: причастие'
        self.parsing += '\n3) постоянные признаки: '
        if {'actv'} in self.first_parsings.tag:
            self.parsing += '\n    действительное'
        else:
            self.parsing += '\n    страдательное'
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.number]}'
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.aspect]}'
        self.parsing += '\n4) непостоянные признаки: '
        if self.first_parsings.tag.POS=='PRTS':
            self.parsing += '\n    краткая форма'
        else:
            self.parsing += '\n    полная форма'
            self.parsing += f'\n    {self.signs[self.first_parsings.tag.case]} падеж'
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.number]}'
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.gender]}'
        return self.parsing

        

word = Morph('ножницы')
print(word.parsingq())
