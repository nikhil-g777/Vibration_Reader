import socket, traceback
import numpy as np
from pylive import live_plotter

size = 100
x_vec = np.linspace(0,1,size+1)[0:-1]
y_vec = np.random.uniform(low=9.6, high=9.9, size=(len(x_vec)))
line1 = []
# while True:
#     rand_val = np.random.randn(1)
#     y_vec[-1] = rand_val
#     line1 = live_plotter(x_vec,y_vec,line1)
#     y_vec = np.append(y_vec[1:],0.0)

host = ''
# host = ''
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

timer = 0

while 1:
    try:
        message, address = s.recvfrom(8192*2)
        timer += 1
        message = str(message).split(",")
        accelerometer_readings = []
        for index, val in enumerate(message):
            val = val.strip()
            if val == "3":
                accelerometer_readings.append(float(message[index+1].replace("'","").strip()))
                accelerometer_readings.append(float(message[index+2].replace("'","").strip()))
                accelerometer_readings.append(float(message[index+3].replace("'","").strip()))
                y_vec[-1] = accelerometer_readings[2]
                line1 = live_plotter(x_vec,y_vec,line1)
                y_vec = np.append(y_vec[1:],0.0)
                print(accelerometer_readings)
    except(KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()