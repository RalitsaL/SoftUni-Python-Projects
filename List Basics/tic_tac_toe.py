l1_str = input().split()
l2_str = input().split()
l3_str = input().split()
l1 = [int(i) for i in l1_str]
l2 = [int(i) for i in l2_str]
l3 = [int(i) for i in l3_str]

if(
    (l1[0] == 1 and l2[0] == 1 and l3[0] == 1)
    or (l1[1] == 1 and l2[1] == 1 and l3[1] == 1)
    or (l1[2] == 1 and l2[2] == 1 and l3[2] == 1)
    or (l1[0] == 1 and l2[1] == 1 and l3[2] == 1)
    or (l1[2] == 1 and l2[1] == 1 and l3[0] == 1)
    or (l1[0] == 1 and l1[1] == 1 and l1[2] == 1)
    or (l2[0] == 1 and l2[1] == 1 and l2[2] == 1)
    or (l3[0] == 1 and l3[1] == 1 and l3[2] == 1)
):
    print("First player won")
elif (
    (l1[0] == 2 and l2[0] == 2 and l3[0] == 2)
    or (l1[1] == 2 and l2[1] == 2 and l3[1] == 2)
    or (l1[2] == 2 and l2[2] == 2 and l3[2] == 2)
    or (l1[0] == 2 and l2[1] == 2 and l3[2] == 2)
    or (l1[2] == 2 and l2[1] == 2 and l3[0] == 2)
    or (l1[0] == 2 and l1[1] == 2 and l1[2] == 2)
    or (l2[0] == 2 and l2[1] == 2 and l2[2] == 2)
    or (l3[0] == 2 and l3[1] == 2 and l3[2] == 2)
):
    print("Second player won")
else:
    print("Draw!")