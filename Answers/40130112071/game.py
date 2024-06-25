import random

def HopGame():
    print("Hi,Wellcome to HOP GAME")
    print("At first,you shoud choose a factor number:",end='')
    fact=input()
    c=1
    record=[]
    new_record=0
    best_record=0
    ans=""
    yesno="n"
    yn=""
    num=0
    number=0
    first=random.randint(1,10)

    if int(first)%int(fact)==1:
        print("CPU:",end='')
        print(first)

    else:
        first=random.randint(1,10)
        print("CPU:",end='')
        print(first)

    c+=1
    first+=1

    while True:

        if c%2==0:
            print("player:",end='')
            number=input()
            result=int(first)%int(fact)
        
            if result==0 and number=="hop":
                new_record+=1
                record.append(new_record)
                best_record=max(record)
            
            if result==0 and number!="hop":
                ans="you lose"
                print(ans)
                print("Your record:",end='')
                print(new_record)
                print("Best record:",end='')
                print(best_record)
                if yn is not yesno:
                    print("Do you want to play again?y/n:",end='')
                    yn=input()
                    if yn=="y":
                        HopGame()
                    if yn=="n":
                        print("Thank you")                   
        if c%2==1:
                print("CPU:",end='')
                result=int(first)%int(fact)
                num=first
                if result==0:
                    print("hop")

                else:
                    print(num)
    
        c+=1
        first+=1
                
HopGame()                    
    


    
