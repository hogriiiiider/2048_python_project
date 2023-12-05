def get_number():
    rand_num = random.randint(1, 10)
    if rand_num <= 9:
        return "[2]"
    else:
        return "[4]"