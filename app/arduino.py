from serial import Serial
import time


class Arduino():
    # def __init__ (self):
    #     _serial_name = '/dev/ttyACM0' # ls /dev/tty* (Para malaman kung ano serial name)
    #     _baudrate = 9600
    #     self.ser = Serial(_serial_name, _baudrate, timeout=1)

    def test_process(self, qLEDStatus):
        while True:
            import random
            
            _status = [
                {'id': 1,'status':random.randint(0,1)},
                {'id': 2,'status':random.randint(0,1)},
                {'id': 3,'status':random.randint(0,1)},
                {'id': 4,'status':random.randint(0,1)},
                ]

            qLEDStatus.put(_status)
            time.sleep(1)

    def get_led_status(self):
        while True:
            status = self.ser.readline().decode('utf-8').rstrip()
            print(status)
                
    
    def check_serial_connection(self):
        if self.ser.is_open == False:
            return False
        
        return True