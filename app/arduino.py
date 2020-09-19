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
            # status = self.ser.readline().decode('utf-8').rstrip()
            # print(status)
            _status = [
                {'id': 1,'status':0}, {'id': 2,'status':0}, {'id': 3,'status':0}, {'id': 4,'status':0},
                {'id': 5,'status':0}, {'id': 6,'status':0}, {'id': 7,'status':0}, {'id': 8,'status':0},
                {'id': 9,'status':0}, {'id': 10,'status':0}, {'id': 11,'status':0}, {'id': 12,'status':0},
                {'id': 13,'status':0}, {'id': 14,'status':0}, {'id': 15,'status':0}, {'id': 16,'status':0},
                {'id': 17,'status':0}, {'id': 14,'status':0}, {'id': 15,'status':0}, {'id': 16,'status':0},
                {'id': 13,'status':0}, {'id': 14,'status':0}, {'id': 15,'status':0}, {'id': 16,'status':0},
                {'id': 13,'status':0}, {'id': 14,'status':0}, {'id': 15,'status':0}, {'id': 16,'status':0},


                ]

            qLEDStatus.put(_status)
            time.sleep(1)    
    
    def check_serial_connection(self):
        if self.ser.is_open == False:
            return False
        
        return True