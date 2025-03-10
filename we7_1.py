fh = open('mbox-short3.txt')

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())