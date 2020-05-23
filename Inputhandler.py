
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

import logging
import time 

'''
---------------------------------------------------------------------------
Logger 
formate:- '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
---------------------------------------------------------------------------
'''
'''
---------------------------------------------------------------------------
Logging Initializer
---------------------------------------------------------------------------
'''
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
timestr = time.strftime("%Y%m%d-%H%M%S")
handler = logging.FileHandler('selenium.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
 


def isalert(driver):
    try:
       WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')
       return True
    except Exception as e:
        return False


def moveToElement(driver,xpath):
    
    try:
        element = driver.find_element_by_xpath(xpath)   
        time.sleep(1)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
    except Exception as timout:
        logger.info('%s - %s - %s', "Unable to find the Xpath in readText ",xpath,timout)

def getAttribute(driver, xpath, name):
    try:
        controlClick=driver.find_element_by_xpath(xpath)
        time.sleep(1)
        return controlClick.get_attribute(name)
    except Exception as timout:
        logger.info('%s - %s - %s', "Unable to find the Xpath getAttributess ", xpath,timout)

   
def downArrow(driver, Xpath, value):
#    time.sleep(1)
    processingCheckWait(driver, Xpath, 10)
    time.sleep(1)
    mouseClick(driver, Xpath)
    time.sleep(0.5)
    mouseClickandSendKey(driver, Xpath, value)
    time.sleep(0.5)
    sendKey(driver, Xpath, Keys.ARROW_DOWN)
    sendKey(driver, Xpath, Keys.ENTER)
    
def clear(driver, xpath):
    try:
        controlClick=driver.find_element_by_xpath(xpath)
        controlClick.clear()
    except Exception as timout:
        logger.info('%s - %s - %s', "Unable to find the Xpath clear ",xpath,timout)

def sendKey(driver,controlxpath,value):
    try:
        controlClick=driver.find_element_by_xpath(controlxpath)
        time.sleep(0.5)
        controlClick.send_keys(value)
    except Exception as timout:
        logger.info('%s - %s - %s', "Unable to find the Xpath Send Keys ",controlxpath,timout)
    

def mouseClick(driver,controlxpath):
    try:
        controlClick=driver.find_element_by_xpath(controlxpath)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, controlxpath)))
        controlClick.click()
    except Exception as timout:
        logger.info('%s - %s - %s', "Unable to find the Xpath mouseClick",controlxpath,timout)
        
        
        
def mouseClickandSendKey(driver,controlxpath,value):
    try:
        controlClick=driver.find_element_by_xpath(controlxpath)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, controlxpath)))
        controlClick.click()
        controlClick.clear()
        time.sleep(1)
        controlClick.send_keys(value)
    except Exception as timout:
        logger.info('%s - %s - %s', "Unable to find the Xpath mouseClickandSendKey ",controlxpath,timout)
        

def mouseClickSendKeyandTab(driver,controlxpath,value):
    try:
        time.sleep(0.5)
        controlClick=driver.find_element_by_xpath(controlxpath)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, controlxpath)))
        controlClick.click()
        controlClick.clear()
        time.sleep(1)
        controlClick.send_keys(value)
        controlClick.send_keys(Keys.TAB)
    except Exception as timout:
        logger.info('%s - %s - %s', "Unable to find the Xpath mouseClickSendKeyandTab",controlxpath,timout)
        
def mouseClickSendKeyandEnter(driver,controlxpath,value):
    try:
        time.sleep(0.5)
        controlClick=driver.find_element_by_xpath(controlxpath)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, controlxpath)))
        controlClick.click()
        controlClick.clear()
        time.sleep(1)
        controlClick.send_keys(value)
        time.sleep(1)
        controlClick.send_keys(Keys.ENTER)
    except Exception as timout:
        logger.info('%s - %s - %s', "Unable to find the Xpath mouseClickSendKeyandTab",controlxpath,timout)    
        

