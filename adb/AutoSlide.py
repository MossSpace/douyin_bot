import time
from adb.AdbShell import AdbCmd

adb = AdbCmd()


def auto_slide():
    width, height = adb.get_screen()

    slide_length = height / 2.5
    x_p1 = x_p2 = width / 2
    y_p2 = height / 2
    y_p1 = y_p2 + slide_length
    duration = 200
    cmd = 'shell input swipe %s %s %s %s %s' % (x_p1, y_p1, x_p2, y_p2, duration)
    adb.run(cmd)
    time.sleep(1.5)


try:
    while True:
        auto_slide()
        time.sleep(1)
except KeyboardInterrupt:
    adb.run('kill-server')
    exit(0)
