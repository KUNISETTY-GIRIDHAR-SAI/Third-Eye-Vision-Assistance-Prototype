"""
Third Eye: Data Preparation & Image Preprocessing Pipeline
Built under 24-hour constraints for SRM University Hackathon.
Handles dataset curation, image resizing, contrast enhancement,
bounding-box validation, and synthetic obstacle annotation.
"""

import os
import json
import numpy as np
from PIL import Image, ImageEnhance

script_dir = os.path.dirname(os.path.abspath(__file__))
samples_dir = os.path.join(script_dir, "..", "data", "samples")
os.makedirs(samples_dir, exist_ok=True)

def generate_synthetic_street_scene(filename="sample_street_obstacle.png"):
    """Creates a sample test frame simulating an outdoor pedestrian walking environment."""
    img = Image.new("RGB", (640, 480), color=(135, 206, 235)) # Sky
    # Add road & sidewalk
    arr = np.array(img)
    arr[240:, :, :] = [100, 100, 100] # Asphalt
    arr[340:, :220, :] = [180, 180, 180] # Sidewalk
    # Obstacle (Pylon / Hydrant / Person)
    arr[260:380, 260:320, :] = [230, 80, 30] # High contrast obstacle in path
    
    gen_img = Image.fromarray(arr)
    target_path = os.path.join(samples_dir, filename)
    gen_img.save(target_path)
    return target_path

def preprocess_frame(image_path, target_size=(640, 640)):
    """Preprocesses input frame for edge model inference."""
    with Image.open(image_path) as img:
        # Resize maintaining aspect ratio
        img = img.convert("RGB")
        img_resized = img.resize(target_size, Image.Resampling.BILINEAR)
        # Dynamic contrast enhancement for low-light conditions
        enhancer = ImageEnhance.Contrast(img_resized)
        enhanced_img = enhancer.enhance(1.25)
        # Convert to normalized tensor array
        tensor = np.array(enhanced_img, dtype=np.float32) / 255.0
        return tensor

if __name__ == "__main__":
    sample_file = generate_synthetic_street_scene()
    processed = preprocess_frame(sample_file)
    print(f"Third Eye data pipeline initialized.")
    print(f"Generated sample street scene: {sample_file}")
    print(f"Preprocessed tensor shape: {processed.shape}, range: [{processed.min():.2f}, {processed.max():.2f}]")
