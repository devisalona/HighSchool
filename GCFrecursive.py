
def main():
	c = 1
	a = input("enter first number ")
	b = input("enter second number ")
	print GCF(a,b,c)
    
def GCF(a,b,c):
	if c == 0:
		return a
	else:
        	c = a - (int)(a/b)*b
        	a = b
        	b = c
        return GCF(a,b,c)

main();
