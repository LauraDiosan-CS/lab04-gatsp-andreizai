import os


def fileData(filename):
    file = open(filename, "r")
    n = int(file.readline())
    m = []
    for line in file:
        m.append([])
        for elem in line.split(","):
            m[-1].append(int(elem))
    network = {}
    network["noNodes"] = n
    network["matrix"] = m
    return network

def save(c):
    filePath = os.path.join(os.getcwd(), "easy-out.txt")
    fileOutput = open(filePath, "w+")

    fileOutput.writelines(str(c.fitness)+ "\n")
    list = c.repres;
    l2 = [x+1 for x in list]
    fileOutput.write(str(l2))