from PIL import Image
from numpy import average, linalg, dot
import numpy as np
from scipy import signal

def robin(img):
    list_edge = []
    k1 = np.array([[1,1,1],[1,-2,1],[-1,-1,-1]])
    img_k1 = signal.convolve2d(img, k1, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k1))
    k2 = np.array([[1,1,1],[-1,-2,-1],[-1,-1,1]])
    img_k2 = signal.convolve2d(img, k2, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k2))
    k3 = np.array([[-1,1,1],[-1,-2,1],[-1,1,1]])
    img_k3 = signal.convolve2d(img, k3, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k3))
    k4 = np.array([[-1,-1,1],[-1,-2,1],[1,1,1]])
    img_k4 = signal.convolve2d(img, k4, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k4))
    k5 = np.array([[-1,-1,-1],[1,-2,1],[1,1,1]])
    img_k5 = signal.convolve2d(img, k5, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k5))
    k6 = np.array([[1,-1,-1],[1,-2,-1],[1,1,1]])
    img_k6 = signal.convolve2d(img, k6, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k6))
    k7 = np.array([[1,1,-1],[1,-2,-1],[1,1,-1]])
    img_k7 = signal.convolve2d(img, k7, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k7))
    k8 = np.array([[1,1,1],[1,-2,-1],[1,-1,-1]])
    img_k8 = signal.convolve2d(img, k8, mode='same', boundary='fill', fillvalue=0)
    list_edge.append(np.abs(img_k8))
    edge = list_edge[0]
    for i in range(len(list_edge)):
        edge = edge*(edge>=list_edge[i]) + list_edge[i]*(edge<list_edge[i])
    return edge

def get_thumbnail(image, size=(1200, 750), greyscale=False):
    image = image.resize(size, Image.ANTIALIAS)
    image = image.convert('L')
    image = robin(image)
    return image

def image_similarity_vectors_via_numpy(image1, image2):
    image1 = get_thumbnail(image1,)
    image2 = get_thumbnail(image2)
    images = [image1, image2]
    vectors = []
    norms = []
    for image in images:
        vector = []
        image = Image.fromarray(image)#将numpy格式转换成Image格式
        for pixel_tuple in image.getdata():
            vector.append(average(pixel_tuple))
        vectors.append(vector)
        norms.append(linalg.norm(vector, 2))
    a, b = vectors
    print(vectors.shape)
    a_norm, b_norm = norms
    print('norm:',a_norm,b_norm)
    res = dot(a / a_norm, b / b_norm)
    return res

image1 = Image.open('./l_1851.jpg')
image2 = Image.open('./r_1851.jpg')
cosin = image_similarity_vectors_via_numpy(image1, image2)
print(cosin)