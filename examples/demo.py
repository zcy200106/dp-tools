import sys


from mechanisms.laplace import laplace_mechanism

# 假设真实值是100（比如某数据集的平均年龄）
true_value = 100
sensitivity = 1

print("epsilon越小，隐私保护越强，但误差越大：\n")

for epsilon in [0.1, 0.5, 1.0, 2.0]:
    noisy = laplace_mechanism(true_value, sensitivity, epsilon)
    error = abs(noisy - true_value)
    print(f"epsilon={epsilon:.1f} -> 加噪后的值: {noisy:.2f}, 误差: {error:.2f}")