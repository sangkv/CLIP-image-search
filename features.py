import torch
import clip 
import numpy as np

class features():
    def __init__(self, model="ViT-B/32"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.preprocess = clip.load(model, device=self.device)

    def extract_image(self, image):
        image = self.preprocess(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            image_features = self.model.encode_image(image)
        
        return image_features

    def extract_text(self, text_list):
        text = clip.tokenize(text_list).to(self.device)

        with torch.no_grad():
            text_features = self.model.encode_text(text)
        
        return text_features
    
    def classifier(self, img, text_list):
        image = self.preprocess(img).unsqueeze(0).to(self.device)
        text = clip.tokenize(text_list).to(self.device)
        with torch.no_grad():
            logits_per_image, logits_per_text = self.model(image, text)

            probs = logits_per_image.softmax(dim=-1).cpu().numpy()
        
        idx = np.argmax(probs)
        prob = np.max(probs)

        return idx, prob


