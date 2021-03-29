

class super:
    python_e = {}
    python_h = {}
    maths_e = {}
    maths_h = {}
    option = {}
    s_user = {}
    def __init__(self,s_id,s_name):
        self.s_id = s_id
        self.s_name = s_name
        print(s_name,'You can set the quiz ')
        
    def setquestion(self):
        while True:
            quiz = input('Do you want to set quiz?(y/n): ')
            if (quiz.lower() == 'y'):
                topic = input('Enter the topic you want to set quiz (python/maths): ')
                difficulty = input('\nEnter the difficulty level (easy/hard): ')
                
                if topic.lower() == 'python'and difficulty.lower() == 'easy':
                    no_of_q = int(input('\nHow many question you want to set: '))
                    for val in range(no_of_q):
                        question = input('\nEnter the question: ')
                        opt = input('\nEnter your option: ').split()
                        super.option[question]=opt
                        answer=input('\nEnter the answer: ')
                        super.python_e[question]=answer
                        
                elif topic.lower() == 'python' and difficulty.lower() == 'hard':
                     no_of_q = int(input('\n how many question you want to set: '))
                     for val in range(no_of_q):
                        question = input('\nEnter the question: ')
                        opt = input('\nEnter your option: ').split()
                        super.option[question]=opt
                        answer=input('\nEnter the answer: ')
                        super.python_h[question]=answer
                        
                elif topic.lower() == 'maths'and difficulty.lower() == 'easy':
                    no_of_q = int(input('\nHow many question you want to set: '))
                    for val in range(no_of_q):
                        question = input('\nEnter the question: ')
                        opt = input('\nEnter your option: ').split()
                        super.option[question]=opt
                        answer=input('\nEnter the answer: ')
                        super.maths_e[question]=answer
                        
                elif topic.lower() == 'maths' and difficulty.lower() == 'hard':
                     no_of_q = int(input('\n how many question you want to set: '))
                     for val in range(no_of_q):
                        question = input('\nEnter the question: ')
                        opt = input('\nEnter your option: ').split()
                        super.option[question]=opt
                        answer=input('\nEnter the answer: ')
                        super.maths_h[question]=answer
                        
            else:
                break
    def add_question(self):
        while True:
            add_q = input('Do you want to add question(y/n): ')
            if add_q.lower()=='y':
                topic = input('Enter the topic where you add question (python/maths): ')
                difficulty = input('\nEnter the difficulty level (easy/hard): ')
                
                
                if topic.lower() == 'python'and difficulty.lower() == 'easy':
                    question = input('\nEnter the question: ')
                    opt = input('\nEnter your option: ').split()
                    super.option[question]=opt
                    answer=input('\nEnter the answer: ')
                    super.python_e[question]=answer
                    
                elif topic.lower() == 'python'and difficulty.lower() == 'hard':
                    question = input('\nEnter the question: ')
                    opt = input('\nEnter your option: ').split()
                    super.option[question]=opt
                    answer=input('\nEnter the answer: ')
                    super.python_h[question]=answer
                    
                if topic.lower() == 'maths'and difficulty.lower() == 'easy':
                    question = input('\nEnter the question: ')
                    opt = input('\nEnter your option: ').split()
                    super.option[question]=opt
                    answer=input('\nEnter the answer: ')
                    super.maths_e[question]=answer
                    
                elif topic.lower() == 'maths'and difficulty.lower() == 'hard':
                    question = input('\nEnter the question: ')
                    opt = input('\nEnter your option: ').split()
                    super.option[question]=opt
                    answer=input('\nEnter the answer: ')
                    super.maths_h[question]=answer
                        
            else:
                break
                