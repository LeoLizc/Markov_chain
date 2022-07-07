import random
import graficar

#genera un modelo de markov en base a una cadena de texto s y a un K especificado por parámetros. El k por defecto es 0
def gen_mmarkov(s,k=0):
  
  if len(s) < k:
    return None
  m_markov={}

  for i in range(k,len(s)):
    sbt=s[i-k:i]
    if not sbt in m_markov:
      m_markov[sbt]=[{},0]
    dic=m_markov[sbt][0]
    m_markov[sbt][1]+=1

    if not s[i] in dic:
      dic[s[i]]=0
    dic[s[i]]+=1
  
  return m_markov, s[:k], k

#{key: [{ c: nc, ...}, nk], ...}

#genera, en base a un modelo de markov, una cadena de longitud n que inicie según el parámetro 'ini' especificado o, en su defecto, inicie por la primera llave del modelo
def cad_markov(n, m:dict, ini=None , k=0):
  if n<k:
    return None

  if ini==None:
    ini=m.keys()[0]
  
  if k!= len(ini):
    return None

  s=ini[:]
  frec={ini:1}
  for i in range(n-k):
    key=s[len(s)-k:len(s)]
    frec[key]=frec.get(key,0)+1
    s=s+gen_c(*m[key])
  return s , frec
    
#Genera un caracter basándose diccionario con la frecuencia de cada caracter y un n de apariciones totales
def gen_c(pr:dict, n):
  r=random.random()
  acum=0
  for k in pr:
    acum+=pr[k]
    if r <= acum/n:
      return k

#recibe dos archivos (uno de entrada y uno de salida), un n y un k
def markov(entrada, salida, n, k):

  inp = open(entrada,'r',)
  m_m = gen_mmarkov(inp.read(), k)
  inp.close()

  inp = open(salida, 'w')

  s, fr = cad_markov(n, *m_m)
  inp.write(s)

  inp.close()

  graficar.gen_graphic(list(fr.keys()), list(fr.values()), True)

# print('abcdefg'[5:7])


# pruebapr.pr([{'r': 2, 'v': 1, 'b':4, 'a': 3},10])

# print(cad_markov(100, *gen_mmarkov(s,2) ) )
# print(gen_mmarkov(s,2))

if __name__ == '__main__':
  i = input('''introduce an input file (default: frankenstein.txt) ''')

  if not i:
    i = 'frankenstein.txt'

  o = input('''introduce an output file (default: output.txt) ''')

  if not o:
    o = 'output.txt'
  
  markov(i, o, 800, 2)