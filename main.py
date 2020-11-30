import sys
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import Slot
import PySide2
import time
from Models.FileFastaReader import FileFastaReader
from Models.readerProcess import ReaderProcess, pr
from multiprocessing import Process, Queue, Pool
from NetworkFastaFetcher import NetworkFastaFetcher
from PySide2.QtNetwork import QNetworkAccessManager
import numpy as np
from dnaDotplot import DNADotplot
from dnaSequence import DNASequence
from dotplot import DotplotData

from scoringMatrixCreator import ScoringMatrixCreator

from pointsParser import parseScoring

import dotplotStorage

from controller import *


cnt = 0
start = 0

def printData(identifier, data):
    print(identifier)
    print(data)
    if cnt == 9:
        print((time.time_ns() - start)/1_000_000_000)

def finito(ident, data):
    global cnt
    cnt -= 1
    print("finito", len(ident), len(data))
    if cnt == 0:
        print((time.time_ns() - start)/1_000_000_000)

def main():
    global cnt, start
    app = QApplication([])
    contr = Controller()

    fileReader = FileFastaReader()
    fileReader.data_ready.connect(printData)
    start = time.time_ns()
    fileReader = FileFastaReader()
    fileReader.data_ready.connect(pr)

    # for i in range(0,10):
    #     pr(fileReader.getData("Models/abc.fasta"))
    #
    # proc = []
    # commands = []
    #
    # for i in range(0, 10):
    #     commands.append("python Models/ReaderProgram.py")
    #
    # for i in range(0, 5):
    #     proc.append(ReaderProcess(commands[i*len(commands)//5: (i+1)*len(commands)//5]))
    #     proc[i].results_ready.connect()
    #     proc[i].errorOccurred.connect(lambda error: print("error", error, proc[i].errorString()))
    #
    # cnt = 10
    # for p in proc:
    #     p.startFirst()
    print((time.time_ns() - start) / 1_000_000_000)

    manager = QNetworkAccessManager()
    net = NetworkFastaFetcher(manager)
    net.data_ready.connect(printData)
    net.error_occurred.connect(lambda msg: print(msg))
    net.fetchFasta("3")

    s1 = DNASequence("123", "ACTG")
    s2 = DNASequence("123", "TTTG")
    dotplot = DNADotplot(DotplotData(s1, s2))
    print(dotplot.create())
    dotplotStorage.store("dotplot.txt", dotplot.data())
    dotplotStorage.loadDNA("dotplot.txt")

    scoring = parseScoring("scoring.txt")

    scoringMatrix = ScoringMatrixCreator(scoring).create(s1, s2)

    print(scoringMatrix)
    print(scoringMatrix.fetchAligned())

    return sys.exit(app.exec_())


if __name__ == "__main__":
    main()
