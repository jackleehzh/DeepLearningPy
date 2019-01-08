split(ary, indices_or_sections, axis=0) 
函数功能：
把数组从左到右按顺序切分 
参数说明： 
ary，要切分的数组 
indices_or_sections，如果该参数是一个整数n，就是把数组ary平均切分成n份；如果该参数是一个数组a，则以参数数组a中的元素为轴切分数组ary（左开右闭） 
axis，表示沿哪个维度切分数组。默认值为0，代表横向切分ary，相当于hsplit；当其为1时，代表纵向切分ary，相当于vsplit。

特殊用法举例：
x, y = np.split(data, (4,), axis=1)
把数据集data中的所有数据在第四、五列之间分割，这在机器学习中分离标签是经常使用。

另外，使用split平均切分数组时，如果不能均分会报如下错误：
ValueError: array split does not result in an equal division
此时可用 array_split代替 split
