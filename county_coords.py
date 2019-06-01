import sys, cardinal_coords

def getCoords(str):
    element = ""
    atCoords = False
    coords = ""

    for i in str:
        if atCoords:
            if i == "<":
                atCoords = False
                element = i
                coords += " "
            else:
                coords += i
        else:
            if i == ">":
                if element == "<coordinates":
                    atCoords = True
                element = ""
            if i == "<":
                element = i
            elif element != "":
                element += i
    return coords

def readFile(filename):
    file = open("./input/"+filename+".csv", 'r')

    headers = file.readline()
    allLines = file.readlines()
    processData(allLines)
    file.close()

def writeStateData(stateCode, countyData):
    ## write dataset to csv file for that state, then switch to next state
    writeFile = open("./input/stateCountyCoords/"+stateCode+".csv", "w")
    writeFile.write("County,Coordinates"+'\n')
    for item in countyData:
        writeFile.write(item+','+countyData[item]+'\n')
    writeFile.close()

def processData(fileData):
    currentState = ""
    allStates = []
    data = {}

    for line in fileData:
        splitLine = line.split(",")

        county = splitLine[0]
        stateCode = splitLine[3]
    
        if currentState == "":
            currentState = stateCode
        elif stateCode != currentState and currentState != "":
            if currentState != '05000US45003':          ## fixes random input with that tag
                writeStateData(currentState, data)
                cardinal_coords.processState(currentState)
            data = {}
            currentState = stateCode

        coords = getCoords(line)
        data[county] = coords

def main(): 
    readFile("United States Counties")

# main()