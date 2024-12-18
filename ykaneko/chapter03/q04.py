import numpy as np
#Numpyをnpという名前でインポート　短縮形で使える
d = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19,20]])
print(d)
# 2行3列の要素を取得
d1 = d[2,3]
#行列のインデックスは0から始まる.2(3行目)3(4列目)
print(d1)

# 第2列の要素すべてを取得
d2 = d[:,2]
#「:」 はすべての行を意味.array[:, 2]はすべての行の2列目(インデックス2)の要素を取得
print(d2)

# 奇数番目の行の要素すべてを取得
d3 = d[1::2]
#array[1::2] は、1行目から始めて2行ごとに選択した行のすべての要素を取得.奇数番目の行(1行目、3行目)の要素を抽出
print(d3)