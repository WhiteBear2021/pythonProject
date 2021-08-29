class Person:
    def __init__(self,param_name):
        print("i am created!!",self)
        self.name=param_name
    
    def talk(self):
        print("안녕하세요 제 이름은",self.name," 입니다")

person_01=Person("유재석")
print(person_01)
print(person_01.name)
person_01.talk()
