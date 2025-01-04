# FNIRSI-IR40 BLE Reader
A Python utility for reading measurements from the FNIRSI-IR40 laser distance meter via Bluetooth Low Energy (BLE). This tool automatically connects to the device, receives measurement data, and can simulate keyboard input for the received values.

## Installation
1. Clone this repository:
```bash
git clone https://github.com/yourusername/fnirsi-ir40-reader.git
cd fnirsi-ir40-reader
```

2. Install required packages:
```bash
pip install bleak pyautogui
```

## Usage
1. Turn on your FNIRSI-IR40 device and enable Bluetooth
2. Run the script:
```bash
python ble_reader.py
```
3. Select your device from the list of discovered BLE devices
4. Press the measurement button on your FNIRSI-IR40
5. The script will:
   - Display the received measurement
   - After a 3-second delay, simulate typing the measurement value

## Example Output
```
New data received:
Raw HEX: 00 15 02 01 14 00 00 00 00 02 05 14 00 00 07 13 02 06 14 00 00 00 00
Distance: 1.813 m (1813 mm)
```

## License
MIT License - feel free to use this code in your projects.


## Disclaimer
This is an unofficial tool and is not affiliated with FNIRSI. Use at your own risk.