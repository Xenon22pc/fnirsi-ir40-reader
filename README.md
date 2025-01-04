# FNIRSI-IR40 BLE Reader

A Python utility for reading measurements from the FNIRSI-IR40 laser distance meter via Bluetooth Low Energy (BLE). This tool automatically connects to the device, receives measurement data, and can simulate keyboard input for the received values.

## Usage
1. Install required packages:
```bash
pip install bleak pyautogui
```
2. Turn on your FNIRSI-IR40 device and enable Bluetooth
3. Run the script:
```bash
python ble_reader.py
```
4. Select your device from the list of discovered BLE devices
5. Press the measurement button on your FNIRSI-IR40
6. The script will:
   - Display the received measurement
   - Simulate typing the measurement value

## Example Output
```
New data received:
Raw HEX: 00 15 02 01 14 00 00 00 00 02 05 14 00 00 07 13 02 06 14 00 00 00 00
Distance: 1.813 m (1813 mm)
```

## Disclaimer
This is an unofficial tool and is not affiliated with FNIRSI. Use at your own risk.