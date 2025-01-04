import asyncio
from bleak import BleakScanner, BleakClient
from bleak.backends.characteristic import BleakGATTCharacteristic
import pyautogui
import time

class BLEDevice:
    def __init__(self):
        self.selected_device = None
        self.is_connected = False
        pyautogui.PAUSE = 0.1
    
    async def scan_devices(self):
        """Scanning for available BLE devices"""
        print("Starting BLE device scan...")
        devices = await BleakScanner.discover()
        
        if not devices:
            print("No devices found")
            return None
            
        print("\nFound devices:")
        for idx, device in enumerate(devices):
            print(f"{idx + 1}. {device.name or 'Unnamed'} ({device.address})")
        
        while True:
            try:
                choice = int(input("\nSelect device number to connect: ")) - 1
                if 0 <= choice < len(devices):
                    self.selected_device = devices[choice]
                    return True
                else:
                    print("Invalid number. Try again.")
            except ValueError:
                print("Please enter a number.")

    def parse_distance(self, data: bytearray) -> int:
        """Parse distance value from bytes using correct protocol"""
        try:
            if len(data) >= 16 and data[2] == 0x02 and data[3] == 0x01:
                distance = int.from_bytes(data[14:16], byteorder='big')
                return distance
            return None
        except Exception as e:
            print(f"Error parsing distance: {e}")
            return None

    def type_number(self, number: int):
        """Type number using keyboard simulation"""
        try:
            number_str = str(number)
            pyautogui.typewrite(number_str)
        except Exception as e:
            print(f"Error simulating keyboard: {e}")

    def notification_handler(self, characteristic: BleakGATTCharacteristic, data: bytearray):
        """Notification handler"""
        distance = self.parse_distance(data)
        if distance is not None:
            hex_data = ' '.join([f"{b:02X}" for b in data])
            print("\nNew data received:")
            print(f"Raw HEX: {hex_data}")
            print(f"Distance: {distance/1000:.3f} m ({distance} mm)")
            self.type_number(distance)
            print("-" * 50)

    async def connect_and_read(self):
        """Connect to device and read data"""
        if not self.selected_device:
            print("No device selected")
            return

        print(f"\nConnecting to {self.selected_device.name or 'Unknown'}...")
        
        try:
            async with BleakClient(self.selected_device.address) as client:
                print("Connected successfully!")
                self.is_connected = True

                notify_uuid = "0000ee02-0000-1000-8000-00805f9b34fb"
                
                try:
                    await client.start_notify(notify_uuid, self.notification_handler)
                    print("\nStarted reading notifications. Press Ctrl+C to stop")
                    print("Waiting for data...")
                    
                    while True:
                        await asyncio.sleep(1)
                        
                except Exception as e:
                    print(f"Error working with characteristic: {e}")
                
                finally:
                    await client.stop_notify(notify_uuid)
                    
        except Exception as e:
            print(f"Connection error: {e}")
            self.is_connected = False

async def main():
    ble_device = BLEDevice()
    if await ble_device.scan_devices():
        await ble_device.connect_and_read()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nProgram stopped by user")