import os
import glob # With python 3.5+
import uuid
import pickle
from tqdm import tqdm
import numpy as np
from PIL import Image

from features import extract_features

def get_list_path(path):
    exts = ['*.jpg', '*.JPG', '*.jpeg', '*.JPEG', '*.png', '*.PNG']
    list_path = []
    for ext in exts:
        list_ext = glob.glob(os.path.join(path, '**/'+ext), recursive=True)
        list_path.extend(list_ext)
    return list_path

class index():
    def __init__(self):
        # Init model
        self.model = extract_features()
    
    def indexing(self, path_images, path_embeddings, path_database):

        list_path_images = get_list_path(path_images)

        database = []

        for i, path_image in tqdm(enumerate(list_path_images)):
            try:
                image = Image.open(path_image)

                image_embedding = self.model.extract_image_features(image)
                
                name_embedding = str(uuid.uuid4())
                path_embedding = os.path.join(path_embeddings, name_embedding) + '.npy'
                np.save(path_embedding, image_embedding)

                metadata = {
                'path_image': path_image,
                'path_embedding': path_embedding
                }

                database.append(metadata)
            except:
                continue
        
        with open(path_database, 'wb') as fp:
            pickle.dump(database, fp)
        
        print('Complete indexing!')


if __name__ == '__main__':
    index().indexing(path_images='./Corel-1000/', path_embeddings='./embeddings/', path_database='./database/Corel-1000')
    print('DONE!')
