from mechanisms.laplace import laplace_mechanism
from mechanisms.gaussian import gaussian_mechanism

true_value = 100
sensitivity = 1

print("epsilon越小，隐私保护越强，但误差越大：\n")

for epsilon in [0.1, 0.5, 1.0, 2.0]:
    noisy1 = laplace_mechanism(true_value, sensitivity, epsilon)
    noisy2 = gaussian_mechanism(true_value, sensitivity, epsilon, delta=1e-5)
    error1 = abs(noisy1 - true_value)
    error2 = abs(noisy2 - true_value)
    print(f"epsilon={epsilon:.1f} -> 拉普拉斯: {noisy1:.2f}, 误差: {error1:.2f}")
    print(f"epsilon={epsilon:.1f} -> 高斯:     {noisy2:.2f}, 误差: {error2:.2f}")
    print()