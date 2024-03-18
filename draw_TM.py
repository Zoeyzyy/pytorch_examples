import numpy as np
import matplotlib.pyplot as plt

# 生成 10 个随机数作为示例数据
A = [17885248668.0, 17728938752.0, 17731924804.0, 17799677044.0, 18020323952.0, 17763492588.0, 17753020972.0, 17794780104.0, 17673097372.0, 17793549408.0]
B = [20622909604.0, 19965478524.0, 20321503112.0, 20439136056.0, 20514035256.0, 20149039900.0, 20274085868.0, 20273614768.0, 20231338692.0, 20258262810.0]

# 创建一个包含 10 个子图的图像
fig, axs = plt.subplots(2, 5, figsize=(15, 6))

# 遍历 A 和 B 列表中的值，绘制矩阵图
for i, (a, b) in enumerate(zip(A, B)):
    row = i // 5
    col = i % 5

    # 创建一个 2x2 的矩阵，对角线元素为0，其他元素根据A[i]和B[i]确定
    matrix = np.array([[0, a], [b, 0]])

    # 绘制矩阵图
    im = axs[row, col].matshow(matrix, cmap='Blues')

    # 添加标题
    axs[row, col].set_title(f'Epoch {i+1}')

    # 添加坐标轴标签
    axs[row, col].set_xticks([0, 1])
    axs[row, col].set_xticklabels(['106', '112'])
    axs[row, col].set_yticks([0, 1])
    axs[row, col].set_yticklabels(['106', '112'])

    # 显示坐标轴
    axs[row, col].xaxis.set_ticks_position('bottom')
    axs[row, col].yaxis.set_ticks_position('left')

# 添加整体标题
plt.suptitle('Traffic Matrix for Each Epoch(x for sender, y for reciever)', fontsize=16)

plt.tight_layout()
plt.savefig("TM.png")
