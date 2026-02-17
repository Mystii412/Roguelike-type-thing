import random
import os

player_location = 0
player = '🔻'

def clear():
    # 'nt' is for Windows, 'posix' is for macOS and Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def print_map(og_map, map_size):
  """Takes map_size and draws the map based on the size."""
  global player_location, player
  map = og_map
  if map_size == 4:
    map[player_location] = player
    print(f'     {map[0]}\n    /  \\\n   {map[1]}   {map[2]}\n    \\  /\n     {map[3]}')  
  elif map_size == 7:
    map[player_location] = player
    print(f'     {map[0]}\n    /  \\\n   {map[1]}   {map[2]}\n    \\  /\n     {map[3]}\n    /  \\\n   {map[4]}  {map[5]}\n    \\  /\n     {map[6]}')
  elif map_size == 10:
    map[player_location] = player
    print(f'     {map[0]}\n    /  \\\n   {map[1]}   {map[2]}\n    \\  /\n     {map[3]}\n    /  \\\n   {map[4]}  {map[5]}\n    \\  /\n     {map[6]}\n    /  \\\n   {map[7]}  {map[8]}\n    \\  /\n     {map[9]}')
  

def define_map(map_size):
  """Creates emoji icons for different space types based on random choice and appends them to the 'map' list."""
  i = 0
  map = []
  while i < map_size:
    power = random.randint(1,3)
    if power == 1:
      icon = '⚔'
    elif power == 2:
      icon= '⛺'
    elif power == 3:
      icon = '🪙'
    map.append(icon)
    i += 1
  return map

def movement_check(map, map_size):
  """Checks where the player can move, and asks for input to move there"""
  global player_location
  if player_location % 3 == 0:  
      while True:
        move = input('Where would you like to move? (L)eft (R)ight\n>').strip().lower()
        if move == 'l':
          print('You moved left yay')
          map[player_location] = '⚫'
          player_location += 1
          clear()
          print_map(map, map_size)
          break
        elif move == 'r':
          print('You moved right yay')
          map[player_location] = '⚫'
          player_location += 2
          clear()
          print_map(map,map_size)
          break
        else:
          print('invalid input')
  elif player_location % 3 == 1:
    map[player_location] = '⚫'
    player_location += 2
    input('>')
    clear()
    print_map(map, map_size)
  elif player_location % 3 == 2:
    map[player_location] = '⚫'
    player_location += 1
    input('>')
    clear()
    print_map(map, map_size)


def main():
  global player_location
  print('This is for testing the node map type')
  while True:
    size = input('What map size would you like?  [small, medium, large]\n>').strip().lower()
    if size == 'small':
      print('Small map chosen')
      clear()
      map_size = 4
      break
    elif size == 'medium':
      print('Medium map chosen')
      clear()
      map_size = 7
      break
    elif size == 'large':
      print('Large map chosen')
      clear()
      map_size = 10
      break
    else:
      print('that\'s not an option cuh.')
  print()
  map = define_map(map_size)
  true_map = list(map)
  print_map(map, map_size)
  
  
  while player_location < map_size -1:
    movement_check(map, map_size)
    if true_map[player_location] == '⚔':
      print('Fight space')
    elif true_map[player_location] == '🪙':
      print('Treasure space')
    elif true_map[player_location] == '⛺':
      print('Rest space')
    


if __name__ == "__main__":
  main()
