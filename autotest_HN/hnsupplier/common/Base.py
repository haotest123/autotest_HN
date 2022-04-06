from appium import webdriver
from appium.common.exceptions import NoSuchContextException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from common.public_log import Logger
from testdatas import filepath_datas as FD
import datetime
import time
from time import sleep
from selenium.webdriver.support.ui import Select

# from pykeyboard import PyKeyboard


logger=Logger(logger="BasePage").getlog()
class BasePage(object):
    #初始化页面
    def __init__(self,driver):
        # self.kb=Pykeyboard()
        self.driver=driver
        # 进行输入内容
     #一个*是元组，两个*是字典
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info('执行成功',loc)
        except:
            logger.error('执行失败%s',(self,loc))

    def sendkeys(self, text, *loc):
        element = self.find_element(*loc)
        try:
            element.send_keys(text)
            logger.info('执行成功')
            # logger.info('执行成功%s',element.text)
            # logger.info('开始进行输入%s',element.text)
        except:
            logger.error('执行失败%s', (self, loc))

    # 清除文本框:
    def clear(self, *loc):
        element = self.find_element(*loc)
        try:
            element.clear()
            logger.info('清除文本框成功')
        except:
            logger.erron('清除元素未找到%s', (self, loc))

    # 点击元素
    def click(self, *loc):
        element = self.find_element(*loc)
        try:
            element.click()
            logger.info('执行成功')
        except  Exception as e:
            logger.error('执行失败', e)

    # 双击元素
    def doubleclick(self, *loc):
        element = self.find_element(*loc)
        try:
            action_chains = ActionChains(self.driver)
            action_chains.double_click(element).perform()
            logger.info('双击正确')
        except Exception as e:
            logger.error('双击失败',e)

    #长按某个元素
    def touch_action(self,*loc):
        element=self.find_element(*loc)
        try:
            TouchAction(self.driver).long_press(element, duration=5).perform()
            logger.info('长按元素成功')
        except Exception as e:
            logger.info('长按元素失败',e)





    #查找单一元素
    def get_element(self,loc,timeout=40,poll=0.5):
        '''

        :param loc:元素定位
        :param timeout: 默认等待时间
        :param poll: 每0.5s查询一次元素
        :return:
        '''
        logger.info("等待元素{0}".format(loc))
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda  x:x.find_element(*loc))

    # 查找一组元素
    def base_find_elements_loc(self, loc, timeout=40, poll=0.5):
        '''
        :param loc:元素定位
        :param timeout: 默认等待时间
        :param poll: 每0.5s查询一次元素
        :return:
        '''
        try:
            logger.info("查找一组元素{0}".format(loc))
            return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))
        except:
            logger.info("查找元素失败{0}".format(loc))

    # 查找元素列表
    def get_elements(self, loc, timeout=40, poll=0.5):
        '''
        :param loc:元素定位
        :param timeout: 默认等待时间
        :param poll: 每0.5s查询一次元素
        :return:
        '''
        logger.info("查询元素{0}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))


    #鼠标悬停
    def mouse_move(self,order_wait,order_click):
        '''

        :param order_wait:鼠标悬停的等待按钮
        :param order_click: 鼠标悬停的点击按钮
        :return:
        '''
        try:
            WebDriverWait(self.driver,30).until(ec.visibility_of_element_located(order_wait))
            sleep(3)
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(order_click)).perform()
            logger.info('鼠标悬停到：'+str(order_click))
        except:
            logger.info('悬停鼠标的元素不存在')

    #鼠标左键点击
    def mouse_left_click(self,locator):
        '''

        :param locator:
        :return:
        '''
        try:
            #找到元素后，左键点击
            ActionChains(self.driver).context_click(self.driver.find_element(*locator)).perform()
            logger.info('鼠标左键点击成功')
        except:
            logger.info('鼠标左键点击的元素不存在')


        # 鼠标右键点击
        def mouse_right_click(self, locator):
            '''

            :param locator:
            :return:
            '''
            try:
                # 找到元素后，左键点击
                ActionChains(self.driver).click(self.driver.find_element(*locator)).perform()
                logger.info('鼠标左键点击成功')
            except:
                logger.info('鼠标左键点击的元素不存在')



    #等待元素可见，存在返回true
    def isElementExist(self,locator,times=30,poll_frequency=0.5):
        '''

                :param locator: 元素定位
                :param doc: 模块名——页面名称——操作名称
                :param times: 默认30s
                :param poll_frequency:每0.5秒查询一次元素
                :return: None
                '''
        logger.info("等待元素{0}".format(locator))
        flag=True
        try:
            starttime=datetime.datetime.now()
            WebDriverWait(self.driver,times,poll_frequency).until(ec.visibility_of_element_located(locator))
            endtime=datetime.datetime.now()
            logger.info("元素存在，等待时长为：{0}".format(endtime-starttime).seconds)
        except Exception as e:
            logger.info('元素不存在')
            flag=False
        return flag

    #下拉列表，等待元素可见，有元素后直接选择（出入的文本）
    def wait_select_visible_text(self,locator,text,doc,times=30,poll_frequency=0.5):
        '''

        :param locator: 元素定位
        :param text: 选择文本
        :param doc: 模块名——页面名称——操作名称
        :param times: 默认30s
        :param poll_frequency: 每0.5秒查询一次元素
        :return: None
        '''
        logger.info("等待元素{0}".format(locator))
        try:
            #开始等待的时间
            starttime = datetime.datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(ec.visibility_of_element_located(locator))
            sleep(1)
            #下拉列表选择
            Select(self.driver.find_element(*locator)).select_by_visible_text(text=text)
            #结束等待时间
            endtime = datetime.datetime.now()
            logger.info("元素存在，等待时长为：{0}".format(endtime - starttime).seconds)
        except Exception as e:
            logger.error("等待元素可见失败，具体错误：{0}".format(e))
            self.save_screenshots(FD.screenshot_path,doc)
            raise

   #输入文本方法
    def wait_input_text(self,locator,text,doc,times=40,poll_frequency=0.5):
        '''
               :param locator: 元素定位
               :param text:输入的文本值
               :param doc: 模块名——页面名称——操作名称
               :param times: 默认30s
               :param poll_frequency:每0.5秒查询一次元素
               :return: None
        '''
        logger.info("等待元素{0}".format(locator))
        try:
            # 开始等待的时间
            starttime = datetime.datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(ec.visibility_of_element_located(locator))
            # 清空输入框
            self.driver.find_element(*locator).clear()
            #输入框赋值
            self.driver.find_element(*locator).send_keys(text)
            # 结束等待时间
            endtime = datetime.datetime.now()
            logger.info("元素存在，等待时长为：{0}".format(endtime - starttime).seconds)
        except Exception as e:
            logger.error("等待元素可见失败，具体错误：{0}".format(e))
            self.save_screenshots(FD.screenshot_path, doc)
            raise










    #等待元素可见，有元素后直接发出点击事件
    def wait_ele_click(self,locator,doc,times=40,poll_frequency=0.5):
        '''

        :param locator: 元素定位
        :param doc: 模块名——页面名称——操作名称
        :param times: 默认30s
        :param poll_frequency:每0.5秒查询一次元素
        :return: None
        '''
        logger.info("等待元素{0}".format(locator))
        try:
            starttime = datetime.datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(ec.visibility_of_element_located(locator))
            self.driver.find_element(*locator).click()
            endtime = datetime.datetime.now()
            logger.info("元素存在，等待时长为：{0}".format(endtime - starttime).seconds)
        except Exception as e:
            logger.error("等待元素可见失败，具体错误：{0}".format(e))
            self.save_screenshots(FD.screenshot_path,doc)
            raise

    #截图方法
    def save_screenshots(self,file_path,file_name):
        '''
        :param file_path: 存储的路径
        :param file_name: 存储的名字
        :return:
        '''
        #图片名称：时间——页面名称——操作名称.png
        time.sleep(2)
        picture_name=time.strftime('%Y-%m-%d %H-%M-%S',time.localtime())+'_{0}.png'.format(file_name)
        path_name=file_path+'\\'+picture_name
        time.sleep(1)
        self.driver.get_screenshot_as_file(path_name)
        logger.info('保存路径：'+path_name)



























