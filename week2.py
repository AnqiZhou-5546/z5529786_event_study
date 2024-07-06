str1="""John said: "Let's learn Python together"."""
print(str1)
str2='John said: "Let\'s learn Python together".'
print(str2)
f=0.2+0.2
print(f==0.4)
ff=0.2+0.2+0.2#need math library
print(ff==0.6)
print(str1.upper().lower())
print('HI'.center(12,'-'))
print(f'I need {f} a, and {ff} b.')
LENGTH=56
WIDTH=33
HEIGHT=30.5
VOLUME=int(LENGTH)*int(WIDTH)*int(HEIGHT)
print(f'The volume is {VOLUME}')
TEXT='From anqi.zhou@unsw.edu.au Mon Feb 19 10:10:15 2024'
LST=list(TEXT)
DOMAIN=LST[15:26]
print(''.join(DOMAIN))
domain=TEXT.split()[1].split('@')[1]
print(domain)
print("--"*20)
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return(f"{self.name} says: Woof!")

    def get_age(self):
        return self.age

my_dog = Dog("Buddy", 3)
another_dog = Dog("Charlie", 5)

print(my_dog.bark())
print(my_dog.get_age())

third_dog = Dog("lili", 4)
third_dog_bark = third_dog.bark
print(third_dog_bark)

