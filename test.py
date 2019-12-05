from pywinauto.application import Application
import time
app = Application().start(r"7z1900-x64.exe")
time.sleep(1)
app['Dialog']['InstallButton'].click()
time.sleep(1)
app['Dialog']['否(&N)'].click()
time.sleep(1)
app['Dialog']['Close'].click()
