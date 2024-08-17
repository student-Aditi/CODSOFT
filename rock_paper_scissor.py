import random
def get_computer_choice():
    return random.choice(['rock','paper','scissors'])
def determine_win(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "It is a tie"
    elif(user_choice == 'rock' and computer_choice=='scissors')or \
        (user_choice == 'scissors' and computer_choice=='paper')or \
        (user_choice == 'paper' and computer_choice=='rock'):
        return "You Win!"
    else:
        return "You Lose!"
    
def main():
    user_score =0
    computer_score=0

    while True:
        #get user input
        user_choice=input("Enter your choice (rock,paper or scissors):").lower()
        if user_choice not in['rock','paper','scissors']:
            print("invalid choice!Please choose rock,paper,or scissors")
            continue

        #get computer choice
        computer_choice=get_computer_choice()

        #determine the winner
        result=determine_win(user_choice,computer_choice)

        #display choices and result
        print(f"\nYou Choose:{user_choice}")
        print(f"Computer choose:{computer_choice}")
        print(result)

        #update scores
        if result== "You Win!":
            user_score+=1
        elif result== "You Lose!":
            computer_score+=1
        
        #Display scores
        print(f"Score- You:{user_score},Computer:{computer_score}")

        #ask if user wants to play again
        play_again=input("\nDo you want to play again? (yes/no):").lower()
        if play_again != 'yes':
            break

if __name__=="__main__":
    main()