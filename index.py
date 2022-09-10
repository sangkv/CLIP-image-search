import os
import uuid
import numpy as np
from PIL import Image

from features import extract_features

class index():
    def __init__(self):
        #self.model = extract_features()
        pass
    
    def indexing(self, path_images='./Corel-1000/', path_embeddings='./embeddings/'):
        self.model = extract_features()

        self.list_of_image_names = os.listdir(path_images)

        for image_name in self.list_of_image_names:
            image = Image.open(os.path.join(path_images, image_name))
            
            image_embedding = self.model.extract_image_features(image)

            name = image_name.split('.')[0]

            np.save(path_embeddings+'/'+name+'.npy', image_embedding)
        print('DONE!')
    
    def loadDatabase(self, path_images='./Corel-1000/', path_embeddings='./embeddings/'):
         
        self.list_of_embedding_names = os.listdir(path_embeddings)

        database = []
         
        for embedding_name in self.list_of_embedding_names:
            name = embedding_name.split('.')[0]
            image_embedding = np.load(os.path.join(path_embeddings, embedding_name))

            elem = dict()
            elem['path_image'] = path_images+'/'+name+'.jpg'
            elem['image_embedding'] = image_embedding

            database.append(elem)
        
        print('DONE')
        return database

if __name__ == '__main__':
    A = index()
    A.indexing()
