print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/       ''')
import random
words=['abacus','baboon','cactus']
chosen_word=random.choice(words)
word_display=['_' for _ in chosen_word]
attempts=7
print("Welcome to hangman")
while attempts>0 and '_' in word_display:
  print("\n" + ' '.join(word_display))
  guess=input("Guess a letter: ").lower()
  if guess in chosen_word:
    for index,letter in enumerate(chosen_word):
      if letter==guess:
        word_display[index]=guess
  else:
    print("The word you guessed is not in the chosen word.") 
    attempts-=1     
if '_' not in word_display:
  print("You guessed it!!!")
  print(' '.join(word_display))
  print("You survived!")
else:
  print(f"You ran out of attempts.The word was {chosen_word}")
  print("You lost!")
