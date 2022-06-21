import os
import re

import wolframalpha
# Get an AppID at developer.wolframalpha.com. Save your AppID as a environment variable and name the key APP_ID.
client = wolframalpha.Client(os.environ['APP_ID'])

def output(input):
  res = client.query(input)
  print(next(res.results).text)

#Input questions to the Wolfram Knowledgebase 
output("2+2")

output("Volume of a Cylinder")

output("Range[10]")

output("NestList[f, x, 5]")

output(input("ask a question:"))

