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


def invent_fraction():
  from random import randint
  t = randint(1,4)
  n = randint(1,5)
  return(t,n)

def str_fraction(a,b):
  return str(a) + "/" + str(b)

def sum_fractions(a, b, c, d):
  t = a*d + b*c
  n = b*d
  return simplify(t,n)

def game():
  (a,b) = invent_fraction()
  (c,d) = invent_fraction()
  s1 = str_fraction(a,b)
  s2 = str_fraction(c,d)
  print("Addera och förenkla: " + s1 + " + " + s2)
  pa = int(input("Vad blir täljaren?"))
  pb = int(input("Vad blir nämnaren?"))
  (ca,cb) = sum_fractions(a,b,c,d) # Correct answer
  if (pa==ca) & (pb==cb):
    print("Bra gjort! Ditt svar var rätt: " + str_fraction(ca,cb))
  else:
    print("Tyvärr, rätt svar är " + str_fraction(ca,cb))


game()
