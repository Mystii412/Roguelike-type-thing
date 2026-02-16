import random
import os

def clear():
    # 'nt' is for Windows, 'posix' is for macOS and Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def print_map(map, map_size):
  """Takes map_size and draws the map based on the size."""
  if map_size == 4:
    print(f'     {map[0]}\n    /  \\\n  {map[1]}    {map[2]}\n    \\  /\n     {map[3]}')  
  elif map_size == 7:
    print(f'     {map[0]}\n    /  \\\n  {map[1]}    {map[2]}\n    \\  /\n     {map[3]}\n    /  \\\n   {map[4]}  {map[5]}\n    \\  /\n     {map[6]}')
  elif map_size == 10:
    print(f'     {map[0]}\n    /  \\\n  {map[1]}    {map[2]}\n    \\  /\n     {map[3]}\n    /  \\\n   {map[4]}  {map[5]}\n    \\  /\n     {map[6]}\n    /  \\\n   {map[7]}  {map[8]}\n    \\  /\n     {map[9]}')
  

def define_map(map_size):
  """Creates emoji icons for different space types based on random choice and appends them to the 'map' list."""
  i = 1
  map = ['🔻']
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

def main():
  print('This is for testing the node map type')
  while True:
    size = input('What map size would you like?  [small, medium, large]').strip().lower()
    if size == 'small':
      map_size = 4
      break
    elif size == 'medium':
      map_size = 7
      break
    elif size == 'large':
      map_size = 10
      break
    else:
      print('that\'s not an option cuh.')
  print()
  map = define_map(map_size)
  print_map(map, map_size)


if __name__ == "__main__":
  main()
