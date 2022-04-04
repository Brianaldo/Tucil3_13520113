import time
import random

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import * 
from PyQt5.QtCore import QPropertyAnimation, QRect

import threading

import sys

from Solver import *

class Window(QWidget):
    def __init__(self, solution):
        super().__init__()
        self.setGeometry(100, 100, 200, 200)
        
        self.solution = solution

        self.Puzzle01Label = QLabel( "1", self)
        self.Puzzle02Label = QLabel( "2", self)
        self.Puzzle03Label = QLabel( "3", self)
        self.Puzzle04Label = QLabel( "4", self)
        self.Puzzle05Label = QLabel( "5", self)
        self.Puzzle06Label = QLabel( "6", self)
        self.Puzzle07Label = QLabel( "7", self)
        self.Puzzle08Label = QLabel( "8", self)
        self.Puzzle09Label = QLabel( "9", self)
        self.Puzzle10Label = QLabel("10", self)
        self.Puzzle11Label = QLabel("11", self)
        self.Puzzle12Label = QLabel("12", self)
        self.Puzzle13Label = QLabel("13", self)
        self.Puzzle14Label = QLabel("14", self)
        self.Puzzle15Label = QLabel("15", self)
        self.Puzzle00Label = QLabel( " ", self)

        self.Puzzle01Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Puzzle02Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Puzzle03Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Puzzle04Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Puzzle05Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Puzzle06Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Puzzle07Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Puzzle08Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Puzzle09Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Puzzle10Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Puzzle11Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Puzzle12Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Puzzle13Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Puzzle14Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Puzzle15Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Puzzle00Label.setAlignment(QtCore.Qt.AlignCenter)

        self.Puzzle01Label.resize(50, 50)
        self.Puzzle02Label.resize(50, 50)
        self.Puzzle03Label.resize(50, 50)
        self.Puzzle04Label.resize(50, 50)
        self.Puzzle05Label.resize(50, 50)
        self.Puzzle06Label.resize(50, 50)
        self.Puzzle07Label.resize(50, 50)
        self.Puzzle08Label.resize(50, 50)
        self.Puzzle09Label.resize(50, 50)
        self.Puzzle10Label.resize(50, 50)
        self.Puzzle11Label.resize(50, 50)
        self.Puzzle12Label.resize(50, 50)
        self.Puzzle13Label.resize(50, 50)
        self.Puzzle14Label.resize(50, 50)
        self.Puzzle15Label.resize(50, 50)
        self.Puzzle00Label.resize(50, 50)

        self.Puzzle01Label.setStyleSheet("border: 1px solid black; background-color: black; color: white")
        self.Puzzle02Label.setStyleSheet("border: 1px solid black; background-color: black; color: white")
        self.Puzzle04Label.setStyleSheet("border: 1px solid black; background-color: black; color: white")
        self.Puzzle03Label.setStyleSheet("border: 1px solid black; background-color: black; color: white")
        self.Puzzle05Label.setStyleSheet("border: 1px solid black; background-color: black; color: white")
        self.Puzzle06Label.setStyleSheet("border: 1px solid black; background-color: black; color: white")
        self.Puzzle07Label.setStyleSheet("border: 1px solid black; background-color: black; color: white")
        self.Puzzle08Label.setStyleSheet("border: 1px solid black; background-color: black; color: white")
        self.Puzzle09Label.setStyleSheet("border: 1px solid black; background-color: black; color: white")
        self.Puzzle10Label.setStyleSheet("border: 1px solid black; background-color: black; color: white")
        self.Puzzle11Label.setStyleSheet("border: 1px solid black; background-color: black; color: white")
        self.Puzzle12Label.setStyleSheet("border: 1px solid black; background-color: black; color: white")
        self.Puzzle13Label.setStyleSheet("border: 1px solid black; background-color: black; color: white")
        self.Puzzle14Label.setStyleSheet("border: 1px solid black; background-color: black; color: white")
        self.Puzzle15Label.setStyleSheet("border: 1px solid black; background-color: black; color: white")
        self.Puzzle00Label.setStyleSheet("border: 1px solid black;")

        self.Puzzle01Label.move(0, 0)
        self.Puzzle02Label.move(0, 0)
        self.Puzzle03Label.move(0, 0)
        self.Puzzle04Label.move(0, 0)
        self.Puzzle05Label.move(0, 0)
        self.Puzzle06Label.move(0, 0)
        self.Puzzle07Label.move(0, 0)
        self.Puzzle08Label.move(0, 0)
        self.Puzzle09Label.move(0, 0)
        self.Puzzle10Label.move(0, 0)
        self.Puzzle11Label.move(0, 0)
        self.Puzzle12Label.move(0, 0)
        self.Puzzle13Label.move(0, 0)
        self.Puzzle14Label.move(0, 0)
        self.Puzzle15Label.move(0, 0)
        self.Puzzle00Label.move(0, 0)

        threading.Thread(target=self.callback, daemon=True).start()

    def callback(self):
        self.drawPath(self.solution)

    def drawPath(self, root):
        if root == None:
            return
        self.drawPath(root.parent)
        self.drawPuzzle(root.puzzle)

    def drawPuzzle(self, puzzle):
        post = [(0, 0) for _ in range (16)]

        for i in range (4):
            for j in range (4):
                post[puzzle[i, j]] = i * 50, j * 50

        self.Puzzle01Label.move(post[ 1][1], post[ 1][0])
        self.Puzzle02Label.move(post[ 2][1], post[ 2][0])
        self.Puzzle03Label.move(post[ 3][1], post[ 3][0])
        self.Puzzle04Label.move(post[ 4][1], post[ 4][0])
        self.Puzzle05Label.move(post[ 5][1], post[ 5][0])
        self.Puzzle06Label.move(post[ 6][1], post[ 6][0])
        self.Puzzle07Label.move(post[ 7][1], post[ 7][0])
        self.Puzzle08Label.move(post[ 8][1], post[ 8][0])
        self.Puzzle09Label.move(post[ 9][1], post[ 9][0])
        self.Puzzle10Label.move(post[10][1], post[10][0])
        self.Puzzle11Label.move(post[11][1], post[11][0])
        self.Puzzle12Label.move(post[12][1], post[12][0])
        self.Puzzle13Label.move(post[13][1], post[13][0])
        self.Puzzle14Label.move(post[14][1], post[14][0])
        self.Puzzle15Label.move(post[15][1], post[15][0])
        self.Puzzle00Label.move(post[ 0][1], post[ 0][0])
        
        time.sleep(1)

if __name__ == '__main__':
    print("Pilih jenis input: ")
    print("1. Masukkan File")
    print("2. Random")

    print()
    choose = input("Pilihan : ")
    print()

    if (choose == "1"):
        file = input("Masukkan nama file: ")
        with open ('../test/' + file, 'r') as f:
            puz = []
            for line in f.readlines():
                puz.append([int(x) for x in line.split(' ')])
            puzzle = np.array(puz)
    elif (choose == "2"):
        puz = [i for i in range(0,16)]
        random.shuffle(puz)
        puzzle = np.array(puz, dtype='int8').reshape(4,4)
    else:
        sys.exit("Masukkan tidak valid")

    printPuzzle(puzzle)

    start_time = time.time()
    if (isSolvable(puzzle)):
        solution = solve(puzzle)
        runtime = time.time() - start_time
        printPath(solution, 0)
        print()
        app = QApplication(sys.argv)
        app.setStyleSheet("QLabel{font-size: 25pt;}")
        w = Window(solution)
        w.show()
        print("Waktu eksekusi program = " + str(runtime) + " detik")
        sys.exit(app.exec())
    else:
        runtime = time.time() - start_time
        print("Waktu eksekusi program = " + str(runtime) + " detik")