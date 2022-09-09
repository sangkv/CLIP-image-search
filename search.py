from PIL import Image
from features import extract_features

# Load model
model = extract_features()

# extract
image = Image.open('Corel-1000/16.jpg')
image_features = model.extract_image_features(image)

text = 'man'
text_features = model.extract_text_features(text)

print('image features: ', image_features)
print('features_text: ', text_features)
