def gcd(a, b):  # Räkna ut gcd för a och b
  while a != b: # Så länge talen inte är lika:
    if a > b:     # Om a är större än b
      a = a - b   # Ändra på a genom att subtrahera b
    else:         # Annars (dvs b är större än a)
      b = b - a   # Ändra på b genom att subtrahera a
                # Nu är while-loopen färdig
                # dvs a och b är lika
  return a      # Returnera gcd, dvs nuvarande värdet på a

def simplify(t,n):
  d = gcd(t,n)
  return (t//d, n//d)


def inventFraction():
  from random import randint
  t = randint(1,4)
  n = randint(1,5)
  return(t,n)

def strFraction(a,b):
  return str(a) + "/" + str(b)

def sumFractions(a, b, c, d):
  t = a*d + b*c
  n = b*d
  return simplify(t,n)

def game():
  (a,b) = inventFraction()
  (c,d) = inventFraction()
  s1 = strFraction(a,b)
  s2 = strFraction(c,d)
  print("Addera och förenkla: " + s1 + " + " + s2)
  pa = int(input("Vad blir täljaren?"))
  pb = int(input("Vad blir nämnaren?"))
  (ca,cb) = sumFractions(a,b,c,d) # Correct answer
  if (pa==ca) & (pb==cb):
    print("Bra gjort! Ditt svar var rätt: " + strFraction(ca,cb))
  else:
    print("Tyvärr, rätt svar är " + strFraction(ca,cb))


game()
