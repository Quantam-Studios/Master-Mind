import random
from colorama import Fore, Back, Style
#methods
code = []
def genRandNumbers():
  for i in range(0, 4):
    code.append(random.randrange(1, 9))
x = 0
comparedList = []
def checkAnswerNum(answer):
  global x
  x = 0
  comparedList.clear()
  for i in range(0, len(code)):
    if code[i] == answer[i]:
      x += 1
      comparedList.append("Right")
    else:
      comparedList.append("Wrong")
  if x == 4:
    return True
  else:
    print("Here's a little something to help!")
    print(f"{Fore.LIGHTYELLOW_EX}" + str(comparedList))
    return False

# style for colors
colorCode = [f"{Fore.RED}", f"{Fore.GREEN}", f"{Fore.LIGHTYELLOW_EX}", f"{Fore.BLUE}", f"{Fore.MAGENTA}", f"{Fore.CYAN}", f"{Fore.WHITE}"]
colors = ['red', 'green', 'yellow', 'blue', 'pink', 'cyan', 'white']
def genRandColors():
  for i in range(0, 4):
    col = random.randrange(0, len(colors))
    code.append(colors[col])
c = 0
def checkAnswerCol(answer):
  global c
  c = 0
  comparedList.clear()
  for i in range(0, 4):
    if code[i] == answer[i]:
      c += 1
      comparedList.append("Right")
    else:
      comparedList.append("Wrong")  
  if c == 4:
    return True
  else:
    print("Here's a little something to help!")
    print(f"{Fore.LIGHTYELLOW_EX}" + str(comparedList))
    return False
# run time stuff
tries = 10
while True:
  for n in range(0, len(code)):
    code.clear()
  r = input(Style.RESET_ALL + "Type 'play' to begin: ")
  if r == 'play':
    mode = input("Type 'c' to play with colors or type 'n' for numbers: ")
    if mode == 'c':
      # color mode
      print(Style.RESET_ALL + "Hi there user I have made a code that I bet you can't crack!\nHowever if you can I will tell the meaning of life itself... \nSomething that you humans have been trying to do since the dawn of humanity.\nWell anyways the code has been made and it's 4 colors you have " + str(tries) + " to guess the colors, and in the right order. \nGoodluck!")
      print("The list of colors you can guess are: ")
      z = 0
      for c in colors:
        print(colorCode[z] + c)
        z += 1
      genRandColors()
      for n in range(0, tries):
        answer = []
        i = 0
        while i < len(code):
          ans = input("What is your guess? (type 1 color): ")
          if ans == "-cheat":
            print(Style.RESET_ALL + "How'd you figure that out!\n Seriously who taught you that!\n Well fine here it is...")
            print(Back.RED + str(code))
          else: 
            answer.append(ans)
            i += 1
        check = checkAnswerCol(answer)
        if check == True:
          print(Style.RESET_ALL + "You gussed it correctly!\nNow for your well deserved reward!\n The meaning of life is really quite a simple thing.\nSilly humans overthinking such a trivial thing.\n Anyways... the meaning of life is simply " + Fore.LIGHTYELLOW_EX + '42')
          break;
        else:
          tries -= 1
          print(Style.RESET_ALL + "You got " + str(c) + " colors right!" + "\nYou have " + str(tries) + " remaining guesses.")
    elif mode == 'n':
      # number mode
      # get random code
      genRandNumbers()
      print(Style.RESET_ALL + "Hi there user I have made a code that I bet you can't crack!\nHowever if you can I will tell the meaning of life itself... \nSomething that you humans have been trying to do since the dawn of humanity.\nWell anyways the code has been made and it's 4 digits you have " + str(tries) + " to guess the numbers, and in the right order. \nGoodluck!")
      for n in range(0, tries):
        answer = []
        i = 0
        while i < len(code):
          ans = input(Style.RESET_ALL + "Whats your guess? (Type a single digit between 1-9): ")
          if ans == "-cheat":
            print(Style.RESET_ALL + "How'd you figure that out!\n Seriously who taught you that!\n Well fine here it is...")
            print(Back.RED + str(code))
          else:  
            answer.append(int(ans))
            i += 1
        check = checkAnswerNum(answer)
        if check == True:
          print(Style.RESET_ALL + "You gussed it correctly!\nNow for your well deserved reward!\n The meaning of life is really quite a simple thing.\nSilly humans overthinking such a trivial thing.\n Anyways... the meaning of life is simply " + Fore.LIGHTYELLOW_EX + '42')
          break;
        else:
          tries -= 1
          print(Style.RESET_ALL + "You got " + str(x) + " numbers right!" + "\nYou have " + str(tries) + " remaining guesses.")



