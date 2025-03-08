#!/usr/bin/env python3

import os
import platform
import socket
import psutil
import time

def get_linux_distro():
	"""Get the linux distribution name for Linux"""
	try:
		return platform.freedesktop_os_release().get("PRETTY_NAME", "Unknown")
	except AttributeError:
		try:
			with open("/etc/os-release") as f:
				for line in f:
					if line.startwith("PRETTY_NAME"):
						return line.strip().split("=")[1].strip('"')
		except FileNotFoundError:
			return "Unknown Linux"

def get_uptime():
	"""Get system uptime in hours and minutes."""
	uptime_seconds = time.time() - psutil.boot_time()
	uptime_hours = int(uptime_seconds // 3600)
	uptime_minutes = int((uptime_seconds % 3600) // 60)
	return f"{uptime_hours}:{uptime_minutes}"

def get_system_info():
	print(f"{'='*30} SYSTEM INFO {'='*30}")
	print(f"OS: {get_linux_distro()}")
	print(f"Kernel: {platform.system()} {platform.release()}")
	print(f"Architecture: {platform.architecture()[0]}")
	print(f"Hostname: {socket.gethostname()}")
	print(f"User: {os.getlogin()}")
	print(f"Python Version: {platform.python_version()}")
	print(f"{'='*73}")
	print(f"CPU Cores: {psutil.cpu_count(logical=True)} (logical), {psutil.cpu_count(logical=False)} (Physical)")
	print(f"RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")
	print(f"Uptime: {get_uptime()}")
	print(f"{'='*73}")

if __name__=="__main__":
	get_system_info()
