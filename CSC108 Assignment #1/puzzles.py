# Code for working with word search puzzles
#
# Do not modify the existing code
#
# Complete the tasks below marked by *task*


PUZZLE1 = '''
rmhlzxceuq
bxmichelle
mnnejluapv
caellehcim
xdydanagbz
xinairbprr
vctzevbkiz
jgfavqwjan
quotjenhna
iumxddbxnd
'''

PUZZLE2 = '''
foigudgctrycmtchdfay
tljellehcimlprplbuia
vumskwxaayeqpkgrrmvx
dapqgluapnnkwzbeidan
jpjmhyelpaulwaamalyz
xfypsdvnairbdppinkuu
ropzkallrshypyactlme
dpkoynwcebnjueuhgnnl
bitbqxdossqscbleubiw
snrphrktfwigvjclheyj
jkbpwapaulhtrotlhqzb
ogbhhwpgjqwmtvfejzzu
'''

def rotate_puzzle(puzzle):
  '''(str) -> str
  Return the puzzle rotated 90 degrees to the left.
  '''
  
  raw_rows = puzzle.split('\n')
  rows = []
  # if blank lines or trailing spaces are present, remove them
  for row in raw_rows:
    row = row.strip()
    if row:
      rows.append(row)
  
  # calculate number of rows and columns in original puzzle
  num_rows = len(rows)
  num_cols = len(rows[0])
    
  # an empty row in the rotated puzzle
  empty_row = [''] * num_rows
    
  # create blank puzzle to store the rotation
  rotated = []
  for row in range(num_cols):
    rotated.append(empty_row[:])
  
  # rotate the puzzle
  for x in range(num_rows):
    for y in range(num_cols):
      rotated[y][x] = rows[x][num_cols - y - 1]
  
  # construct new rows from the lists of rotated
  new_rows = []
  for rotated_row in rotated:
    new_rows.append(''.join(rotated_row))
  
  rotated_puzzle = '\n'.join(new_rows)
  
  return rotated_puzzle
  
def lr_occurrences(puzzle, word):
  '''(str, str) -> int
  Return the number of times word is found in puzzle in the 
  left-to-right direction only.
  
  >>> lr_occurrences('xaxy\nyaaa', 'xy')
  1
  '''
  return puzzle.count(word)


# ---------- Your code to be added below ----------

# *task* 3: write the code for the following function.
# We have given you the header, type contract, example, and description.

def total_occurrences (puzzle, word):
  '''(str, str) -> int
  Return total occurrences of word in puzzle.
  All four directions are counted as occurrences:
  left-to-right, top-to-bottom, right-to-left, and bottom-to-top.
  
  >>> total_occurrences('xaxy\nyaaa', 'xy')
  2
  '''
  total = lr_occurrences (puzzle,word) #left-to-right
  total = total + lr_occurrences (rotate_puzzle (puzzle),word) #top-to-bottom
  total = total + lr_occurrences (rotate_puzzle (rotate_puzzle (puzzle)),word) #right-to-left
  total = total + lr_occurrences (rotate_puzzle (rotate_puzzle (rotate_puzzle (puzzle))),word) #bottom-to-top
  return total

# *task* 5: write the code for the following function.
# We have given you the function header only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.

def in_puzzle_horizontal (puzzle, word):
  '''(str, str) -> bool
  Return true iff word is found in puzzle in the left-to-right direction
  or right-to-left direction or both.

  >>> in_puzzle_horizontal ('xaxy\nyaaa', 'xy')
  True
  '''
  return lr_occurrences (puzzle,word) > 0 or lr_occurrences (rotate_puzzle(rotate_puzzle(puzzle)), word)  > 0

# *task* 8: write the code for the following function.
# We have given you the function header only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.

def in_puzzle_vertical (puzzle, word):
    '''(str, str) -> bool
  Return true iff word is found in puzzle in the top-to-bottom direction
  or bottom-to-top direction or both.

  >>> in_puzzle_vertical ('xaxy\nyaaa', 'xy')
  True
  '''
    return lr_occurrences (rotate_puzzle(puzzle), word) > 0 or lr_occurrences (rotate_puzzle (rotate_puzzle (rotate_puzzle (puzzle))), word) > 0

# *task* 9: write the code for the following function.
# We have given you the function header only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.

