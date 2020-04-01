import os
import Datas
import TSP



def main():
    filePath = os.path.join(os.getcwd(), "hard.txt")
    data = Datas.fileData(filePath)

    popSize = 100
    generations = 500
    tsp = TSP.TSP(data, popSize)
    tsp.createPop()

    globalC = None
    localC = None

    generatonCount = 1
    while generatonCount < generations:
        generatonCount += 1
        tsp.newGeneration()

        localC = tsp.best()

        if globalC is None:
            globalC = localC
        elif globalC.fitness > localC.fitness:
            globalC = localC

        print("<------------------->")
        print(generatonCount)
        print(globalC.fitness)
        print(localC.fitness)
    Datas.save(globalC)

main()
