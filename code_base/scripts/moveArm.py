import serial
import time

'''
enum PART
{
  BASE=0, 
  SHOULDER, 
  ELBOW,  
  WRISTROTATION, 
  WRIST  
};

enum DIRECTION
{
  L=1,  //left
  R,    //right
  F,    //forward
  B,    //backward
  U,    //up
  D,    //down
  WU,   //wrist up
  WD    //wrist down
};
'''
class arm:
    def __init__(self, serial_port = 'COM3'):
        self.port = serial.Serial(serial_port, 115200,timeout=1)
        ###the defination of parts, the key words of different joints of the arm from down to up
        self.part = {'BASE' : '0', 'SHOULDER':'1', 'ELBOW':'2', 'WRISTROTATION':'3', 'WRIST':'4'}
        ###the defination of direction, the key words of direction of joints
        ###BASE --> Left & Right
        ###SHOULDER --> Forward & Backward
        ###ELBOW --> Up & Down
        ###WRISTROTATION --> Wrist UP & Wrist down
        ###WRIST --> Vertical & horizontal
        self.direction = {'L':'1', 'R':'2', 'F':'3','B':'4', 'U':'5','D':'6','WU':'7','WD':'8', 'H':'9', 'V':'0'}
        time.sleep(3)
    def sent2arm(self, cmd):
        for i in range(4):
            self.port.write(cmd.encode())
            time.sleep(0.05)
            OK = self.port.read(1).decode()
            if(OK == 'T'):
                #print('OK***********************88888888')
                break
            print(OK+'retry')
           
    def set_joint(self, joint, direction, speed = 0):
        speed = max(0, speed)
        speed = min(50, speed)
        speed = int(speed)
        cmd = 'S'+ self.part[joint]+self.direction[direction]+str(speed).zfill(3)+'\n'
        print(cmd)
        self.sent2arm(cmd)
        
    def close(self):
        self.port.close()
        
        
if __name__ == '__main__':
    a=arm()
    time.sleep(3)
    a.set_joint('ELBOW', 'U', 3)
    a.set_joint('SHOULDER', 'F', 3)
    time.sleep(3)
    a.set_joint('ELBOW', 'D', 3)
    a.set_joint('SHOULDER', 'B',3)
    ##time.sleep(1)
    #a.set_joint('BASE', 'L', 10)
    #time.sleep(1)
    #a.set_joint('BASE', 'R', 10)
