

from super import super


class user:
    user = {}
    marks = 0
    def __init__(self,id_no,name):
        self.id_no = id_no
        self.name = name
        
    def startquiz(self):
        choose = input('\n\nEnter you want to take quiz (python/maths): ')
        level = input('\nEnter the difficulty level you want (easy/hard): ')
        if choose.lower() == 'python' and level.lower() == 'easy':
            for val in super.python_e:
                print(val)
                for i in range(len(super.option[val])):
                    print(str(i+1)+")",super.option[val][i])
                ans = input()
                if super.python_e[val] == ans:
                    user.marks+=1
                    user.user[self.id_no]=user.marks
                    
        elif  choose.lower() == 'python' and level.lower() == 'hard':
              for val in super.python_h:
                print(val)
                for i in range(len(super.option[val])):
                    print(str(i+1)+")",super.option[val][i])
                ans = input()
                if super.python_h[val] == ans:
                    user.marks+=1
                    user.user[self.id_no]=user.marks
         
        elif choose.lower() == 'maths' and level.lower() == 'easy':
            for val in super.maths_e:
                print(val)
                for i in range(len(super.option[val])):
                    print(str(i+1)+")",super.option[val][i])
                ans = input()
                if super.maths_e[val] == ans:
                    user.marks+=1
                    user.user[self.id_no]=user.marks
                    
        elif  choose.lower() == 'maths' and level.lower() == 'hard':
              for val in super.maths_h:
                print(val)
                for i in range(len(super.option[val])):
                    print(str(i+1)+")",super.option[val][i])
                ans = input()
                if super.maths_h[val] == ans:
                    user.marks+=1
                    user.user[self.id_no]=user.marks
                    
    def result(self):
        res = int(input('Enter id_no. : '))
        print(self.name,'scored',user.user[res],'marks')
        user.marks = 0
        print('\nCorrect option:')
        for val in super.python_e.values():
            print(val)
        for val in super.python_h.values():
            print(val)
        for val in super.maths_e.values():
            print(val)
        for val in super.maths_h.values():
            print(val)
        