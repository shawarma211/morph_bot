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
        if self.first_parsings.tag.POS =='ADVB':
            return self.advb()
        elif self.first_parsings.tag.POS=='VERB':
            return self.verb()
        elif self.first_parsings.tag.POS=='INFN':
            return self.infn()
        elif self.first_parsings.tag.POS=='ADJF' or self.first_parsings.tag.POS=='ADJS':
            return self.adjf()
        else: 
            return 'такого не знаю'


    def noun(self): #существительное, работет
        self.parsing = '\n1) часть речи: имя существительное'
        self.parsing = f'\n2) начальная форма: {self.first_parsings.normal_form}'
        self.parsing += '\n3) постоянные признаки: '
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.animacy]}'
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.gender]}'
        if {'Name'} in self.first_parsings or {'Surn'} in self.first_parsings or {'Patr'} in self.first_parsings or {'Geox'} in self.first_parsings or {'Geox'} in self.first_parsings:
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


    def verb(self):# глагол, почему то не работает tens
        self.parsing = '\n1) часть речи: глагол'
        self.parsing = f'\n2) начальная форма: {self.first_parsings.normal_form}'
        self.parsing += '\n3)постоянные признаки: '
        self.parsing += f'\n    {self.sign[self.first_parsings.tag.aspect]}'
        self.parsing += f'\n    {self.sign[self.first_parsings.tag.trns]}'
        self.parsing += '\n3) непостоянные признаки: '
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.mood]}'
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.tens]}'
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.number]}'
        self.parsing += f'\n    {self.signs[self.first.parsing.tag.pers]}'
        if self.first_parsings.tag.tens == 'past' and self.signs[self.first_parsings.tag.number] =='sign':
            self.parsing += f'\n    {self.signs[self.first_parsings.tag.gender]}'
        return self.parsing
    

    def infn(self): #инфнитив, почему то не работает tens
        self.parsing = '\n1) часть речи: глагол'
        self.parsing = f'2) начальная форма: {self.first_parsings.normal_form}'
        self.parsing += '\n3) постоянные признаки: '
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.aspect]}'
        self.parsing += f'\n    {self.signs[self.first_parsings.tag.tens]}'
        if self.first_parsings.tag.refl == None:
            self.parsing+='\n    невозвратный'
        else:
            self.parsing+='\n    возвратный'
        self.parsing += '\n3) непостоянные признаки: \n    инфинитив(неизменяемая форма)'
        return self.parsing


    def grnd(self): #деепричастие, все есть 
        self.parsing ='\n1) часть речи: деепричастие'
        self.parsing = f'2) начальная форма: {self.first_parsings.normal_form}'
        self.parsing += '\nпостоянные признаки: '
        self.parsing += f'{self.sign[self.first_parsings.tag.aspect]}'
        if self.first_parsings.tag.transitivity == 'tran':
            self.parsing += ', переходный, '
        else:
            self.parsing += ', непереходный, '
        if self.first_parsings.tag.refl == None:
            self.parsing+='невозвратный'
        else:
            self.parsing+='возвратный'
        self.parsing+='\nнеизменяемая форма'
        return self.parsing


    def advb(self):#  наречие, нет категории  
        self.parsing += '\nчасть речи: наречие'
        self.parsing += '\nпостоянные признаки: '
        self.parsing += '\nнеизменяемое'
        return self.parsing


    def prtf(self):#  причастие 
        self.parsing += '\nчасть речи: причастие'
        self.parsing += '\nпостоянные признаки: '
        self.parsing += f'{self.signs[self.first_parsings.tag.voic]}'
        self.parsing += f'{self.signs[self.first_parsings.tag.number]}'
        self.parsing += f'{self.signs[self.first_parsings.tag.aspect]}'
        self.parsing += '\nнепостоянные признаки: '
        if self.first_parsings.tag.POS=='PRTS':
            self.parsing += 'краткая форма, '
        else:
            self.parsing += 'полная форма, '
            self.parsing += f'{self.signs[self.first_parsings.tag.case]} падеж, '
        self.parsing += f'{self.signs[self.first_parsings.tag.number]}'
        self.parsing += f'{self.signs[self.first_parsings.tag.gender]}, '
        return self.parsing\

        

word = Morph('бежать')
print(word.parsingq)