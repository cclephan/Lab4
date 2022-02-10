import pyb
import utime
import task_share


def toggler(timerobj):
    q0.put(myADC.read())

if __name__ == "__main__":
    print('Hello I am a line')
    pinC0 = pyb.Pin(pyb.Pin.board.PC0)
    pinC1 = pyb.Pin(pyb.Pin.board.PC1,pyb.Pin.OUT_PP)
    tim = pyb.Timer(4, freq = 1000)
    myADC = pyb.ADC(pinC0)
    q0 = task_share.Queue ('h', size = 1000, thread_protect = False, overwrite = False,
                           name = "Queue 0")
    
    pinC1.high()
    tim.callback(toggler)
    
    #Constantly checking whether queue is full and stops timer when true.
    while True: 
        if q0.full():
            tim.deinit()
            pinC1.low()
            break
        
    #Print Queue values
    while q0.any():
        print(q0.get())
    
    print('Stop')