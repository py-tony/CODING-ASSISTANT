# Compulsory Task 2:

# Import random to generate random joke:
import random

# Dictionary of 10 Jokes:
joke_list = {
    1: "What’s the best thing about Switzerland? \n"
       "I don’t know, but the flag is a big plus.",

    2: "Why do we tell actors to “break a leg?” \n"
       "Because every play has a cast.",

    3: "Hear about the new restaurant called Karma? \n"
       "There’s no menu: You get what you deserve.",

    4: "A woman in labour suddenly shouted, \"Shouldn’t! Wouldn’t! Couldn’t! Didn’t! Can’t!\" \n"
       "\"Don’t worry,\" said the doctor. \"Those are just contractions.\"",

    5: "Did you hear about the actor who fell through the floorboards? \n"
       "He was just going through a stage.",

    6: "Did you hear about the claustrophobic astronaut? \n"
       "He just needed a little space.",

    7: "Why don’t scientists trust atoms? \n"
       "Because they make up everything.",

    8: "What sits at the bottom of the sea and twitches? \n"
       "A nervous wreck.",

    9: "What did the bald man exclaim when he received a comb for a present? \n"
       "Thanks— I’ll never part with it!",

    10: "What did the left eye say to the right eye? \n"
        "Between you and me, something smells."
}


print("Here's a Joke:")
print("|")

# Print random generated joke:
print(f"{joke_list[random.randrange(1, 10)]}")
