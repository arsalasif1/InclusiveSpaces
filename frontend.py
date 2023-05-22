from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import backend as bk


driver =webdriver.Firefox()
driver.get("https://www.booking.com")



previous_url=""
isinclusive =-1



 
while(True):
        ######### Remove Jumps to new tabs #############
        element1=driver.find_elements(By.TAG_NAME, 'a')
        for e in element1:
                try:
                   driver.execute_script("arguments[0].removeAttribute('target')",e)
                except:
                   pass
          ##############################################
        
        try:
                element=driver.find_element(By.CSS_SELECTOR, ".d2fee87262")   
                Nameofhotel =element.text 
                isinclusive = int(isinclusive)
                sleep(1)
                if(isinclusive<0):
                        if(element.text.find("(Loading)")<0):
                                        original_name = element.text
                                        Nameofhotel="'"+ element.text + " (Loading)" +"'"
                        if("'"+element.text+"'"!=Nameofhotel):
                                driver.execute_script("arguments[0].innerText = " + Nameofhotel, element)
                                driver.execute_script("arguments[0].style.color = 'Yellow'", element)
                                print(element.text)          
                elif(isinclusive<1):
                        if(element.text.find("(NON-Inclusive Space)")<0):
                                Nameofhotel="'"+ original_name + " (NON-Inclusive Space)" +"'"
                        if("'"+element.text+"'"!=Nameofhotel):
                                driver.execute_script("arguments[0].innerText = " + Nameofhotel, element)
                                driver.execute_script("arguments[0].style.color = 'RED'", element)
                                print(element.text)
                else:
                        if(element.text.find("(Inclusive Space)")<0):
                                Nameofhotel="'"+ original_name + " (Inclusive Space)" +"'"
                        if("'"+element.text+"'"!=Nameofhotel):
                                driver.execute_script("arguments[0].innerText = " + Nameofhotel, element)
                                driver.execute_script("arguments[0].style.color = 'Green'", element)
#                                print(element.text)
                sleep(1)
                if(len(element.text)>0 and previous_url!=driver.current_url):
                        isinclusive = -1
                        isinclusive = bk.process(driver.current_url)
                        previous_url=driver.current_url
                           
                        
        except:
         pass


