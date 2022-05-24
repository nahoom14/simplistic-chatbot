import re, time

bot_message = "Hello, my name is Diana. What is your name?"
patient_message = "My name is John."

print("Diana: " + bot_message )
time.sleep(2)
print("John: " + patient_message)
time.sleep(2)

print("Diana: " + re.sub("My name is", "Hi", patient_message))
time.sleep(2)


bot_message = "How are you feeling today?"
patient_message = "I am feeling sad."

print("Diana: " + bot_message)
time.sleep(2)
print("John: " + patient_message)
time.sleep(2)

print("Diana: " + re.sub("I am", "I am sorry you are", patient_message))
time.sleep(2)
print("Diana: " + re.sub(".* (depressed|sad)", "Why are you feeling \g<1>?", patient_message))
time.sleep(2)

patient_message = "I don't know what my purpose is in life."
bot_message = re.sub("I", "You", patient_message)
bot_message = re.sub("my", "your", bot_message)
bot_message = re.sub("\.", "", bot_message)
bot_message += "?"


print("John: " + patient_message)
time.sleep(2)
print("Diana: " + bot_message)
