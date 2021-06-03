import random as rd
def init_board():#initialize board value with blank space.
  values = [0,1,2,3,4,5,6,7,8,9]
  for r in range(1,10):
      values[r] = " "
  return values
def draw_board():#drawing board.
    print(f"\n\t     |     |\n\t  {values[1]}  |  {values[2]}  |  {values[3]}\n\t_____|_____|_____\n\t  {values[4]}  |  {values[5]}  |  {values[6]}\n\t_____|_____|_____\n\t     |     |\n\t  {values[7]}  |  {values[8]}  |  {values[9]}\n\t     |     |")
values=init_board()#calling the function.
draw_board()
game_over = False
turn='X'
name=input("Enter name:")#input name.
flag=int(input("Enter your sign:\nEnter 0 for O:\nEnter 1 for X:"))#input flag.
def is_empty(pos):#check for empty block.
    return values[pos]==" "
def update(p,t):#update block value if it is empty.
    values[p]=t
def get(x):
    return values[x]
def move(a,b,c,t):
    return (get(a)==t and get(b)==t and get(c)==t)
def winner():#checking for winner.
    if move(1,2,3,turn) or move(4,5,6,turn) or move(7,8,9,turn) or move(1,4,7,turn) or move(2,5,8,turn) or move(3,6,9,turn) or move(1,5,9,turn) or move(3,5,7,turn):
        return True
    elif get(1)!=" " and get(2)!=" " and get(3)!=" " and get(4)!=" " and get(5)!=" " and get(6)!=" " and get(7)!=" " and get(8)!=" " and get(9)!=" ":#checking for Tie state.
        return "Tie"
def check():#changing the player turn.
    global turn
    if turn == 'X':
        turn='O'
    else:
        turn='X'
def AI_moves():
    if flag==0 and not turn=='O':
        if values[1]=='O' and values[2]=='O' and values[3]==" ":
            return 3
        elif values[1]=='O' and values[2]==" " and values[3]=='O':
            return 2             
        elif values[1]==" " and values[2]=='O' and values[3]=='O':
            return 1
        elif values[4]=='O' and values[5]=='O' and values[6]==" ":
            return 6
        elif values[4]=='O' and values[5]==" " and values[6]=='O':
            return 5             
        elif values[4]==" " and values[5]=='O' and values[6]=='O':
            return 4
        elif values[7]=='O' and values[8]=='O' and values[9]==" ":
            return 9
        elif values[7]=='O' and values[8]==" " and values[9]=='O':
            return 8             
        elif values[7]==" " and values[8]=='O' and values[9]=='O':
            return 7
        elif values[1]=='O' and values[4]=='O' and values[7]==" ":
            return 7
        elif values[1]=='O' and values[4]==" " and values[7]=='O':
            return 4             
        elif values[1]==" " and values[4]=='O' and values[7]=='O':
            return 1
        elif values[2]=='O' and values[5]=='O' and values[8]==" ":
            return 8
        elif values[2]=='O' and values[5]==" " and values[8]=='O':
            return 5             
        elif values[2]==" " and values[5]=='O' and values[8]=='O':
            return 2
        elif values[3]=='O' and values[6]=='O' and values[9]==" ":
            return 9
        elif values[3]=='O' and values[6]==" " and values[9]=='O':
            return 6             
        elif values[3]==" " and values[6]=='O' and values[9]=='O':
            return 3
        elif values[1]=='O' and values[5]=='O' and values[9]==" ":
            return 9
        elif values[1]=='O' and values[5]==" " and values[9]=='O':
            return 5             
        elif values[1]==" " and values[5]=='O' and values[9]=='O':
            return 1
        elif values[3]=='O' and values[5]=='O' and values[7]==" ":
            return 7
        elif values[3]=='O' and values[5]==" " and values[7]=='O':
            return 5             
        elif values[3]==" " and values[5]=='O' and values[7]=='O':
            return 3
        else:
            return rd.randint(1,9)
    elif flag==1 and not turn=='X':
        if values[1]=='X' and values[2]=='X' and values[3]==" ":
            return 3
        elif values[1]=='X' and values[2]==" " and values[3]=='X':
            return 2             
        elif values[1]==" " and values[2]=='X' and values[3]=='X':
            return 1
        elif values[4]=='X' and values[5]=='X' and values[6]==" ":
            return 6
        elif values[4]=='X' and values[5]==" " and values[6]=='X':
            return 5             
        elif values[4]==" " and values[5]=='X' and values[6]=='X':
            return 4
        elif values[7]=='X' and values[8]=='X' and values[9]==" ":
            return 9
        elif values[7]=='X' and values[8]==" " and values[9]=='X':
            return 8             
        elif values[7]==" " and values[8]=='X' and values[9]=='X':
            return 7
        elif values[1]=='X' and values[4]=='X' and values[7]==" ":
            return 7
        elif values[1]=='X' and values[4]==" " and values[7]=='X':
            return 4             
        elif values[1]==" " and values[4]=='X' and values[7]=='X':
            return 1
        elif values[2]=='X' and values[5]=='X' and values[8]==" ":
            return 8
        elif values[2]=='X' and values[5]==" " and values[8]=='X':
            return 5             
        elif values[2]==" " and values[5]=='X' and values[8]=='X':
            return 2
        elif values[3]=='X' and values[6]=='X' and values[9]==" ":
            return 9
        elif values[3]=='X' and values[6]==" " and values[9]=='X':
            return 6             
        elif values[3]==" " and values[6]=='X' and values[9]=='X':
            return 3
        elif values[1]=='X' and values[5]=='X' and values[9]==" ":
            return 9
        elif values[1]=='X' and values[5]==" " and values[9]=='X':
            return 5             
        elif values[1]==" " and values[5]=='X' and values[9]=='X':
            return 1
        elif values[3]=='X' and values[5]=='X' and values[7]==" ":
            return 7
        elif values[3]=='X' and values[5]==" " and values[7]=='X':
            return 5             
        elif values[3]==" " and values[5]=='X' and values[7]=='X':
            return 3
        else:
            return rd.randint(1,9)
if __name__=="__main__":#main program start from here.
    while not game_over:
        if flag == 0:
            if turn == 'O':
                print(f"{name} turn")
                print("Your flag is - O")
                pos=int(input("Enter your position:"))
            else:
                print("Computer turn")
                pos=AI_moves()
        elif flag == 1:
            if turn == 'X':
                print(f"{name} turn")
                print("Your flag is - X")
                pos=int(input("Enter your position:"))
            else:
                print("Computer turn")
                pos=AI_moves()
        if is_empty(pos):
            update(pos,turn)
            draw_board()
            check()
        elif not is_empty(pos) or pos >9:
            print("Invalid move")
        result=winner()
        if result == True:
            if (flag==0 and turn=='O') or(flag==1 and turn=='X'):
                print(f"{name} -wins!")
            else:
                print("Computer -wins!")
            game_over=True
        elif result == "Tie":
            print("It's Tie")
            game_over=True
