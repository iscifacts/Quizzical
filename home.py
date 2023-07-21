# import the time module
import threading
import time


def countdown(t):
	
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1 
def start_timer(duration):
    print(f"The timer has started for {duration} seconds.")
    print()
    time.sleep(duration)
    print("Time's up!")
       
            
def display_question(Round_1,name,duration):
    timer_thread = threading.Thread(target=start_timer, args=(duration,))
    timer_thread.start()
    print()
    correct=0
    incorrect=0
    start_time=time.time()
    for i in range(0,len(Round_1)):
         question=Round_1[i]
         print("\n")
         print("->",i+1,question[0])

         print(f"1.{question[1]}")                  
         print(f"2.{question[2]}")
         print(f"3.{question[3]}")                  
         print(f"4.{question[4]}")
         print()
         print("If you want to close the quiz Press 0")
         print()
         ans=int(input("Enter your choice from(1-4): "))
         if(ans==answers[i]):
           print("You're crushing it! That's the correct answer!")
           print("your answer is correct")
           correct=correct+1
          
           
         elif(ans!=answers[i]):
           print("Saddening , Not the Right answer. ")
           print("Better luck next time :)")
           incorrect=incorrect+1
         end_time=time.time() 
         time_taken=  end_time-start_time
         if time_taken>duration:
               print("Time is up!!") 
               return
         else:
           print(f"Congratulation !! you have completed the quiz on {time_taken} seconds")
           
    print()
    print(f"{name} Your score is :) ",correct)
    print()
    print(f"Correct answers are ",correct,"out of ",len(Round_1))
    print(f"Your incorrect answers are ",incorrect ," out of ",len(Round_1))
    if correct==5:
         print(f"       You've proven yourself as the ultimate quiz master! Congratulations {name}         ")
    print("If you want to play Quiz Again!!!")
    print("Press 9")   
    again=int(input())
    if again==9:
         print("starting the Quiz again")
         display_question(Round_1,name,60)
         print("Welcome to Quizzical Again!!")
         print("Your quiz starts Now")
        

print('Fire in the hole!')
    

#--------------------------Quiz-------------------

print("               WELCOME TO QUIZZICAL!          ")
#----------Name------------
name=input("Enter your Name: ")
name=name.upper()
print(f"                                        Hello {name}!.                       ")

print()
print("         Welcome to our thrilling quiz project, where knowledge and excitement intersect! ")
print("         Get ready to embark on an intellectual journey filled with intriguing questions, mind-boggling challenges, and an abundance of fun!!")      
print()

#--------Rules------------
print("                        -------------------RULES------------------             ")
print("1.You will get only one chance to answer each question.")
print("2.You will get 60 seconds for the quiz")
print("3.There are total 5 question")
print("You will get one point for correct answer and 0 point for incorrect answers.")
print()
print()
#----------------questions-----------------------
Round_1=[
    [
        "Which of the following traits is associated with effective leadership?","Empathy"," Timidity"," Inflexibility","Micro-management"
    ],
    [
        "What does the term proactive mean?","Reacting to situations after they occur","Taking initiative and anticipating future events","Avoiding conflicts and challenges","Following instructions without question"
    ],
    [
        "Which of the following is an example of good time management?","Working on multiple tasks simultaneously without prioritizing","Constantly checking social media during work hours","Setting clear goals and deadlines for tasks","Procrastinating until the last minute and then rushing to complete tasks"
    ],
    [
        "What does the term adaptability refer to?","Sticking to established routines and processes","Avoiding change and new challenges","Being open to new ideas and adjusting to different situations","Being resistant to feedback and suggestions"
    ],
    [
        "Which of the following is a characteristic of effective teamwork?","Dominating conversations and ignoring others' input"," Lack of communication and collaboration"," Active listening and valuing diverse perspectives","Assigning blame and criticizing team members"
    ],
]
answers=[1,2,3,3,3]
correct=0
incorrect=0
print(f"So your Quiz Starts Now")
print("If you are Ready to Start Quiz then Press 1 otherwise Press 0")
choice=int(input())
if(choice==1):
    start_time=time.time()
    display_question(Round_1,name,60)
else:
     print("Exit Quiz!!!!")   

            
                    


    






    
    
    

    