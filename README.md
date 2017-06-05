# UAC Bypass in Windows 10 using Fodhelper.exe
- fodhelper.exe looks for “HKCU:\Software\Classes\ms-settings\shell\open\command”, by default this key does not exist in Windows 10.
- If it exists then it looks for "HKCU:\Software\Classes\ms-settings\Shell\Open\command\DelegateExecute"
- If it finds it, “HKCU:\Software\Classes\ms-settings\shell\open\command” will get executed
