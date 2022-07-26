import random

def main():
  '''Start a Scissors-Rock-Paper game'''
  
  '''assign times variable to store the number of times to play the game from a user and use input function to prompt input from a user'''
  times = int(input('How many times you want to play Scissors-Rock-Paper game?'))
  
  '''assign x to zero as counter for times'''
  x = 0
  '''While x counter is less than the number of times that input by the user, getting input from the user and compare to see who is the winner '''
  while x < times:
    player = input('scissor (s), rock (r), or paper (p)?') #get input from user
    if player != 's' and player !='r' and player !='p':  #check only accept s, r, p
        print('You can only enter the option of s or r or p only.') 
        player = input('scissor (s), rock (r), or paper (p)?') 

    chosen = random.randint(1,3)  #chosen variable to store random number of computer from 1 to 3

    if chosen == 1:    #if chosen var stored 1, then it is r=rock
        computer = 'r'
  
    elif chosen == 2:  #if chosen var stored 2, then it is p=paper
        computer = 'p'
  
    else:              #oterwise chosen var stored 3, then it is s=scisors
        computer ='s' 
  
    print(player + ' VS ' + computer) #output display on screen of user input vs computer 

    if player == computer:  #if user input same as computer, then nobody wins the game
        print('Nobody wins!')  

    elif player == 'r' and computer == 's':  #if user input is r=rock against computer s=scisors, then user(player) wins
        print('Player wins!')                

    elif player == 'r' and computer == 'p':  #if user input is r=rock against computer p=paper, then computer wins
        print('Computer wins!')              
  
    elif player == 'p' and computer == 'r':  #if user input is p=paper against computer r=rock, then user(player) wins
        print('Player wins!')                

    elif player == 'p' and computer == 's':  #if user input is p=paper against computer s=scisors, then computer wins
        print('Computer wins!')              
  
    elif player == 's' and computer == 'r':  #if user input is s=scisors against computer r=rock, then computer wins
        print('Computer wins!')              

    elif player == 's' and computer == 'p':  #if user input is s=scisors against computer p=paper, then user(player) wins
        print('Player wins!')                
    
    x +=1           # x counter increased by 1 

    
main()              #call the main function
print ('=== End of the Game! ===' ) #output display on screen of a message of end game
