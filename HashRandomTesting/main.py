import random

for i in range(10):
    keyList = [33755, 38099]
    keyList.sort()
    keyRaw = " ".join(str(x) for x in keyList)
    numeric_seed = hash(keyRaw)
    random.seed(numeric_seed)
    chosen_port = random.choice(keyList)
    print(chosen_port)