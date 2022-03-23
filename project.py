import numpy as np
import pygame 
import sys
import math
BLUE = (0,100,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
ROW_COUNT = 6
COLUMN_COUNT =7
def create_board():
    b = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return b
def drop_piece(b,row,col,piece):
    b[row][col] = piece
    
def is_valid_location(b,col):
    return b[ROW_COUNT -1][col] == 0
def get_next_open_row(b,col):
    for r in range(ROW_COUNT):
        if b[r][col] == 0:
            return r
def print_board(b):
	print(np.flip(b,0))  
def draw_board(b):
    for c in range(COLUMN_COUNT):
        for r in range (ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQURESIZE, r*SQURESIZE +SQURESIZE,SQURESIZE,SQURESIZE))
            pygame.draw.circle(screen, BLACK,(int(c*SQURESIZE +SQURESIZE/2),int(r*SQURESIZE+SQURESIZE+SQURESIZE/2)),RADIUS)
    for c in range(COLUMN_COUNT):
        for r in range (ROW_COUNT):       
            if b[r][c] == 1:
                pygame.draw.circle(screen, RED,(int(c*SQURESIZE +SQURESIZE/2),height-int(r*SQURESIZE+SQURESIZE/2)),RADIUS)
            elif b[r][c] == 2:
                pygame.draw.circle(screen, YELLOW,(int(c*SQURESIZE +SQURESIZE/2),height -int(r*SQURESIZE+SQURESIZE/2)),RADIUS)
    pygame.display.update()
          
def winning_move(b,piece):
    for c in range(COLUMN_COUNT -3):
        for r in range(ROW_COUNT):
            if b[r][c] == piece and b[r][c+1] == piece and b[r][c+2] == piece and b[r][c+3] == piece :
                return True
    for c in range(COLUMN_COUNT ):
        for r in range(ROW_COUNT -3):
            if b[r][c] == piece and b[r+1][c] == piece and b[r+2][c] == piece and b[r+3][c] == piece :
                return True 
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if b[r][c] == piece and b[r+1][c+1] == piece and b[r+2][c+2] == piece and b[r+3][c+3] == piece :
                return True       
    for c in range(COLUMN_COUNT -3):
        for r in range(3,ROW_COUNT -3):
            if b[r][c] == piece and b[r-1][c+1] == piece and b[r-2][c+2] == piece and b[r-3][c+3] == piece :
                return True       
            
b = create_board()
print_board(b)    
game_over = False
turn = 0
pygame.init()
SQURESIZE =100
width = COLUMN_COUNT * SQURESIZE
height = (ROW_COUNT +1)* SQURESIZE
size = (width,height)
RADIUS = int(SQURESIZE/2 - 5)
screen = pygame.display.set_mode(size)
draw_board(b)
pygame.display.update()
while not game_over:
    for event in pygame.event.get():
       if event.type ==pygame.QUIT:
           sys.exit()

       if event.type == pygame.MOUSEMOTION:
           pygame.draw.rect(screen, BLACK, (0,0,width,SQURESIZE))
           
           posx =event.pos[0]
           if turn == 0:
               pygame.draw.circle(screen,RED,(posx,int(SQURESIZE/2)),RADIUS)
           else :
               pygame.draw.circle(screen,YELLOW,(posx,int(SQURESIZE/2)),RADIUS)
           pygame.display.update()    
       if event.type == pygame.MOUSEBUTTONDOWN:
           
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQURESIZE))
                
                
                #col = int(input("player 1 make your selection (0-6) :"))
                if is_valid_location(b, col):
                    row = get_next_open_row(b, col)
                    drop_piece(b, row, col, 1)
                if winning_move(b,1):
                    print("player 1 wins !!!! congrats !!!")
                    game_over = True 
            else :
                posx = event.pos[0]
                col = int(math.floor(posx/SQURESIZE))
                
                    #col = int(input("player 2 make your selection (0-6) :"))
                if is_valid_location(b, col):
                    row = get_next_open_row(b, col)
                    drop_piece(b, row, col, 2)
                if winning_move(b,2):
                    print("player 2 wins !!!! congrats !!!")
                    game_over = True  
            print_board(b)    
            draw_board(b)    
            #print(b)       
            turn +=1
            turn = turn % 2         
    
            
    