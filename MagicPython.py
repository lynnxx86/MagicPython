import webbrowser
import random
import datetime




print("Welcome to lynnxx's magic 8 program!")
print("Named after the magic 8 ball toy of yesteryear, MagicPython will answer any yes/no question you ask!")
usr_nme = input("What's your name? ")

char_count = 0
for char in usr_nme:
 char_count += 1
responses = ["Pull the trigger!","Try restarting the universe and asking again!", "No way, Jose.", "Yah", "I don't like the idea","Yeah, I don't know about that.","It seems dangerous...",
             "You may not.", "Yes, you should not.", "Absolutely not!",  "Get some chicken strips first.",
             "I don't believe in you", "This does not sound like a good idea", "Get a corndog after to protecc from negative energies.", "69",  "Don't think twice, just go for it.", "Try restarting the software and asking again!", "Nah G",
             "Yap", "I think it's a good idea!", "Yeah, totally!", "Ehhhhh.. screw it", "You may.","Yes, you should.", "Make haste!", "It has been decided without you.", "I believe in you!", "It's time to suck today's dick!!", "Do whatever you want, idk.", "Maybe you should stay home today.", "Don't do it.", "Try restarting the program and asking again!", "Try restarting the computer and asking again!","Yes", "Outlook good!", "Most likely", "As I see it, yes.", "You may rely on it", "Yes, definetly.", "Without a doubt", "It is decidedly so", "It is certain", "You already have everything you need for this journey found within. Go get it!", "Do whatever you want, idk.", "Maybe you should stay home today.", "Bring the THUNDA", "They aren't ready for someone like you!", "You're gonna kill it!", "Best of luck.. you'll need it.", "How the fuck should I know? I'm a line of code.", "The spirits are not working in your favor on this endeavor.", "The spirits are on your side today!", "Go for it!", "Better not tell you now!", "Ask again later!", "All I know is that I know nothing.", "Did you ask your pet(s), if applicable?", "Why are you asking me?", "I don't think you should.", "I'm sorry, I'm actually away from my desk at this time!", "Don't worry about it!", "Fruit loops", "Maybe you should sleep on it.", "Chicken Butt" ]


while True:
 question = input("What's your question, " + usr_nme + "? ")

 if (question.lower() == "quit"):
  print("Goodbye!")
  break
 timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

 rickroll = random.randint(1,150)

 if (rickroll <= 2):
  webbrowser.open("https://www.youtube.com/watch?v=3BFTio5296w")
 else:
  answer = random.choice(responses)
  print(answer)



 again = input("Would you like to ask another question? Yes/No: ").strip().lower()
 if again not in ["yes", "y"]:
   print("Goodbye!")
   break




