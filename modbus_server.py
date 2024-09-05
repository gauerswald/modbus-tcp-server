from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataStore, ModbusSlaveContext, ModbusServerContext

def run_modbus_server():
    # Erstellen eines Datenspeichers
    store = ModbusSequentialDataStore()
    slaves = ModbusSlaveContext(di=store, co=store, hr=store, ir=store)
    context = ModbusServerContext(slaves=slaves, single=True)

    # Geräteinformationen
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'Vendor'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'http://example.com'
    identity.ProductName = 'Modbus Server'
    identity.ModelName = 'Modbus Server'
    identity.MajorMinorRevision = '1.0'

    # Starten des Servers Test
    StartTcpServer(context, identity=identity, address=("0.0.0.0", 5020))

if __name__ == "__main__":
    run_modbus_server()
