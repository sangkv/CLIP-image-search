import os
import numpy as np
from PIL import Image
from scipy.spatial import distance

from database import database
from features import extract_features

class search():
    def __init__(self, path_database):
        self.database = database().loadDatabase(path_database)
        self.model = extract_features()
        print('model loaded!\n')
    
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

        for metadata in self.database:
            elem = dict()
            elem['path_image'] = metadata['path_image']

            # Calculate similarity
            elem['distance'] = distance.cosine(input_features, metadata['image_embedding'])

            list_results.append(elem)
        
        #list_results.sort(key=lambda x:x['distance'])
        sorted_results = sorted(list_results, key=lambda x:x['distance'])

        return sorted_results[:n_result]


if __name__ == '__main__':
    # TEST
    machine = search('./database/Corel-1000')

    # TEST 1: Seach by text
    input_data = 'flowers'

    results = machine.search(input_data=input_data)

    for elem in results:
        print('image name: ', elem['path_image'])
    
    # TEST 2: Search by image
    input_data = Image.open('./doc/a.jpg')

    results = machine.search(input_data=input_data)

    print('\n\n')
    for elem in results:
        print('image name: ', elem['path_image'])

    # TEST 3: Similarity test
    king = machine.extract('king')
    man = machine.extract('man')
    woman = machine.extract('woman')

    queen = machine.extract('queen')

    result = king - man + woman
    similarity =  1 - distance.cosine(queen, result) # Cosine similarity

    print('\n\nCosine similarity = ', similarity)

