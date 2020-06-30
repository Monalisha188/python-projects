#to print the letter of string in decreasing order of frequency

def most_frequent(str):
  count = {}
  for x in str:
    if x in count:
      count[x]+= 1
    else:
      count[x] = 1
  mydict = sorted(count.items(), key = lambda x: x[1], reverse = True)
  print(mydict)
  return
  
most_frequent(str = "mississippi")
