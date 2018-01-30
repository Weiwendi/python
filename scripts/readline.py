f = open(r'../resource/somefile.txt')
for i in range(3):
    print str(i) + ': ' + f.readline(),
f.close()
