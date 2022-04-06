

import os

class KillBrower:

    def KillBrower(self,DriverType):

        #判断启动浏览器
        if DriverType=='IE':
            # pass
            #杀死浏览器和驱动进程
            self.kill("iexplore.exe")
            self.kill('IEDriverServer.exe')

        elif DriverType=='Firefox':
            self.kill("Firefox.exe")
            self.kill('geckodriver.exe')

        elif DriverType == '360':
            self.kill("360se.exe")
            self.kill('chromedriver.exe')

        else:
            self.kill("Chrome.exe")
            self.kill('chromedriver.exe')
















    @staticmethod
    def kill(driver_name):
        '''
        杀死浏览器和驱动进程，减少资源占用，提高运行效率
        :param driver_name:
        :return:
        '''
        try:
            os.system('taskkill /f /im %s'% driver_name)
            return True
        except Exception as e:
            return False





















