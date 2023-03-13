import frida
import os
import sys
import serial
import subprocess
from time import sleep

TIMEOUT = 200 # timeout in seconds / 10
RESET_COUNTER = 10 # restart app after X actions

if (len(sys.argv) < 3):
	print("Use: python monitor.py [bundleId of app] [serial device]")
	sys.exit(1)

tmp = os.popen("ps -Af").read()
proccount = tmp.count('iproxy')
if (proccount == 0):
	print("Need to run iproxy (and have 'open' installed on phone)!")
	sys.exit(1)

bundleId = sys.argv[1] # e.g. com.epson.ESCPR01
dev = sys.argv[2] # e.g. /dev/cu.usbserial-0001

def open_app():
	cmd = 'ssh -T -p 2222 root@localhost "open ' + bundleId + '"'
	subprocess.run(cmd, shell=True)

def restart_app():
	cmd = 'frida-ps -U -a | grep ' + bundleId + ' | cut -d " " -f1'
	res = subprocess.run(cmd, shell=True, capture_output=True)
	pid = int(res.stdout.decode())

	cmd = 'frida-kill -U ' + str(pid)
	subprocess.run(cmd, shell=True)

	open_app()

def kill_all():
	cmd = 'frida-ps -U -a | tail -n +4 | cut -d " " -f1'
	res = subprocess.run(cmd, shell=True, capture_output=True)
	pids = res.stdout.decode().split('\n')
	for pid in pids:
		if pid and int(pid) != 0:
			cmd = 'frida-kill -U ' + pid
			subprocess.run(cmd, shell=True)

device = frida.get_usb_device()
s = serial.Serial(dev, baudrate=115200, timeout=0.050)

i = 0 # timeout counter
j = 0 # restart counter
while True:
	i += 1

	if i > TIMEOUT:
		print("Timeout reached. Exiting..")
		sys.exit(2)

	running_app = device.get_frontmost_application()
	if running_app is None or running_app.identifier != bundleId:
		print("App not running. Killing other apps and opening it..")
		kill_all()
		open_app()
		sleep(1)
		continue

	data = s.readall().decode()
	if "Waiting for commands.." in data:
		j +=1
		if (j > RESET_COUNTER):
			print("Restarting app")
			restart_app()
			sleep(2)
			j = 0

		print("Sent commands.. " + str(j))
		s.write("g".encode())
		i = 0 # reset timeout counter
	else:
		if i % 10 == 0:
			print("Waiting for serial device.. " + str(i))

	sleep(0.1)
