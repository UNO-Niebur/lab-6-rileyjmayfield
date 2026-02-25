#WordCount.py
#Name:Riley Mayfield
#Date:2/24
#Assignment:Lab 6
#Purpose:Develop understanding of slicing strings

def main():
  try:
    textFile = open("fish.txt", 'r')
  except FileNotFoundError:
    print("Error could not find file.")
    return
  lineCount = 0
  wordCount = 0
  chCount = 0

  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1

  textFile.seek(0)
  content = textFile.read()
  chCount = chCount + len(content)
  

  print("Lines:", lineCount)    
  print("Words:", wordCount)  
  print("Characters:", chCount)  


if __name__ == '__main__':
  main()
