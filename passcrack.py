print('making password list')
global passw
passw = ''
time = 0
import string
w = string.printable
for a in range (100):
    for b in range (100):
        for c in range (100):
            for d in range (100):
                for e in range (100):
                    for f in range (100):
                        for g in range (100):
                            for h in range (100):
                                for i in range (100):
                                    for j in range (100):
                                        time += 1
                                        persent = (time * 100) // (100 ** 10)
                                        for persent10 in range(10):
                                            if (persent10*10) == persent:
                                                print (str(persent) + "%")
                                            else:
                                                pass 
                                        passw = "{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}".format(w[a],w[b],w[c],w[d],w[e],w[f],w[g],w[h],w[i],w[j])+'\n'
                                        aa = open ("passlist.txt","r").read()+passw
                                        open ("passlist.txt","w").write(aa)
print('task complited')