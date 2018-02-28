from numpy import *
vector1 = mat([1,2,3])
vector2 = mat([4,5,6])
# 欧氏距离
print(sqrt((vector1-vector2)*((vector1-vector2).T)))
# 曼哈顿距离
print(sum(abs(vector1-vector2)))
# 切比雪夫距离
vector2 = mat([4,7,5])
print(abs(vector1-vector2).max())
# 夹角余弦
# cosV12 = dot(vector1,vector2)/(linalg.norm(vector1)*linalg.norm(vector2))
# print(cosV12)
# 汉明距离
matV = mat([[1,1,0,1,0,1,0,0,1],[0,1,1,0,0,0,1,1,1]])
smstr = nonzero(matV[0]-matV[1])
print(shape(smstr[0])[0])

# 杰卡德距离
import scipy.spatial.distance as dist
print(dist.pdist(matV,'jaccard'))