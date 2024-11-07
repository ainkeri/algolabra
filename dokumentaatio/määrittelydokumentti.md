# Määrittelydokumentti

## Kirjoitusvirheiden korjaaja

- Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti (TKT)
- Projektin dokumentaation kieli: suomi

Ohjelma on toteutettu Pythonilla. Pystyn vertaisarvioimaan ohjelmia, jotka on tehty Pythonilla tai JavaScriptilla.

### Ohjelman idea

Käyttäjä pystyy tekemään kahta asiaa: hakemaan sanoja ja lisäämään sanoja. Käyttäjä antaa ohjelmalle syötteenä jonkin väärinkirjoitetun sanan, jolle ehdotetaan oikeinkirjoitusta. Ohjelma vertaa käyttäjän väärinkirjoitetun merkkijonon etäisyyttä oikein kirjoitettuihin sanoihin. Tämän perusteella ohjelma osaa antaa lähimmän merkkijonoa muistuttavan sanan. Ensimmäinen versio ohjelmasta osaisi korjata yksittäisiä sanoja, mutta mahdollisesti jatkossa se osaisi korjata lauseita. Käyttäjä voi myös lisätä uusia sanoja ohjelmaan.

Oikein kirjoitetut sanat on ohjelmassa talletettu trie-tietorakenteeseen. Trie-tietorakenteesta merkkijonon tallettaminen ja hakeminen vie O(n) aikaa, missä n on merkkijonon pituus. Käyttäjän merkkijono-syötteen etäisyyttä tutkitaan Damerau-Levenshtein -etäisyyden avulla. Tähän menee pahimmassa tapauksessa O(mn) aikaa, missä m ja n ovat verrattavien merkkijonojen pituudet.

Harjoitustyön ytimenä on mainitsemani trie-tietorakenne ja Damerau-Levenshtein etäisyysalgoritmi.

### Sanasto

Käytän ohjelmassani nykysuomen sanalistaa, joka sisältää yli 100 000 suomen kielen sanaa. Sanalistan olen ladannut Kotus.fi -sivustolta, [tästä linkistä ](https://kaino.kotus.fi/lataa/nykysuomensanalista2024.csv)(lataa sanalistan). Sanalista ei ole tyhjentävä tai normatiivinen luettelo suomen kielen sanoista. Sen on tarkoitus muun muassa toimia apuvälineenä suomen kieltä käsittelevien tietokoneohjelmien ja suomenkielisten käyttöliittymien kehitystyössä.

### Viitteet:

- [Scaler | Trie Data Structure](https://www.scaler.in/trie-data-structure/)

- [Wikipedia | Damerau-Levenshtein distance](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)

- [Kotus | Nykysuomen sanalista 2024](https://www.kotus.fi/aineistot/sana-aineistot/nykysuomen_sanalista)
