import os
import re

import wolframalpha
# Get an AppID at developer.wolframalpha.com. Save your AppID as a environment variable and name the key APP_ID.
client = wolframalpha.Client(os.environ['APP_ID'])

def output(input):
  print("Answer to "+str(input)+"\n")
  try:
    res = client.query(input)
    print(next(res.results).text)
    print("\n")
    return
  except:
    return output("Provide a different question: ")
  
#Ask questions to the Wolfram Knowledgebase. 
output("2+2")

output("Volume of a Cylinder")

output("cost of 300 kWh of electricity in Minnesota")

output("50 lb wet dog shaking frequency")

output(input("Ask a question: "))