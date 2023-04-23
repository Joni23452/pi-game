# pi-game
Sovelluksella voi harjoitella piin desimaaleja. Pelissä syötetään piin desimaaleja yksi kerrallaan, jos syötetty luku ei ole oikea, peli päättyy. Pelin päätyttyä voi luoda itselleen vihjeen joka näkyy tulevissa peleissä kyseisen desimaalin kohdalla. Sovelluksessa voi luoda käyttäjän ja kirjautua sisään sekä ulos. Vihjeiden käyttö edellyttää sisään kirjautumista. Sovelluksessa pääsee myös katsomaan piitä.

Tulevia ominaisuuksia:
 - Vihjeet ovat piilossa, ne saa näkyviin vain halutessaan. Pelin aikana katsottujen vihjeiden määrästä pidetään kirjaa. 
 - Suoritukset tallennetaan: käyttäjä, kuinka pitkälle pääsi, montako vihjettä käytettiin, aikaleima
 - Leaderboard, kaikista käyttäjistä parhaat suoritukset löytyvät täältä. Käyttäjä voi halutessaan poistaa itsensä leaderboardilta.
 - Käyttäjät voivat lisätä toisia käyttäjiä kavereikseen ja nähdä toistensa parhaat suoritukset
 - Käyttäjät voivat luoda ryhmiä, ryhmien jäsenet näkevät ryhmän parhaat tulokset
 - Käyttäjä voi nähdä erilaisia tilastoja omista suorituksistaan
 - Ylläpitäjä voi tarkastella käyttäjien suorituksia ja poistaa epäilyttäviä tuloksia leaderboardilta

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
