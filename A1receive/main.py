import serial
import time

def receive_and_save_data(port, baud_rate, output_file):
    with serial.Serial(port, baud_rate) as ser:
        with open(output_file, 'w') as file:
            while True:
                line = ser.readline().decode('ascii', 'ignore').strip()  # Odbieranie danych z UART
                if line == "END":
                    break  # Przerwanie pętli, gdy napotkano "END"
                file.write(line + '\n')  # Zapisywanie danych do pliku


def wait_for_volt(port, baud_rate):
    with serial.Serial(port, baud_rate) as ser:
        while True:
            line = ser.readline().decode('ascii', 'ignore').strip()  # Odbieranie danych z UART
            if line == "CHANGE":
                break

def set_voltage(port, baud_rate, voltage):
    with serial.Serial(port, baud_rate) as ser:
        ser.write(voltage.encode())



def connect(port, baud_rate):
    with serial.Serial(port, baud_rate) as ser:
        data = "<09100000000>"
        ser.write(data.encode())
        time.sleep(1)
        data = "<01004580000>"
        ser.write(data.encode())
        time.sleep(1)
        data = "<03006920000>"
        ser.write(data.encode())
        time.sleep(1)


def disconnect(port, baud_rate):
    with serial.Serial(port, baud_rate) as ser:
        data = "<09200000000>"
        ser.write(data.encode())



def out_on(port, baud_rate):
    with serial.Serial(port, baud_rate) as ser:
        data = "<07000000000>"
        ser.write(data.encode())



def out_off(port, baud_rate):
    with serial.Serial(port, baud_rate) as ser:
        data = "<08000000000>"
        ser.write(data.encode())



def confirm(port, baud_rate):
    with serial.Serial(port, baud_rate) as ser:
        data = 0b1
        ser.write(data)


if __name__ == "__main__":
    portSTM = "//dev/tty.usbmodem11203"
    baud_rateSTM = 115200
    output_file = "results.txt"

    port ="/dev/tty.usbserial-0001"
    baud_rate = 9600

    connect(port, baud_rate)
    out_on(port, baud_rate)

    data = "<01004500000>"
    wait_for_volt(portSTM, baud_rateSTM)
    set_voltage(port, baud_rate, data)
    confirm(portSTM, baud_rateSTM)

    data = "<01005000000>"
    wait_for_volt(portSTM, baud_rateSTM)
    set_voltage(port, baud_rate, data)
    confirm(portSTM, baud_rateSTM)

    data = "<01006000000>"
    wait_for_volt(portSTM, baud_rateSTM)
    set_voltage(port, baud_rate, data)
    confirm(portSTM, baud_rateSTM)

    data = "<01007000000>"
    wait_for_volt(portSTM, baud_rateSTM)
    set_voltage(port, baud_rate, data)
    confirm(portSTM, baud_rateSTM)

    data = "<01008000000>"
    wait_for_volt(portSTM, baud_rateSTM)
    set_voltage(port, baud_rate, data)
    confirm(portSTM, baud_rateSTM)

    data = "<01009000000>"
    wait_for_volt(portSTM, baud_rateSTM)
    set_voltage(port, baud_rate, data)
    confirm(portSTM, baud_rateSTM)

    data = "<01010000000>"
    wait_for_volt(portSTM, baud_rateSTM)
    set_voltage(port, baud_rate, data)
    confirm(portSTM, baud_rateSTM)

    data = "<01011000000>"
    wait_for_volt(portSTM, baud_rateSTM)
    set_voltage(port, baud_rate, data)
    confirm(portSTM, baud_rateSTM)

    data = "<01012000000>"
    wait_for_volt(portSTM, baud_rateSTM)
    set_voltage(port, baud_rate, data)
    confirm(portSTM, baud_rateSTM)

    data = "<01013000000>"
    wait_for_volt(portSTM, baud_rateSTM)
    set_voltage(port, baud_rate, data)
    confirm(portSTM, baud_rateSTM)

    data = "<01014000000>"
    wait_for_volt(portSTM, baud_rateSTM)
    set_voltage(port, baud_rate, data)
    confirm(portSTM, baud_rateSTM)

    data = "<01015000000>"
    wait_for_volt(portSTM, baud_rateSTM)
    set_voltage(port, baud_rate, data)
    confirm(portSTM, baud_rateSTM)

    data = "<01016000000>"
    wait_for_volt(portSTM, baud_rateSTM)
    set_voltage(port, baud_rate, data)
    confirm(portSTM, baud_rateSTM)

    data = "<01017000000>"
    wait_for_volt(portSTM, baud_rateSTM)
    set_voltage(port, baud_rate, data)
    confirm(portSTM, baud_rateSTM)

    data = "<01017500000>"
    wait_for_volt(portSTM, baud_rateSTM)
    set_voltage(port, baud_rate, data)
    confirm(portSTM, baud_rateSTM)

    out_off(port, baud_rate)
    disconnect(port, baud_rate)
    confirm(portSTM, baud_rateSTM)
    wait_for_volt(portSTM, baud_rateSTM)

    receive_and_save_data(portSTM, baud_rateSTM, output_file)
