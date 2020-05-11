# print("I'm Shotaro")

def kisuu_or_gusuu(num):
    if num % 2 == 0:
        print('偶数です。')
    else:
        print('奇数です')
    

def tree(num):
    if num % 3 == 0:
        print('3の倍数です')
    else:
        print('3の倍数ではありません')

num = input('>>>')

if int(num) % 3 == 0:
    print(num + ':' +'3の倍数です')
else:
    print('3の倍数ではありません')

class Shotaro:

    human = True
    age = 21

    def __init__(self, name):
        self.name = name
    
    def names(self):
        print('私の名前は' + self.name + 'です' + '私の年齢は' + self.age + 'です')


human = Shotaro()
human.name('Shotaro OOki')
human.age