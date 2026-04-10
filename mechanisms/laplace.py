import numpy as np

def laplace_mechanism(true_value, sensitivity, epsilon):
    """
    拉普拉斯机制：对真实值加噪声，实现差分隐私
    
    参数:
        true_value:  真实的查询结果（比如某列的均值）
        sensitivity: 查询的敏感度
        epsilon:     隐私预算，越小隐私保护越强
    
    返回:
        加了噪声之后的值
    """
    scale = sensitivity / epsilon
    noise = np.random.laplace(0, scale)
    return true_value + noise