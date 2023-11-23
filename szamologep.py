import streamlit as st 

def osszead(elso , masodik):
  return elso + masodik 
def kivon(elso , masodik):
  return elso-masodik

def szorzas(elso , masodik):
  return elso * masodik 
def osztas(elso , masodik):
  if masodik != 0:
    return elso / masodik
  else:
    return "Nullával nem lehet osztani hülyegyerek"


def szazalek(szam , szazalek_erteke):
  return szam * (szazalek_erteke / 100)

def main():
  st.title("Számológép")

elso = st.number_input("Add meg a második számot:")

muvelet = st.selectbox("Válasszd ki a műveletet ",("összeadás","kivunás","osztás","szorzás","százalékszámítás"))

masodik = st.number_input("Add meg a második számot:")

eredmeny = 0
if muvelet == "összeadás":
  result = osszeadas(elso,masodik) 
elif muvelet == "kivonás":
  result = kivonas(elso,masodik)
elif muvelet == "szorzás":
  result = szorzas(elso,masodik)
elif muvelet == "osztás":
  result = osztas(elso,masodik)
  elif muvelet == "százalékszámítás":
  result = szazalekszamitas(elso,masodik)

st.write(f"Eredmény:{eredmeny}")

if __name__ == '__main__':
  main()
  
