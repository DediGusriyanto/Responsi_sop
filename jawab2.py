print("----------inputan---------")
r1 = int(input("program : "))
t2 = int(input("program  : "))
r3 = int(input("program :"))
t4 = int(input("program  : "))
r5 = int(input("program :"))
t6 = int(input("program : "))
Quantum_time = int(input("masukan quantum time: ")) 

jawab = r1+t2+r3+t4+r5+t6/Quantum_time
jawab2 = t4+r1+r3+r5+t6+r1/Quantum_time
print("========hasil=======")
print("Average turnaround time: ", jawab)
print("Average waiting time: ", jawab2)