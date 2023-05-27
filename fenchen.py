from minitorch import tensor,Tensor,TensorData,TensorBackend
import minitorch


t = tensor([[2, 3], [4, 6], [5, 7]])
t_summed = t.sum()
print(t_summed)