import urllib.request
import numpy as np

#open('foo2.csv', 'w').close() #clear file
#f=open('foo2.csv','a') #open file in append mode
def scrapper(url):
        f = open("ImagesLink.txt", "w")


#        html = urllib.request.urlopen("https://www.booking.com/hotel/gb/the-belmont.en-gb.html")
        html = urllib.request.urlopen(url)
        mybytes = html.read()

        mystr = mybytes.decode("utf8")
        html.close()
        #mystr=mystr[mystr.find('large_url:'):mystr.find('/body')]
        #print(mystr)
        #mystr="kkk bbb bbcccccddddeee bbb "
        i=0
        #print(mystr.find('bbb'))
        mystr=mystr[mystr.find('hotelPhotos:',mystr.find('large_url:'))+4:-1]
        for i in range(1000):
        #        print(mystr.find('.jpg',mystr.find('large_url:')))
                filtered = mystr[mystr.find('large_url:'):mystr.find('\'',(mystr.find('large_url:')+100))]
#                print(filtered)
                if(filtered):
                        print(filtered[filtered.find('large_url:')+12:mystr.find('\'',mystr.find('large_url:')+100)+5])
                        
                        if(filtered.find('xdata')>0):
        #                        print(filtered[filtered.find('large_url:')+12:mystr.find('.')+4])
                                f.write(filtered[filtered.find('large_url:')+12:mystr.find('\'',mystr.find('large_url:')+100)+5])
                                f.write('\n')
                mystr=mystr[mystr.find('\'',mystr.find('large_url:')+100)+4:-1]

        f.close()
