import random
Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
win = int()
draw = int()
lose = int()
print('Welcome to Rock Paper Scissors Game..!!!')
play = int(input('How Many times wants to play the game : \n'))

while play > 0:
    gamer = int(input('What do you choose ? Type 0 for Rock , 1 for Paper, 2 for Scissors : \n'))
    computer = ['Rock','Paper','Scissors']
    if gamer == 0:
        print("Rock\n", Rock)
        c1 = (random.choice(computer))
        if c1 == "Scissors":
            print("Scissors\n", Scissors)
            print('you win')
            win += 1
        elif c1 == "Rock":
            print("Rock\n", Rock)
            print('you draw')
            draw += 1
        elif c1 == "Paper":
            print('Paper\n', Paper)
            print('you lose')
            lose += 1
    elif gamer == 1:
        print('Paper\n', Paper)
        c2 = (random.choice(computer))
        if c2 == "Rock":
            print("Rock\n", Rock)
            print('you win')
            win += 1
            # print('Your Score', score)
        elif c2 == "Scissors":
            print("Scissors\n", Scissors)
            print('you lose')
            lose += 1
        elif c2 == "Paper":
            print("Paper\n", Paper)
            print('you draw')
            draw += 1
    elif gamer == 2:
        print("Scissors\n", Scissors)
        c3 = (random.choice(computer))
        if c3 == "Paper":
            print("Paper\n", Paper)
            print('you win')
            win += 1
            # print('Your Score', score)
        elif c3 == "Scissors":
            print("Scissors\n", Scissors)
            print('you draw')
            draw += 1
        elif c3 == "Rock":
            print("Rock\n", Rock)
            print('you lose')
            lose += 1
    else:
        print("Entered wrong number, Please Type 0 for Rock , 1 for Paper, 2 for Scissors : \n ")

    play -= 1
print(f"\nYour overall score is : win = {win}, draw = {draw}, lose = {lose}")