import numpy as np
import matplotlib.pyplot as plt

# 生成 10 个随机数作为示例数据
A = [20774440468.0, 20481699736.0, 20787315628.0, 20693141804.0, 20706712748.0]
B = [18126338068.0, 18042749092.0, 18105352620.0, 17997620572.0, 18102993404.0]

# 创建一个包含 10 个子图的图像
fig, axs = plt.subplots(2, 5, figsize=(15, 6))

# 遍历 A 和 B 列表中的值，绘制矩阵图
for i, (a, b) in enumerate(zip(A, B)):
    row = i // 5
    col = i % 5

    # 创建一个 2x2 的矩阵，对角线元素为0，其他元素根据A[i]和B[i]确定
    matrix = np.array([[0, a], [b, 0]])

    # 绘制矩阵图
    axs[row, col].matshow(matrix, cmap='Blues')

    # 添加标题
    axs[row, col].set_title(f'Epoch {i+1}')

    # 隐藏坐标轴
    axs[row, col].axis('off')

plt.tight_layout()
plt.savefig("TM.png")

