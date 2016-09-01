from sklearn.datasets import load_iris
iris = load_iris()
print iris.feature_names
print iris.target_names
print iris.data[0]
print iris.target[0]

# print " full dataset"
# for index in range(len(iris.target)):
#     print "{0}: {1}: {2}".format(index, iris.data[index], iris.target[index])
