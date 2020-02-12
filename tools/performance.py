import cProfile

def task_while():
    packages = list()
    i = 0
    while i < 24*1024*1024:
        packages.append(i)
        i += 1 

def task():
    packages = list()
    for i in range(24*1024*1204):
        packages.append(i)
    

cProfile.run("task_while()")