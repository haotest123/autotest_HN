from selenium import webdriver

class GetDriver:
    #声明变量
    __web_driver=None

    @classmethod
    def get_web_driver(cls,url):
        #判断是否为空
        if cls.__web_driver is None:
            #获取浏览器
            cls.__web_driver=webdriver.Ie()
            #最大化浏览器
            cls.__web_driver.maximize_window()
            #打开url
            cls.__web_driver.get(url)
        #返回driver
        return cls.__web_driver

    #退出driver方法
    @classmethod
    def quit_web_driver(cls):
        #判断driver不为空
        if cls.__web_driver:
            cls.__web_driver.quit()
            cls.__web_driver=None
























