import os
import psutil
import ctypes
import subprocess
import ctypes.wintypes

print("Press Enter to inject")
os.system("pause >Nul")
os.system("inject.exe -p example.exe -f example.dll")
