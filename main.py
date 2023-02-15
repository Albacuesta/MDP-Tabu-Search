import os
import random

from structure import solution, instance, add
from constructives import greedy, ctabu
from localsearch import lsfirstimprove
from algorithms import tabu
import datetime

def executeInstance():
    random.seed(1309)
    path = "instances/Amparo.csv"
    inst = instance.readInstance(path)
    sol = greedy.construct(inst)
    final = tabu.execute(inst, 60, 5, sol)
    solution.printSol(final)

def executeDir():
    dir = "instances"
    with os.scandir(dir) as files:
        ficheros = [file.name for file in files if file.is_file() and file.name.endswith(".csv")]
    with open("resultados.csv", "w") as results:
        for f in ficheros:
            path = dir+"/"+f
            print("Solving "+f+": ", end="")
            inst = instance.readInstance(path)
            results.write(f+"\t"+str(inst['n'])+"\t")
            start = datetime.datetime.now()
            sol = greedy.construct(inst)
            final = tabu.execute(inst, 60, 5, sol)
            elapsed = datetime.datetime.now() - start
            secs = round(elapsed.total_seconds(),2)
            print(str(final) + "\t" + str(secs))
            results.write(str(round(final, 2)) + "\t" + str(secs) + "\t" + str(5) + "\n")


if __name__ == '__main__':
    #executeInstance()
    executeDir()