#def mouseClickSendKeyandEnter(driver,controlxpath,value):
#    try:
#        controlClick=driver.find_element_by_xpath(controlxpath)
#        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, controlxpath)))
#        controlClick.click()
#        controlClick.clear()
#        time.sleep(1)
#        controlClick.send_keys(value)
#        controlClick.send_keys(Keys.ENTER)
#    except Exception as timout:
#        logger.info('%s - %s - %s', "Unable to find the Xpath mouseClickSendKeyandEnter",controlxpath,timout)

def scroll(driver, offset):
    driver.execute_script("window.scrollBy(0,"+ str(offset)+");")

def scrollToElement(driver, xpath):
    try:
        element = driver.find_element_by_xpath(xpath)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
    except Exception as timout:
        logger.info('%s - %s - %s', "Unable to find the Xpath in scroll to element ",xpath,timout)


#def click(driver, xpath):
#    try:
#        element = driver.find_element_by_xpath(xpath)
#        actions = ActionChains(driver)
#        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
#        actions.click(element).perform()
#    except Exception as timout:
#        actions.click(element).perform()
#        logger.info('%s - %s - %s', "Unable to find the Xpath in Click ",xpath,timout)

#def sendKeyActionChain(driver, value):
#    try:
#        actions = ActionChains(driver)
#        actions.send_keys(value).perform()
#    except Exception as timout:
#        logger.info('%s - %s - %s', "Unable to sendkeys using action chains ",timout)

#def doubleClick(driver, xpath):
#    try:
#        element = driver.find_element_by_xpath(xpath)
#        actions = ActionChains(driver)
#        actions.double_click(element).perform()
#    except Exception as timout:
#        logger.info('%s - %s - %s', "Unable to find the Xpath in Click ",xpath,timout)

#def scrollToElementandClick(driver, xpath):
#    try:
#        element = driver.find_element_by_xpath(xpath)
#        actions = ActionChains(driver)
#        actions.move_to_element(element).perform()
#        waitTillClickable(driver, xpath)
#        actions.click(element).perform()
#    except Exception as timout:
#        logger.info('%s - %s - %s', "Unable to find the Xpath in scrollToElementandClick ",xpath,timout)

'''
Reads the inner text of the xpath given
'''
def readText(driver, xpath):
    try:
        element = driver.find_element_by_xpath(xpath)
        return element.text
    except Exception as timout:
        logger.info('%s - %s - %s', "Unable to find the Xpath in readText ",xpath,timout)
        


def readText_err(driver, xpath):
    try:
        element = driver.find_element_by_xpath(xpath)
        return element.text
    except Exception as timout:
        logger.info('%s - %s - %s', "Unable to find the Xpath in readText ",xpath,timout)
        raise

'''
---------------------------------------------------------------------------
Important methods to wait until loading done
---------------------------------------------------------------------------
'''   
  
'''
----------------------------------------------------------------------
Waits for timeout sec for the element with the xpath to be displayed
----------------------------------------------------------------------
'''    
def processingCheckWait(driver,controlxpath, timeout):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, controlxpath)))
        # WebDriverWait(driver, timeout).until(lambda s: s.find_element(By.XPATH, controlxpath).is_displayed())
    except Exception as e:
        logger.info('%s - %s - %s', "Time out exception in finding of in processingcheckwait ",controlxpath, e)


'''
--------------------------------------------------------
Waits till the element with the xpath is clickable
if element is not clickable after 10s returns false
--------------------------------------------------------
'''
def waitTillClickable(driver, xpath):
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        return True
    except Exception as timout:
        logger.info('%s - %s - %s', "Unable to find the Xpath in wait till clickable to element ",xpath,timout)
        return False

'''
-----------------------------------------
Checks whether the xpath is displayed.
If xpath is displayed returns true.
-----------------------------------------
'''
def isXpathDisplayed(driver,elementXpath, timeout):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, elementXpath)))
        logger.info('%s - %s', "Content Displayed  ",elementXpath)
        return True
    except Exception as e:
 #       logger.info('%s - %s - %s', "Unable to find the Xpath in is xpath displayed ",elementXpath,e)        
        return False

        
