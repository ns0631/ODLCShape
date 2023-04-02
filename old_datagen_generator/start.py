from multiprocessing import Process
import os

def p1():
    os.system("python3 generator.py 0")

def p2():
    os.system("python3 generator.py 100")

def p3():
    os.system("python3 generator.py 200")

def p4():
    os.system("python3 generator.py 300")

def p5():
    os.system("python3 generator.py 400")

if __name__ == "__main__":
    t1 = Process(target=p1)
    t1.start()
    t2 = Process(target=p2)
    t2.start()
    t3 = Process(target=p3)
    t3.start()
    t4 = Process(target=p4)
    t4.start()
    t5 = Process(target=p5)
    t5.start()
    """
    t6 = Process(target=p6)
    t6.start()
    t7 = Process(target=p7)
    t7.start()
    t8 = Process(target=p8)
    t8.start()
    t9 = Process(target=p9)
    t9.start()
    t10 = Process(target=p10)
    t10.start()
    """