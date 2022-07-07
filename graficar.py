import matplotlib
import matplotlib.pyplot as plt
import numpy

# t , v = ['ab','ac','bc','bb','cb'], [10,12,13,20,6]

def gen_graphic( t, v, save=False ):
  fig, ax = plt.subplots()

  ax.set_title('Diagrama de Frecuencias')
  plt.bar(t,v)
  if save: plt.savefig('diagrama.png')
  #Finalmente mostramos la grafica con el metodo show()
  plt.show()