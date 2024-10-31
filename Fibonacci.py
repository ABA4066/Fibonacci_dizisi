import time

sayim=0
sayin=1
while True:
    time.sleep(0.5)
    print(sayim)
    time.sleep(0.5)
    print(sayin)
    sayim = sayim + sayin
    sayin = sayin + sayim

