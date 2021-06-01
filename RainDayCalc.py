import random

def main():  

  num = 0 #will represent how many names are being analyzed
  result = [] #will hold resulting names to be printed
  rows = [] #holds rows from uploaded text file
  totals = [] #holds the sums from uploaded text file
  names = [] #holds names from uploaded text file

  # Have user input number of guards to stay
  max = input("How many guards can stay?")

  # Have user input the file name
  filename = input("What is the name of text file?")
  filename = filename + ".txt"

  # Open the file back up and read the contents
  f = open(filename,"r")

  if f.mode == 'r': # Check to make sure that the file was opened
    for line in f:
        # Split on any whitespace (including tab characters)
        row = line.split()
        # Convert strings to numeric values:
        row[1] = int(row[1])
        row[2] = int(row[2])
        rows.append(row)
    else:
        print("file won't open")
  
  # Prompt user to enter the schedule (since canidates will vary depending on who's working)
  response = input("Who is working today? (enter one name at a time, hit \"q\" to exit)")
  scheduled = []

  while (response != "q"):
        scheduled.append(response)
        response = input("Who is working today? (enter one name at a time, hit \"q\" to exit)")

  response = ("Please Confirm the following Guards are Scheduled (Y/N)")      
  for x in scheduled:
      print(x + " ,")

  for n in rows:
        if scheduled.contains(n[0]):
            names.append(n[0])
            totals.append(n[1] + n[2])

  while (response == "y"):

        while (num < max):
            for x in result:
                print(x)
            
            min = 1000

            #determine the minimum sum
            for x in totals:
                if (x < min):
                    min = x
                
            #clear result so that it can be replaced
            result = []

            #determine the sum of minimums
            for x in totals:
                if (x == min):
                    result.append(names[x.getIndex()])
                    totals.remove(x.getIndex())
                    names.remove(x.getIndex())
                    sum = sum + 1

        while ((num - max) > 0):
            rn = random.randint(0,num - max)
            print(names[rn])
            names.remove(rn)
            num = num - 1
        
        response = input("Would you like to redo? (Y/N)")

if __name__ == "__main__":
  main()
