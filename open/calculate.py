import numpy as np

mu = 60
# Natural frequency
def natural_frequency(k,m):
    fn = (1 / (2 * np.pi)) * np.sqrt(k / m)
    return fn


ax = 2

ay = 2

geox = 0.15

geoy = 0.15

# 輪胎自然頻率計算
# =============================================

fnt = natural_frequency(240000,mu) # 對於黃夏這邊應該是彈簧並聯所以理論需要加入懸吊剛性
print("tire natural frequency : ",fnt)
print("tire fn need to be 5 times spring fn !!")