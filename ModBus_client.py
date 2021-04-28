from pyModbusTCP.client import ModbusClient
from time import sleep

try:
    client = ModbusClient(host="127.0.0.1", port=12345)
    client.open()
    print("Connected to server")
    while True:
        client.read_holding_registers(0)
        time.sleep(2)

except:
    client.close()
    print("Disconnected from server")
