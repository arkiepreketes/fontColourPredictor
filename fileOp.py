import csv 

def writeResultToFile(colours, result):
    with open("training.csv", 'a', newline="") as fp:

        colours = normaliseData(colours)

        writer = csv.writer(fp)
        writer.writerow([colours[0], colours[1], colours[2], result])
        

def getFileColours(colours):
    
    r,g,b = colours
    fileColour = [str(r), str(g), str(b)]
    return fileColour 
    
def normaliseData(colour):

    colour[0] = str(int(colour[0]) / 255)
    colour[1] = str(int(colour[1]) / 255)
    colour[2] = str(int(colour[2]) / 255)
    return colour

def writeHypers(weights, bias):
    
    with open("hyperparameters.txt", 'w', newline="") as fp:

        writer = csv.writer(fp)
        writer.writerow(weights)
        writer.writerow([bias])


def getWeightFromFile():
    
    with open("hyperparameters.txt", 'r') as fp:
        
        reader = csv.reader(fp)
        return next(reader)

def getBiasFromFile():
    
    with open("hyperparameters.txt", 'r') as fp:
        
        reader = csv.reader(fp)
        return next(reader)










