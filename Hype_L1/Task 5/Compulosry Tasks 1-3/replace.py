# Compulsory Task 2:

# Sentence to change:
sent_change = "The!quick!brown!fox!jumps!over!the!lazy!dog!"

# Replaces all "!" with " "(blank space):
new_sent = sent_change.replace("!", " "[0:])
# Makes string uppercase:
new_sent = new_sent.upper()
# reverses string:
new_sent = new_sent[::-1]

print(new_sent)
