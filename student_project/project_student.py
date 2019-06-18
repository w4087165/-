import random
class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value
l = []
for  i in range(3):
    s = Student("闫少甫",18,random.randint(1,100))
    l.append(s)

print(l)
ll = [5,6,8,4,1,2,3]
sorted(ll)

print(ll)
def get_Student_score(x):
    print(x.score)
    return x.score
l = sorted(l,key=get_Student_score)

