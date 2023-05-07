# pi-game
Sovelluksessa voi luoda käyttäjän sekä kirjautua sisään ja ulos. Kirjauduttuaan sisään pääsee pelaamaan peliä. 

Pelissä syötetään piin desimaaleja yksi kerrallaan, peli päättyy kun väärä luku syötetään. 

Pelin päätyttyä pääsee lisäämään kohdalle jossa hävisi itselleen vihjeen, tai muokkaamaan vihjettä jos vihje on jo olemassa. Vihjeet saa halutessaan näkyviin pelin aikana kun tulee kohdalle jossa vihje on olemassa.

Sovelluksessa pääsee katsomaan leaderboardeja, joista löytyy ilman vihjeitä pisimmälle päässeet pelaajat, eniten pelejä pelanneet pelaajat, sekä yhteensä eniten lukuja oikein syöttäneet pelaajat.

Sovelluksessa pääsee katsomaan omaa profiiliaan josta löytyy käyttäjän omat tilastot sekä pelihistoria

Sovelluksessa käytetään vain 3 tietokanta taulua, aiemman suunnitelman mukaiset ryhmät eivät toteutuneet.



Sovellus ei ole testattavissa fly.iossa.

##Käynnistysohjeet:
Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. 
Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>

Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt

Määritä vielä tietokannan skeema komennolla
$ psql < schema.sql

Nyt voit käynnistää sovelluksen komennolla

$ flask run
