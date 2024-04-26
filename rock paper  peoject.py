import random
choice=["rock","papper","scissor"]
while True:
    print("rock paper scissor game:")
    youwin,computerwin=0,0
    for i in range(1,6):
        print("round",i,"start:")
        print("please select any one option:")
        print("1.rock","2.paper","3.scissor",sep="\n")
        yourchoice=int(input())
        if yourchoice==1:
            print("you select rock")
            yourchoice="rock"
        elif yourchoice==2:
            print("you select paper")
            yourchoice="paper"
             
        elif yourchoice==3:
                print("you select scissor")
                yourchoice="scissor"
                print("invalid choice")
                break

                computerchoice=random.choice(choice)
                print("computer select:",computerchoice)

                if yourchoice==computerchoice:
                    youwin+=1
                    computerwin+=1
                    print("this round is drawn:")
                elif(yourchoice=="paper"and computerchoice=="rock") or (yourchoice=="scissor") or (yourchoice=="paper"):
                        youwin+=1
                        print("you win this round")
                else:
                            computerwin+=1
                            print("computer win this round")
                    
                

