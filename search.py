import os
import numpy as np
from scipy.spatial import distance
from PIL import Image

from features import extract_features
from index import index

class query():
    def __init__(self):
        self.model = extract_features()
        self.database = index().loadDatabase()
    
    def extract(self, input_data):
        try:
            if type(input_data) is str:
                features = self.model.extract_text_features(input_data)
            else:
                features = self.model.extract_image_features(input_data)
            
            return features
        
        except:
            print('Input data is not an image or a text string!!!')
    
    def search(self, input_data, n_result=10):
        input_features = self.extract(input_data)

        list_results = []

        for elem in self.database:
            elem_result = dict()
            elem_result['path_image'] = elem['path_image']

            # Calculate similarity
            elem_result['distance'] = distance.cosine(input_features, elem['image_embedding'])

            list_results.append(elem_result)
        
        #list_results.sort(key=lambda x:x['distance'])
        sorted_results = sorted(list_results, key=lambda x:x['distance'])

        return sorted_results[:n_result]

# Check search results
query = query()

input_data = 'a herd of elephants'

results = query.search(input_data=input_data)

for elem in results:
    print('\nimage name: ', elem['path_image'])