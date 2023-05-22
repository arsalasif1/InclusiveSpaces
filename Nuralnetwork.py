import torch
import numpy as np
import time


#data = np.loadtxt('ImagesLink.txt', dtype=str)#, delimiter='\n'
#print(data)




# Weights
#weights = 'best.pt'

## Model
#model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # or yolov5n - yolov5x6, custom
#model2 = torch.hub.load("yolov5", "custom",path=weights,source='local')  # or yolov5n - yolov5x6, custom

#model.eval()
### Images
#img = "index.jpeg"  # or file, Path, PIL, OpenCV, numpy, list

## Inference
#results = model(img)

## Results
##results.show()  # or .show(), .save(), .crop(), .pandas(), etc.
#results.show()
#print(results.pandas().xyxy[0].name)
weights = 'best.pt'
model2 = torch.hub.load("yolov5", "custom",path=weights,source='local')  # or yolov5n - yolov5x6, custom
model2.classes = [2] #for grabbars only

def modeltwo(img):
        k=0
        results = model2(img)
#        results.show()
        if len(results.pandas().xyxy[0].name)>0:
#                print(results.pandas().xyxy[0].name)
                for i in range(len(results.pandas().xyxy[0].name)):
                        if results.pandas().xyxy[0].name[i]=='Grabbar':
#                                print('a')
                                results.show() #uncomment this to show the images
                                k+=1
                                print(img)
#                                break
                if k>2:         #set this to the min number of garbbars detected               
                        return True
                else:
                        return False
                                



def mymodel():
        inclusive=0
        data = np.loadtxt('ImagesLink.txt', dtype=str)#, delimiter='\n'
#        weights = 'best.pt'
        model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # or yolov5n - yolov5x6, custom
        for i in range(len(data)):
                img = data[i]
#                print(i)
                results = model(img)

                if len(results.pandas().xyxy[0].name)>0:
#                        print(results.pandas().xyxy[0].name)
                        for j in range(len(results.pandas().xyxy[0].name)):
#                                print(j)
                                if ((results.pandas().xyxy[0].name[j]=='toilet') or (results.pandas().xyxy[0].name[j] == 'sink')) : #or (results.pandas().xyxy[0].name[j] =='bed')): 
                                        print(results.pandas().xyxy[0].name)
                                        print(img)
                                        if(modeltwo(img)):
                                            inclusive+=1    

                                        break
        return inclusive
                        
                

