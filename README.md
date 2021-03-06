# Todoist List Printer Pi

Raspberry Pi based thermal paper list printer using python and the Todoist API.

## Hardware

### Test and Install Printer

Run the following commands in a terminal after connecting Rx/Tx and GND from the TTL thermal printer to a raspberry pi. Ensure you have enabled serial output in raspi-config.

```
stty -F /dev/serial0 9600
echo -e "This is a test.\\n\\n\\n" > /dev/serial0
```

Enter the correct serial baud rate in the first line. This can be found by holding down the printer button during power up, it will print a self test.

#### Install ESCPOS library and dependencies

```
sudo apt-get install python3 python3-setuptools python3-pip libjpeg8-dev libopenjp2-7 libtiff5
sudo pip3 install --upgrade pip
sudo pip3 install python-escpos
```

## How To Use

1. Ensure you have python3 installed and working correctly

2. Install requirements using the following command:

`pip3 install -r requirements.txt`

3. Copy config-sample.py to a new file called config.py. Populate with your Todoist API token and which projects you want to associate with each button action.

4. Test by running the following from the project directory.

`python3 main.py`

5. Add as a service so the script will run on startup

```
cd /lib/systemd/system/
sudo nano listprinter.service
```

_Copy in from example file_

```
sudo chmod 644 /lib/systemd/system/listprinter.service
chmod +x /home/pi/list-printer-pi/main.py
sudo systemctl daemon-reload
sudo systemctl enable listprinter.service
sudo systemctl start listprinter.service
```

6. Reboot and test
