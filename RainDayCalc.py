#necessary library
import random

def main():  

  
  rows = [] #holds rows from uploaded text file
  

  # Have user input number of guards to stay
  max = int(input("How many guards can stay?  "))

  # Have user input the file name
  #filename = input("What is the name of text file?")

  # Open the file back up and read the contents
  f = open("todstallies.txt","r")

  if f.mode == 'r': # Check to make sure that the file was opened
    for line in f:
        # Split on any whitespace (including tab characters)
        row = line.split()
        # Convert strings to numeric values:
        row[1] = int(row[1])
        row[2] = int(row[2])
        rows.append(row)
  else:
        # Inform user if file will not open correctly
        print("file won't open")
  
  # Prompt user to enter the schedule (since canidates will vary depending on who's working)
  print("Who is working today? (enter one name at a time, hit \"q\" to exit)")

  
  response = input()
  numscheduled = 0
  scheduled = []

  while (response != "q"):
        scheduled.append(response)
        numscheduled = numscheduled + 1
        response = input()

  print("***********************************************************")
  print("The schedules guards are:")
  

  for x in scheduled:
      print(x)

  response = input("Please Confirm the following Guards are Scheduled (Y/N): ")  

  if (numscheduled < max):
      print("there are more spaces than guards.")

  while (response == "y" and numscheduled > max):
        print("***********************************************************")
        print("The Guards that should stay are:")

        num = 0 #will represent how many names are being analyzed
        temp = 0 #will represent the number of guards that are confirmed to stay
        totals = [] #holds the sums from uploaded text file
        names = [] #holds names from uploaded text file
        result = [] #will hold resulting names to be considered
        finalresult = [] #will hold names that will stay for rain day
        
        # generates canidates data into a list of name and list of totals
        for n in rows:
            if n[0] in scheduled:
                names.append(n[0])
                totals.append(n[1] + n[2])

        # selects canidates based off of lowest totals
        while (num < max):

            #updates list and prints guards that are confirmed to stay
            for x in result:
                print(x)
                finalresult.append(x)
            
            #sets minimum to a value that is gaurenteed to be updated
            min = 1000

            #determine the minimum sum
            for x in totals:
                if (x < min):
                    min = x
                
            #clear result so that it can be replaced
            result = []

            #sets temp to the number of canidates confirmed for rain day
            temp = num

            #determine the sum of minimums
            for x in totals:
                if (x == min):
                    result.append(names[totals.index(x)])
                    names.remove(names[totals.index(x)])
                    totals.remove(x)
                    num = num + 1

        # determines the number of remaining canidates
        remainingcanidates = max - temp

        # randomize remaining canidates
        while (remainingcanidates > 0):
            rn = random.randint(0,num - temp - 1)
            print(result[rn])
            finalresult.append(result[rn])
            result.remove(result[rn])
            remainingcanidates = remainingcanidates - 1
            
        # provides option to restart process (can be used to prove randomization)
        response = input("Would you like to redo? (Y/N)")
  
  # -------------------------------------------------------------------------------
  # provides option to update table
  response = input("Would you like to update the table? (Y/N)")
  f = open("todstallies.txt","w+")
  #go through each line:
  #if name in final result == a name in table, add 1 to the last column

  f.close()

  
if __name__ == "__main__":
  main()
