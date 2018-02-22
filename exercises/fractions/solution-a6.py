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
  t = randint(1,9)
  n = randint(1,9)
  d = randint(2,9)
  return(t*d,n*d)

def strFraction(a,b):
  return str(a) + "/" + str(b)

def game():
  (a,b) = inventFraction()
  print("Förenkla " + strFraction(a,b))
  pa = int(input("Vad blir täljaren?"))
  pb = int(input("Vad blir nämnaren?"))
  (ca,cb) = simplify(a,b) # Correct answer
  if (pa==ca) & (pb==cb):
    print("Bra gjort! Ditt svar var rätt: " + strFraction(ca, cb))
  else:
    print("Tyvärr, rätt svar är " + strFraction(ca,cb))


game()
