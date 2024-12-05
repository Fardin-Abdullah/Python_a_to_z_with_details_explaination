"One class can contain diffrent characteristics of one or multiple classes what is the differences with inheritance with it"
"Child class contains the characteristics of parent class then if we need we can change in the cild class"
"But in case of composition we can use method of class without inherit the class"
"If B class inherit C class then B is a C and if B doesn't inherit class C just only contain the characteristics of C then we say B has a C"
#Example
#Nonte goods at math
#Monte goods at english
#Fonte goods at science
#Jhoontu goods at bangla
#now if in one term exam jhontu gets highest in bangla,nonte gets highest in math,monte in english,fonte in science
# but parents of jhontu did not ask him the number of bangla but asks all the other subjects number
# now question is parents of Jhontu wants to see as jhontu as which type of student?
# we can use composition to answer this problem
class Jhontu:
    def __init__(self):
        self.n = Nonte()
        self.f = Fonte()
        self.m = Monte()
    def math_marks():
        return self.n.math_marks()
    def english_marks():
        return self.m.english_marks()
    def science_marks():
        return  self.f.science_marks()

j = Jhontu()