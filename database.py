import pickle
import numpy as np
from tqdm import tqdm

class database():
    def __init__(self):
        pass

    def loadDatabase(self, path_database):

        with open(path_database, 'rb') as fp:
            database = pickle.load(fp)
        
        list_embed_of_images = []
        
        for i, elem in tqdm(enumerate(database)):
            try:
                image_embedding = np.load(elem['path_embedding'])

                metadata = dict()
                metadata['path_image'] = elem['path_image']
                metadata['image_embedding'] = image_embedding

                list_embed_of_images.append(metadata)
            except:
                continue
        
        print('Database loaded!')
        return list_embed_of_images
