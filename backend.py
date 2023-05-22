import scrapperpython_large as sc
import Nuralnetwork as mynn
#url = "https://www.booking.com/hotel/gb/the-belmont.en-gb.html"
def process (url):
#        url="https://www.booking.com/hotel/us/the-metric-los-angeles.en-gb.html"
        sc.scrapper(url)
        isinclusive = mynn.mymodel()
        
        print("isinclusive =" + str(isinclusive))
        return isinclusive
#url="https://www.booking.com/hotel/us/the-metric-los-angeles.en-gb.html"
#process(url)
