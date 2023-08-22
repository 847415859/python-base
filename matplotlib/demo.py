from matplotlib import pyplot as plt

if __name__ == '__main__':
    # 准备数据
    x = [-3, 5, 7]
    y = [10, 2, 5]

    # 创建画布
    plt.figure(figsize=(15, 3))
    # plot绘图
    plt.plot(x, y)
    # 设置x轴和y轴的取值范围
    plt.ylim(0, 10)
    plt.xlim(-3, 8)
    # 设置x轴和y轴的标签
    plt.xlabel('X Axis', size=20)
    plt.ylabel('Y Axis')
    # 设置标题
    plt.title('Line Plot', size=30)

    plt.show()