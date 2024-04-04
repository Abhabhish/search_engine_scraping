import numpy as np
import requests
from skimage import io, img_as_float
from skimage.metrics import structural_similarity as ssim
from skimage.color import rgb2gray

def download_image(url):
    response = requests.get(url)
    image = io.imread(response.content, plugin='imageio')
    return img_as_float(image)

from skimage.transform import resize

def compare_images(image1, image2):
    # Resize the second image to match the dimensions of the first
    image2_resized = resize(image2, image1.shape[:2], anti_aliasing=True)
    
    # Convert images to grayscale
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2_resized)
    
    # Compute SSIM between the two images
    similarity_index, _ = ssim(gray_image1, gray_image2, full=True, data_range=1)
    return similarity_index


# Download images
url1 = 'https://search.pstatic.net/sunny/?src=https%3A%2F%2Fi.pinimg.com%2F736x%2F5c%2Fe7%2Fa8%2F5ce7a8d5f5ed93fe6379e2ba84560b1e.jpg'
url2 = 'https://articlebucketgts.s3.ap-south-1.amazonaws.com/test/W4PHDI_12403.jpg'
image1 = download_image(url1)
image2 = download_image(url2)

# Compare images
similarity = compare_images(image1, image2)
print(f"Similarity: {similarity * 100:.2f}%")








