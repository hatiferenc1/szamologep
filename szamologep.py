import streamlit as st

def osszeadas(szam1, szam2):
  return szam1 + szam2

def kivonas(szam1, szam2):
  return szam1 - szam2

def szorzas(szam1, szam2):
  return szam1 * szam2

def osztas(szam1, szam2):
  if szam2 != 0:
    return szam1 / szam2
  else:
    return "Nullával nem osztható"

def szazalek(szam, szazalek_ertek):
  return szam * (szazalek_ertek / 100)

def main():
  st.title("Számológép")

  szam1 = st.number_input("Első szám:")

  szam2 = st.number_input("Második szám:")

  muvelet = st.selectbox("Válassz műveletet:",("összeadás","kivonás","szorzás","osztás","százalékszámítás"))

  

  result = 0
  if muvelet == "összeadás":
    result = osszeadas(szam1, szam2)
  elif muvelet == "kivonás":
    result = kivonas(szam1, szam2)
  elif muvelet == "szorzás":
    result = szorzas(szam1, szam2)
  elif muvelet == "osztás":
    result = osztas(szam1, szam2)
  elif muvelet == "százalékszámítás":
    result = szazalek(szam1, szam2)

  st.write(f"Eredmény: {result}")

if __name__ == '__main__':
  main()
