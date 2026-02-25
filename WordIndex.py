#WordIndex.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("gettysberg.txt", 'r')
  lineNumber = 0
  words = {} #create an empty dictionary
  
  for line in textFile:
    lineNumber = lineNumber + 1
    wordlist = line.split()
   
    for w in wordlist:
      w = w.lower()
      w = w.replace("," ,"")
      w = w.replace("." ,"")
      w = w.replace("?" ,"")
      w = w.replace("!" ,"")
      w = w.replace("." ,"")
      w = w.replace("\"" ,"")
      
      
      if w in words:
        if lineNumber not in words[w]:
         words[w].append(lineNumber)
      else:
        words[w] = [lineNumber]
  
  for word in words:
    print(word, words[word])


if __name__ == '__main__':
  main()
