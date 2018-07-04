
def load_doc(filename):
	file = open(filename, 'r')
	text = file.read()
	file.close()
	return text

 

def extract_words(doc):
	mapping = list()
	for line in doc.split('\n'):
		tokens = line.split(' ')
		mapping.append(tokens[0])
	return mapping


def extract_dic(doc):
	mapping = list()
	for line in doc.split('\n'):
		mapping.append(line)
	return mapping


def get_words(w):
        l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


        d=dict()
        d2=dict()

        for i in l:
                d[i]=extract_words(load_doc('Words/'+str(i)+'word.csv'))
                d2[i]=extract_dic(load_doc('Dictionary in csv/'+str(i)+'.csv'))
                

        

                
        m=[]
        y=[]
        f=w.lower()
        F=''.join(sorted(f))
         
        for i in f:
                r=i.upper()
                for o in range(len(d[r])):
                        j=d[r][o]
                        J=''.join(sorted(j))
                        if len(J)==len(F):
                                for k in range(len(J)):
                                        if J[k]!=F[k]:
                                                break
                                        if k==len(J)-1:
                                                m.append(j)
                                                y.append(d2[r][o])
                                                print(d2[r][o]+'\n')
                                                
        return m                               
                                
                                        
                        
                






























