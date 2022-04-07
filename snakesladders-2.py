## Created by - Shashank Kawatra
## Date - 5 April 2022
## Snakes and Ladders Sample

import pandas as pd
import numpy as np

def diceRoll():
  dice = np.random.randint(1,7)
  return dice


def playersTurn(pos,dice,gsize,dh,ph,player):
  status=0
  if pos+dice <= gsize:
    pos = pos+dice
    dh.append(dice)
    ph.append(pos)
    df.at[player-1,'Dice Roll History'] = dh
    df.at[player-1,'Position History'] = ph
    if pos == gsize:
      status = 1
      df.at[player-1,'Win Status'] = 1
  return status, pos


a = int(input('Enter Grid Size - '))
gsize = a*a
print("\nPlayer to reach",gsize,"will win this game\n")
#initializing players
p1 = 0
dh1 = []
ph1 = []

p2 = 0
dh2 = []
ph2 = []

p3 = 0
dh3 = []
ph3 = []

p4 = 0
dh4 = []
ph4 = []

curPlayer = 1

df = pd.DataFrame(columns = ['Players','Dice Roll History','Position History','Win Status'])
df['Players'] = ['Player 1','Player 2', 'Player 3', 'Player 4']
df['Win Status'] = 0
status = 0

while not status:
  dice = diceRoll()
  if curPlayer == 1:
    status,p1 = playersTurn(p1,dice,gsize,dh1,ph1,curPlayer)
    curPlayer = 2

  elif curPlayer == 2:
    status,p2 = playersTurn(p2,dice,gsize,dh2,ph2,curPlayer)
    curPlayer = 3

  elif curPlayer == 3:
    status,p3 = playersTurn(p3,dice,gsize,dh3,ph3,curPlayer)
    curPlayer = 4

  else:
    status,p4 = playersTurn(p4,dice,gsize,dh4,ph4,curPlayer)
    curPlayer = 1

print(df,"\n")