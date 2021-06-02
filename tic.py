import random as rd #importing random module.
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
if __name__=="__main__":#main program start from here.
    while not game_over:
        if flag == 0:
            if turn == 'O':
                print(f"{name} turn")
                print("Your flag is - O")
                pos=int(input("Enter your position:"))
            else:
                print("Computer turn")
                pos=rd.randint(1,9)
        elif flag == 1:
            if turn == 'X':
                print(f"{name} turn")
                print("Your flag is - X")
                pos=int(input("Enter your position:"))
            else:
                print("Computer turn")
                pos=rd.randint(1,9)
        if is_empty(pos):
            update(pos,turn)
            draw_board()
            check()
        elif not is_empty(pos) or pos >9:
            print("Invalid move")
        result=winner()
        if result == True:
            print(turn+"-wins!")
            game_over=True
        elif result == "Tie":
            print("It's Tie")
            game_over=True
