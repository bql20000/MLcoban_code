import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

img = mpimg.imread('/home/long/Code/MLcoban/Lesson_5/girl3.jpg')
plt.imshow(img)
imgplot = plt.imshow(img)
#plt.axis('off')
#plt.show() 
print(img)
X = img.reshape(img.shape[0] * img.shape[1], img.shape[2])

for K in [3]:
    kmeans = KMeans(n_clusters=K).fit(X)
    label = kmeans.predict(X)

    img4 = np.zeros_like(X)
    # replace each pixel by its center
    for k in range(K):
        img4[label == k] = kmeans.cluster_centers_[k]
    # reshape and display output image
    img5 = img4.reshape((img.shape[0], img.shape[1], img.shape[2]))
    print(kmeans.cluster_centers_)
    plt.imshow(img5, interpolation='nearest')
    plt.axis('off')
    plt.show()