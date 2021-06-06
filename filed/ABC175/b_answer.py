*l,=map(int,[*open(0)][1].split())
print(sum(i<j<k<i+j for i in l for j in l for k in l))