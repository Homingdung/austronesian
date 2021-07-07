import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.decomposition import PCA
dataset = pd.read_excel('./语言研究.xlsx',encoding="utf- 8")
A = dataset.iloc[:,1:18].values
distA = sch.distance.pdist(A,'euclidean')
distB = pd.DataFrame(sch.distance.squareform(distA.round(2)),col umns=[i for i in range(22)],index=[i for i in range(22)])
Z = sch.linkage(A, method ='ward',metric='euclidean') 
fig=plt.figure(figsize=(6,10))
dendrogram = sch.dendrogram(Z,labels =
dataset['language'].values
,orientation='left'
,leaf_rotation=0
               ,leaf_font_size=10
              )
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
fig=plt.figure(figsize=(13.5,20))
method_type=
['single','complete','average','centroid','median','ward
']
hlines_cut=[3.8,6.5,5.5,4.8,5.3,9]
for i in range(len(method_type)):
    ax=fig.add_subplot(2,3,i+1)
    Z = sch.linkage(A, method
=method_type[i],metric='euclidean')
    sch.dendrogram(Z,labels =
dataset['language'].values,leaf_rotation=0
,leaf_font_size=3.5)
 plt.hlines(y=hlines_cut[i],xmin=0,xmax=1000,linestyles=
'dashed')
    plt.annotate('clustering hieght',xy=
(0,hlines_cut[i]),xytext=(30,hlines_cut[i]+0.3)
,color='r',arrowprops=dict(arrowstyle="-
>",color='red',connectionstyle="arc3"))
    plt.title(method_type[i])
plt.show()