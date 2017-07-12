import sys

def tonum(c):
   if c == 'X':
      return 10
   elif c == '-':
      return 0
   return int(c)

def calcscore(s, verbose = False):
   sl = list(s)
   if verbose: print 'sl = ', sl
   iframe = 0
   framel = []

   while iframe < 10:
      c0 = tonum(sl[0])
      if c0 == 10:
#        rolled a strike, add next two rolls
         c1 = tonum(sl[1])
         if sl[2] == '/':
            c2 = 10 - c1
         else:
            c2 = tonum(sl[2])
         framel.append([c0, c1, c2])
         sl = sl[1:]
      elif sl[1] == '/':
#        rolled a spare, add next roll
         c1 = 10 - c0
         c2 = tonum(sl[2])
         framel.append([c0, c1, c2])
         sl = sl[2:]
      else:
#        no spare or strike, score just the rolls
         c1 = tonum(sl[1])
         framel.append([c0, c1])
         sl = sl[2:]
      iframe += 1
   if verbose: print 'framel = ', framel
   score = 0
   for f in framel:
      score += sum(f)
   return score

if __name__ == '__main__':
   if len(sys.argv) > 1:
      ss = sys.argv[1:]
   else:
      ss = ['XXXXXXXXXXXX', '9-9-9-9-9-9-9-9-9-9-', '5/5/5/5/5/5/5/5/5/5/5', 'X7/9-X-88/-6XXX81']
   for s in ss:
      score = calcscore(s)
      print 'score = ', score
