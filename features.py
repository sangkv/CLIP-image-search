import torch
import clip 

class extract_features():
    def __init__(self, model='ViT-B/32'):
        # Load the model
        self.DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model, self.preprocess = clip.load(model, device=self.DEVICE)

    def extract_image_features(self, image):
        # Prepare the image
        image_input = self.preprocess(image).unsqueeze(0).to(self.DEVICE)

        # Calculate features of the image
        with torch.no_grad():
            image_features = self.model.encode_image(image_input)
        
        # Normalize
        image_features /= image_features.norm(dim=-1, keepdim=True)

        return image_features

    def extract_text_features(self, list_text):
        # Prepare the text
        text_inputs = clip.tokenize(list_text).to(self.DEVICE)

        # Calculate features of the image
        with torch.no_grad():
            text_features = self.model.encode_text(text_inputs)
        
        # Normalize
        text_features /= text_features.norm(dim=-1, keepdim=True)

        return text_features
