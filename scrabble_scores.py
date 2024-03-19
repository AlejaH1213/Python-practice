letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# using a list comprehension and zip to create a dictionary that has the elements of letters as keys and points as values
letter_to_points = {letter: points for letter, points in zip(letters,points)}
# blank tiles
letter_to_points[" "] = 0
# function that will take in a word and return how many points that word is worth
def score_word(word):
  point_total = 0
  # for loop that goes through the letters in word
  for letter in word:
    # if the letter is in the letter points
    if letter in letter_to_points:
      # it adds the value of that letter from the dictionary to the points total
      point_total += letter_to_points[letter]
      #if the letter is not in the dictionary then it adds a zero 
    else:
      point_total += 0
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

player_to_points = {}
# iterating through the items in plater to words 
for player, words in player_to_words.items():
  player_points = 0 
  # a loop that goes through each word in words and adds the value of score_word with word as an input
  for word in words:
    player_points += score_word(word)
  # set the current plater value to be a key of player to points with a value of player points
  player_to_points[player] = player_points

print(player_to_points)