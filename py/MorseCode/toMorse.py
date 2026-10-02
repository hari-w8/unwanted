import re
morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
}

onlyMorse = []

print("choose your's: \n 1. Manual typing.. \n 2. Upload file..")
opt = str(input(">>>"))
if opt == "1":
   text = input("Text or even Sentence type here: ")
   extracted = text.split(" ")
   for n in extracted:
      tempWord = ""
      for i in n:
         tempWord = morse[i.upper()]
         onlyMorse.append(tempWord)
      onlyMorse.append("  ")
   print("Morse code of yours:", end=" ")
   for x in onlyMorse:
       print(x, end= " ")
   print()
elif opt == "2":
   f = input("Upload file(Filename?): ")
   with open(f, "r") as file:
     word = file.read().split(" ")
     checkedWords = []
     for c in word:
        cw = ""
        for w in c:
           if w not in [".", ",", "\n"]:
              cw = cw + w
        checkedWords.append(cw)
     for n in checkedWords:
        if re.match(r"[0-9]", n):
           onlyMorse.append(n)
           continue
        tempWord = ""
        for i in n:
           tempWord = morse[i.upper()]
           onlyMorse.append(tempWord)
        onlyMorse.append("  ")
     with open("IngaPaaru.txt", "w") as pencil:
      count = 0
      for x in onlyMorse:
              count = count + 1
              pencil.write(x + " ")
              if count == 30:
                 pencil.write("\n")
                 count = 0
      print(f"{"-" * 10}your file is created!!{"-" * 10}")
      cls = input("Do you want reset your file?(Y/n)").lower()
      if cls == "y":
         with open("IngaPaaru.txt", "w") as file:
              pass
      else:
         print("okayy...terminated...cum again")
         
      
                         
      
   

# else:
#     print("Irukurathey rendu options thaan moodevi..")
