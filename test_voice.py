from voice.recognition import is_same_person

same, score = is_same_person(
    "voices/harshit/harshit.wav",
    "voices/temp/current.wav"
)

print("Match:", same)
print("Score:", score)