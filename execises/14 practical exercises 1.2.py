"""
Exercise 2

a.- ask to user that say any text and

-calcute how much takes saying it
-how words say it?

b.- if take more than 1 minute
- say it "stop it please"

c.- speed speker is 30% more faster:
-how take it in say it the same?
"""

#a
phrase = input("Tell me want do you want say: ")
word_phrase_len = len(phrase.split(" "))
time_phrase = word_phrase_len//2

print(f"time needed for speech: {time_phrase}")
print(f"number of words: {word_phrase_len}")

#b
if time_phrase>60:
    print("time exceed for speech")
else:
    print("time is ok")
    
#c
speed_speak_time = int(time_phrase * .7)
print(f"time needed for a 30% faster speaker: {speed_speak_time}")
