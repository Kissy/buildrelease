
examples:

PyPackage
©¦  PyCommonM.py
©¦  __init__.py
©¦
©À©¤p1Package
©¦      P1M.py
©¦      P1MC.py
©¦      __init__.py
©¦
©¸©¤p2
       P2.py
       P2M.py


PyCommonM.py
def PyCommonMF():  print "PyCommonMF"


P2M.py:
def P1MF():   print 'P1MF'

P1MC.py:
class P1MC(): 
  @staticmethod
  def P1MCF():  print 'P1MCF'

P2M.py:
def P2MF(): print 'P2MF'



P2.py:
import P2M
from PyPackage import PyCommonM
from PyPackage.p1Package import P1M
from PyPackage.p1Package.P1MC import P1MC


def P2F(): 
  print 'P2F'
  
  
if __name__ == '__main__':
  P2F()
  P2M.P2MF()
  P1M.P1MF()
  P1MC.P1MCF()
  PyCommonM.PyCommonMF()


result:

P2F
P2MF
P1MF
P1MCF
PyCommonMF