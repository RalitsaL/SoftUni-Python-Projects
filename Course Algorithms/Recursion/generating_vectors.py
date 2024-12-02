def gen_vectors(idx, vector):
    if idx >= len(vector):
        print(*vector, sep="")
        return
    for num in range(2):
        vector[idx] = num
        gen_vectors(idx+1, vector)

n = int(input())
vector = [0]*n
gen_vectors(0, vector)