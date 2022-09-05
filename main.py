import torch
import clip
from PIL import Image
from features import features

# Load model
model = features()

# Data
image = Image.open('data/d.jpg')
categori = ['a man', 'a woman', 'flowers', 'a house', 'a little girl', 'A flock of birds', 'a bird']

# Classification
idx, prob = model.classifier(image, categori)

print('result: ', categori[idx])
print('prob: ', prob)

print(clip.available_models())