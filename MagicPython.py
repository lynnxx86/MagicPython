import webbrowser
import random
import datetime





responses_file = "responses.txt"
ascii_file = "ascii.txt"
with open(ascii_file, "a+") as file:
    file.seek(0)
    printer = file.read()

print(printer)


print("Welcome to lynnxx's magic 8 program!")
print("Named after the magic 8 ball toy of yesteryear, MagicPython will answer any yes/no question you ask!")
usr_nme = input("What's your name? ")

char_count = 0
for char in usr_nme:
 char_count += 1



while True:
 question = input("What's your question, " + usr_nme + "? ")

 if (question.lower() == "quit"):
  print("Goodbye!")
  break
 timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

 rickroll = random.randint(1,500)

 if rickroll <= 2:
     webbrowser.open("https://www.youtube.com/watch?v=3BFTio5296w")
 else:
     with open(responses_file, "a+") as file:
         file.seek(0)
         responseses = file.read().splitlines()
         if responseses:
             random_response = random.choice(responseses)
             print(random_response)


 again = input("Would you like to ask another question? Yes/No: ").strip().lower()
 if again not in ["yes", "y"]:
   print("Goodbye!")
   break




