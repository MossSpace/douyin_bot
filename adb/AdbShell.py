# -*- coding: utf-8 -*-
import os
import platform
import re
import subprocess


class AdbCmd:

    def __init__(self):
        try:
            adb_path = 'adb'
            subprocess.Popen([adb_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.adb_path = adb_path

        except OSError:
            if platform.system() == 'Windows':
                adb_path = os.path.join('Tools', "adb", 'adb.exe')
                try:
                    subprocess.Popen(
                        [adb_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    self.adb_path = adb_path
                except OSError:
                    pass
            else:
                try:
                    subprocess.Popen(
                        [adb_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                except OSError:
                    pass
            print('请安装 ADB 及驱动并配置环境变量')

    def get_screen(self):
        process = os.popen(self.adb_path + ' shell wm size')
        output = process.read()
        m = re.search(r'(\d+)x(\d+)', output)
        return int(m.group(1)), int(m.group(2))

    def run(self, raw_command):
        print('執行命令: %s' % raw_command)
        command = '{} {}'.format(self.adb_path, raw_command)
        process = os.popen(command)
        output = process.read()
        return output

    def adb_path(self):
        return self.adb_path
