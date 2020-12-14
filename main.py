
# Welcomes user
welcome = "Welcome to my MadLib program. Please enter some information below:\n"
here_is= "\nHere is your MadLib:\n"
print(welcome)

# Creates dictionary 
madlib_words =[
   "Name",
   "Place",
   "Food item",
   "Noun",
   "Another Name",
   "Animal",
   "Another noun",
   "Another food item",
   "Number larger than 1"
  ]

# Stores user input
madlib_userinput= {}

# for loop to ask user for input
for keyitem in madlib_words:
  word = input({keyitem})
  madlib_userinput[keyitem] = word
  
# prints MadLib
print(here_is)
print(f"{madlib_userinput['Name'].capitalize()} was walking by the {madlib_userinput['Place']}, watching the seagulls fly by, when one of them grabbed his lunchbag full of {madlib_userinput['Food item']}s He didn't want to chase it because he didn't want people to think he was a {madlib_userinput['Noun']}, so he just watched it fly out over the ocean. \" I'm not going after it,\" he said to {madlib_userinput['Another Name']},\"Maybe the {madlib_userinput['Animal']}s will bring the bag back to you\"-said a kid while building a sand {madlib_userinput['Another noun']}. A man started chasing after it, and caught it and put it down on the sand.\"You\'re a hero!\" a passerby exclamated in awe.{madlib_userinput['Name'].capitalize()} looked over at the seagull, as it dissapeared in the horizon.Then they all walked to the {madlib_userinput['Another food item']} truck to get a  {madlib_userinput['Number larger than 1']} drinks to celebrate.")

