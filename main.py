
# naloga1

odgovor = {
    " temperatura ": 24 ,
    " vlaznost ": 60 ,
    " veter ": 8 ,
    " lokacija ": " Ljubljana "
}
print(odgovor[" temperatura "])
print(odgovor[" vlaznost "])
print(f"V mestu{odgovor[' lokacija ']}je {odgovor[" temperatura "]} stopinj")



# naloga2

student = {
    "ime": " Marko ",
    " priimek ": " Horvat ",
    " naslov ": {
        " ulica ": " Slovenska cesta 12",
        " mesto ": " Maribor ",
        " posta ": 2000
    }
}
print(student[" naslov "][" ulica "])
print(student[" priimek "])
print(f"{student["ime"]}{student[" priimek "]},{student[" naslov "][" ulica "]}")

# naloga3

razred = {
    " oznaka ": "4.a",
    " dijaki ": ["Ana", " Bojan ", " Cvetka ", " David "] ,
    " ocene ": [5 , 4 , 5 , 3]
}
print(razred[" dijaki "][0])
print(razred[" ocene "][2])
for i in razred[" dijaki "]:
    print(i)

# naloga4

knjige = {
    " knjiznica ": " Mestna knjiznica ",
    " seznam ": [
    {" naslov ": " Python programiranje ", " cena ": 29.99} ,
    {" naslov ": " Uvod v algoritme ", " cena ": 35.50} ,
    {" naslov ": " Spletne aplikacije ", " cena ": 42.00}
    ]
}

print(knjige[" seznam "][0][" naslov "])
print(knjige[" seznam "][1][" cena "])
for i in knjige[" seznam "]:
    print(f"{i[' naslov ']}: {i[' cena ']} EUR")

# naloga5

narocilo = {
    "id": "ORD -2024 -001 ",
    " kupec ": {
        "ime": " Petra Novak ",
        " email ": " petra@email .si"
    } ,
    " artikli ": [
        {" naziv ": " Miska ", " kolicina ": 2 , " cena ": 15.99} ,
        {" naziv ": " Tipkovnica ", " kolicina ": 1 , " cena ": 45.00}
    ] ,
    " status ": " potrjeno "
}
print(narocilo["id"])
print(narocilo[" kupec "][" email "])
print(narocilo[" artikli "][0][" naziv "])
for i in narocilo[" artikli "]:
    print(f"{i[' naziv ']}: {i[' kolicina ']} kos/i")

    