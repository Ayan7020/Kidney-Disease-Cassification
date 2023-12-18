import numpy as np
import tensorflow
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os 


class PredictionPipeline:
    def __init__(self,filename):
        self.filename = filename
        self.model = load_model(os.path.join("artifacts","training","model.h5")) 
        
    def predict(self): 
        imagename = self.filename
        test_image = image.load_img(imagename,target_size=(150,150))  
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image,axis=0)
        result = np.argmax(self.model.predict(test_image),axis=1)
        print(result) 
        
        if result[0]==0:
            prediction = "Cyst"
            return [{ "image" : prediction}]
        elif result[0]==1:
            prediction = "Normal"
            return [{ "image" : prediction}]
        elif result[0]==2:
            prediction = "Stone"
            return [{ "image" : prediction}]
        elif result[0]==3:
            prediction = "Tumor"
            return [{ "image" : prediction}]
        
        
        
            
        
  
        
        
            

