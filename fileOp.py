import csv 

def writeToFile(colours, result):
    with open("training.csv", 'a', newline="") as fp:

        writer = csv.writer(fp)
        writer.writerow([colours[0], colours[1], colours[2], result])
        

def getFileColours(colours):
    
    r,g,b = colours
    fileColour = [str(r), str(g), str(b)]
    return fileColour 
    
