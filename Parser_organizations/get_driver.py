from selenium import webdriver
from time import sleep
import random
from selenium.webdriver.support.ui import WebDriverWait
import os

# from check_proxy import ProxyCheck


class GetDriver(object):

    def __init__(self, url):
        self.url = url
        # self.proxy_ag = ProxyCheck()
        # self.proxy = self.proxy_ag.get_proxy()
        # self.user_agent = self.proxy_ag.get_user_agent()

    def get_driver(self):
        #
        #driver = webdriver.Chrome()
        #driver.wait = WebDriverWait(driver, sleep(random.uniform(3, 6)))
        # driver.get(self.url)
        #return driver



        fp = webdriver.FirefoxProfile()
        mime_types = "application/pdf,application/vnd.adobe.xfdf,application/vnd.fdf,application/vnd.adobe.xdp+xml"
        fp = webdriver.FirefoxProfile()
        # Proxy set
        # fp.set_preference("network.proxy.type", 1)
        # fp.set_preference("network.proxy.http", self.proxy['http'].strip().split(':')[0])
        # fp.set_preference("network.proxy.http_port", int(self.proxy['http'].strip().split(':')[1]))
        # fp.set_preference("network.proxy.socks", self.proxy['http'].strip().split(':')[0])
        # fp.set_preference("network.proxy.http_socks", int(self.proxy['http'].strip().split(':')[1]))
        # fp.set_preference("general.useragent.override", self.user_agent)
        # print(self.proxy['http'].strip().split(':')[0])
        # print(int(self.proxy['http'].strip().split(':')[1]))
        # print(self.user_agent)

        fp.set_preference("browser.download.folderList", 2)
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        dir = str(os.path.join(os.getcwd())).replace('\\', '\\\\')
        print(dir)
        fp.set_preference("browser.download.dir", dir)
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", mime_types)
        fp.set_preference("plugin.disable_full_page_plugin_for_types", mime_types)
        fp.set_preference("pdfjs.disabled", True)
        fp.update_preferences()
        driver = webdriver.Firefox(firefox_binary=r'C:\Program Files\Mozilla Firefox\firefox.exe', firefox_profile=fp)
        driver.wait = WebDriverWait(driver, sleep(random.uniform(6, 9)))
        driver.get(self.url)
        return driver
