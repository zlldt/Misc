import datetime
import time
import os
import win32com.client


def CheckProcExistsByPN(process_name):
    try:
        WMI = win32com.client.GetObject('winmgmts:')
        processCodeCov = WMI.ExecQuery(
            'select * from Win32_Process where Name="%s"' %
            process_name)
    except Exception:
        print(process_name, ' ERROR')
    if len(processCodeCov) > 0:
        print(process_name, ' EXIST')
        return 1
    else:
        print(process_name, 'DOES NOT EXIST')
        return 0


def main():
    filename = 'JSHISSRVERROR.log'
    while True:
        time.sleep(2)
        now = datetime.datetime.now()
        print(now, 'check')
        if CheckProcExistsByPN('werfault.exe'):
            closecommand = 'taskkill /f /IM werfault.exe'
            os.system(closecommand)
            opencommand = 'd:\HISSRV\JSHISSRV.exe'
            os.system(opencommand)
            f1 = open(filename, 'a')
            f1.write(str(now)+'\n')
            f1.close()


if __name__ == "__main__":
    main()
