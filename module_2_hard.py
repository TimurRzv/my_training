def generate_password(n):
    password = []

    for a in range(1, 21):
        for b in range(a + 1, 21):
            sum_pair = a + b
            if n % sum_pair == 0:
                password.append(f"{a}+{b} ")

    return ''.join(password)
n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    print("Нужный пароль:", generate_password(n))
else:
    print("Число должно быть в диапазоне от 3 до 20.")
