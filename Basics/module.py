# Author:Leva
import sys

from gevent import os

print(sys.path)     # 打印环境变量


test = os.system("ls")  # 执行命令，不保存结果
print(test)