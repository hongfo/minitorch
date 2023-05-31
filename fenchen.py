def change(a):
    ls = []
    for i in range(len(a)):
        ls.append(a.index(i))
    return ls


import torch

# 原始张量形状为 (3, 4, 5)
x = torch.randn(3, 4, 5, 6)

# 使用 (1, 2, 0) permute 变换得到新张量 y
y = x.permute(3, 1, 2, 0)

# 记录变换前后的顺序为 (1, 2, 0)
order = [3, 1, 2, 0]

# 将 y 张量变回原来的形状
order = change(order)
print(order)
z = y.permute(*order)

print(x.shape)  # torch.Size([3, 4, 5])
print(y.shape)  # torch.Size([4, 5, 3])
print(z.shape)  # torch.Size([3, 4, 5])
