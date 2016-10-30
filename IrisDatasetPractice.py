from sklearn import datasets, svm
import matplotlib.pyplot as plt
import numpy as np

# iris = datasets.load_iris()
# print iris.data[:-2]
# print len(iris.data[:-2])
# print iris.target
# print len(iris.target)

digits = datasets.load_digits()
#print digits.data
# print len(digits.data)
# print len(digits.target)
# print len(digits.data[0])
# print digits.images[0]

a = np.array(digits.data[0])
#print a
#print len(digits.data)
#print len(digits.images)
b = a.reshape((-1,8))
#print b

plt.grid(True)
plt.axis([0,8,0,8])
plt.plot([4,6,4,2,4], [6,4,2,4,6])
plt.show()
# for data_image in digits.data:
#     data_array = np.array(data_image)
#     data_reshape = data_array.reshape((-1, 8))
#     plt.imshow(data_reshape, cmap=plt.cm.gray_r, interpolation='nearest')
#     plt.show()

# clf = svm.SVC(gamma=0.001, C=100.)
# clf.fit(digits.data[:-4], digits.target[:-4])
# print clf.predict(digits.data[-2])
# image = digits.images[-2]
# images_labels = list(zip(digits.images, digits.target))
# for index, (image, label) in enumerate(images_labels[:4]):
#     plt.subplot(2,4,index+1)
#     plt.axis('off')
#     plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
#     plt.title(label)
# plt.axis('off')
# plt.imshow(b, cmap=plt.cm.gray_r, interpolation='nearest')
# plt.show()