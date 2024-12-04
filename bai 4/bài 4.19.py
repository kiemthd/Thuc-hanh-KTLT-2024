print('Hoàng Thanh Kiếm MSSV 235752021610003')
def sieve_of_eratosthenes(limit):
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False  # 0 và 1 không phải là số nguyên tố
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False
    return tuple(i for i in range(limit) if is_prime[i])

# Tạo tuple P chứa các số nguyên tố nhỏ hơn 1 triệu
P = sieve_of_eratosthenes(1_000_000)

# In ra kích thước của tuple và một vài số nguyên tố
print(f"Số lượng số nguyên tố nhỏ hơn 1 triệu: {len(P)}")
print(f"Các số nguyên tố nhỏ hơn 1 triệu (100 số đầu tiên): {P[:100]}")
