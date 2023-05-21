import serial
import serial.tools.list_ports as port_list

print(serial.__version__)

port="/dev/cu.usbmodem14301"
try:
    arduino = serial.Serial(port, 9600)
except:
    ports = list(port_list.comports())
    print('====> Designated Port not found. Using Port:', ports[0].device)
    print('====> Designated Port not found. Using Port:', ports[1].device)
    print('====> Designated Port not found. Using Port:', ports[2].device)
    print('====> Designated Port not found. Using Port:', ports[3].device)
    print('====> Designated Port not found. Using Port:', ports[4].device)
    port = ports[4].device

output_list = []



while True:
    output = arduino.read()
    print("test",output)

    # output_list.append(output.decode())



    # for element in output_list:
    #      element.replace('\r', '')
    #      element.replace('\n', '')

    # print(output_list)

    # if output_list[-1].endswith('\r\n'):
    #     concatenated_output = ''.join(output_list)  # Join the list elements into a single string
    #     print(concatenated_output)





