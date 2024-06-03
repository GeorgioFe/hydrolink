import serial
import time

# Replace 'COM3' with the correct port for your Bluetooth device
# On Windows, it will be something like 'COM3', on Linux it will be something like '/dev/rfcomm0'
bt_port = 'COM12'  # Update this
baud_rate = 115200

ser = serial.Serial(bt_port, baud_rate)

def read_from_bluetooth():
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            print(f"Received: {data}")

if __name__ == "__main__":
    try:
        read_from_bluetooth()
    except KeyboardInterrupt:
        print("Exiting Program")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ser.close()
