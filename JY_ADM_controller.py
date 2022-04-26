import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md
import sys

def control_all(para):
    control_key = list(bin(int(para,16))[2:])
    control_key.reverse()
    x = list(map(int,control_key))
    for i in range(32-len(x)):
        x.append(0)
    master = mt.TcpMaster("192.168.1.232", 10000)
    master.set_timeout(5.0)
    master.execute(slave=1, function_code=md.WRITE_MULTIPLE_COILS, starting_address=0, quantity_of_x=len(x), output_value=x)
    master.execute(slave=1, function_code=md.READ_COILS, starting_address=0, quantity_of_x=len(x), output_value=x)

def control_one(address,value):
    master = mt.TcpMaster("192.168.1.232", 10000)
    master.set_timeout(5.0)
    master.execute(slave=1, function_code=md.WRITE_SINGLE_COIL, starting_address=address, quantity_of_x=1,output_value=value)
    status = master.execute(slave=1, function_code=md.READ_COILS, starting_address=address, quantity_of_x=1, output_value=value)
    if status[0] != value:
        master.execute(slave=1, function_code=md.WRITE_SINGLE_COIL, starting_address=address, quantity_of_x=1,output_value=value)

def main():
    parameter = sys.argv
    if len(parameter) == 2:
        control_all(parameter[1])
    elif len(parameter) == 3:
        control_one(int(parameter[1]),int(parameter[2]))
    else:
        print("wrong parameters indeed")

if __name__ == "__main__":
    #main()
    control_one(31,1)