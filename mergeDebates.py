import glob
import csv
debateCategories = ["abortion","creation","gayRights","god","guns","healthcare"]
#outputFile = open(fileName[i] + '.csv', 'w',newline='')
for i in range(len(debateCategories)):
    read_files = glob.glob("C:/Python34/mergeDebates/SomasundaranWiebe-politicalDebates/" + debateCategories[i] + "/*")
    try:
        with open(debateCategories[i] + '.csv', 'w',newline='') as outputFile:
            id = 0
            print(debateCategories[i])
            outputWriter = csv.writer(outputFile)
            outputWriter.writerow(["ID", "Text"])
            for f in read_files:
                with open(f, "rb") as infile:
                    for line in infile:
                        id = id + 1
                        if "#" not in str(line):
                            outputWriter.writerow([id ,line])
    except:
        print('Oops')
print("Done")
