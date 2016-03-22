import json
import gzip
import csv


def parse(path):
  g = gzip.open(path, 'r')
  for l in g:
    yield eval(l)

fileName = ["reviews_Baby.json.gz", "reviews_Electronics.json.gz", "reviews_Home_and_Kitchen.json.gz", "reviews_Tools_and_Home_Improvement.json.gz"]
#fileName = ["reviews_Baby.json.gz"]
for i in range(len(fileName)):
  id = 0
  outputFile = open(fileName[i] + '.csv', 'w',newline='')
  outputWriter = csv.writer(outputFile)
  outputWriter.writerow(["ID", "ProductID", "Review Summary", "Review Text"])
  for review in parse(fileName[i]):
        id = id + 1
        if (id == 3000):
          break
        else:
          outputWriter.writerow([id ,review['asin'], review['summary'],review['reviewText']])
print("Done!")