def in_puzzle (puzzle, word):
   '''(str, str) -> bool
  Return true iff word is found anywhere in puzzle in at least
  one of the four directions.

  >>> in_puzzle ('xaxy\nyaaa', 'xy')
  True
  '''
   return in_puzzle_vertical (puzzle,word) or in_puzzle_horizontal (puzzle,word)


# *task* 10: write the code for the following function.
# We have given you only the function header.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.

def in_exactly_one_dimension (puzzle, word):
     '''(str, str) -> bool
  Return true iff word is found in puzzle in exactly
  one of the two directions (horizontal or vertical) but not both.

  >>> in_puzzle ('xaxy\nyaaa', 'xy')
  False
  '''
     return not (in_puzzle_vertical (puzzle,word) and in_puzzle_horizontal (puzzle,word))

# *task* 11: write the code for the following function.
# We have given you only the function header.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.

def all_horizontal (puzzle, word):
     '''(str, str) -> bool
  Return true iff all occurrences of word are horizontal,
  if word is not in puzzle, true is returned.

  >>> in_puzzle ('xaxy\naabb', 'xy')
  True
  '''
     return not in_puzzle_vertical (puzzle,word)

# *task* 12: write the code for the following function.
# We have given you only the function header.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.

def at_most_one_vertical (puzzle, word):
     '''(str, str) -> bool
  Return true iff word occurs at most once in the puzzle
  and that occurrence (if present) is vertical. 

  >>> in_puzzle ('xaxy\nyaaa', 'xa')
  True
  '''
     return (not in_puzzle_horizontal (puzzle, word)) and (lr_occurrences (rotate_puzzle(puzzle), word) == 1 or lr_occurrences (rotate_puzzle (rotate_puzzle (rotate_puzzle (puzzle))), word) == 1)
    
def do_tasks (puzzle, name):
  '''(str, str) -> NoneType
  puzzle is a word search puzzle and name is a word.
  Carry out the tasks specified here and in the handout.
  '''

  # *task* 1a: add a print call below the existing one to print
  # the number of times that name occurs in the puzzle left-to-right.
  # Hint: one of the two starter functions defined above will be useful.

  print ('Number of times', name, 'occurs left-to-right: ', end='')
  print (lr_occurrences (puzzle,name)) #left-to-right
  
  # *task* 1b: add code that prints the number of times
  # that name occurs in the puzzle top-to-bottom.
  # Hint: both starter functions are going to be useful this time!

  print ('Number of times', name, 'occurs top-to-bottom: ', end='')
  print (lr_occurrences (rotate_puzzle (puzzle), name)) #top-to-bottom
  
  # *task* 1c: add code that prints the number of times
  # that name occurs in the puzzle right-to-left.
  
  print ('Number of times', name, 'occurs right-to-left: ', end='')
  print (lr_occurrences (rotate_puzzle (rotate_puzzle (puzzle)), name)) #right-to-left

  # *task* 1d: add code that prints the number of times
  # that name occurs in the puzzle bottom-to-top.
  
  print ('Number of times', name, 'occurs bottom-to-top: ', end='')
  print (lr_occurrences (rotate_puzzle (rotate_puzzle (rotate_puzzle (puzzle))), name)) #bottom-to-top
  
  # *task* 4: print the results of calling total_occurrences on puzzle and name.
  # Add only one line below. 
  # Your code should print a single number, nothing else.
  print (total_occurrences (puzzle,name))

  # *task* 6: print the results of calling in_puzzle_horizontal on puzzle and name.
  # Add only one line below. The code should print only True or False.
  print (in_puzzle_horizontal (puzzle, name))


# *task* 2: call do_tasks on PUZZLE1 and 'paul'.`
# Your code should work on 'paul' with no other changes made.
# If it doesn't work, check your code in do_tasks.
# Hint: you shouldn't be using 'dan' anywhere in do_tasks.

do_tasks (PUZZLE1, 'dan')
do_tasks (PUZZLE1, 'paul')

# *task* 7: call do_tasks on PUZZLE2 (that's a 2!) and 'paul'.
# Your code should work on the bigger puzzle with no changes made to do_tasks.
# If it doesn't work properly, go over your code carefully and fix it.
# Hint: you shouldn't be using PUZZLE1 anywhere in do_tasks.

do_tasks (PUZZLE2, 'paul')



