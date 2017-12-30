import random

a = list()
for i in range(20):
    a.append(random.randint(0, 100))


def get_en(p_t):
    ans = list(filter(lambda x: x>p_t, a))
    if len(ans) > 3:
        return ans[:3]
    else:
        return ans


print(get_en(90))
