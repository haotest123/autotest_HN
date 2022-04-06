from HTMLTestRunner import HTMLTestRunner


import os
import sys

import getopt
import unittest
import time

current_directory=os.path.dirname(os.path.abspath(__file__))

root_path=os.path.abspath(os.path.dirname(current_directory)+os.path.sep+'.')

sys.path.append(root_path)

opts,args=getopt.getopt(sys.argv[1:],'p:')


pattern=opts[0][1]

discover=unittest.defaultTestLoader.discover('./first_execute/',pattern=pattern)

dir_path='../report'
now=time.strftime('%Y-%m-%d %H-%M-%S')

report_path=dir_path+now+'result.html'

with open(report_path,'wb') as f:
    runner=HTMLTestRunner(stream=f,verbosity=2,title='测试报告',description='用例执行详细信息')
    runner.run(discover)
f.close()




#python test_run.py -p test*.py














































