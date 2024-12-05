# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelman ideana on kirjoitusvirheiden korjaaja, joka käyttää Trie-tietorakennetta sanojen tallentamiseen/hakemiseen ja Damerau-Levenshtein -etäisyyttä kahden sanan etäisyyden laskemiseen.

### Trie-tietorakenne

Trie on puumainen tietorakenne, joka sisältää merkkijonoja. Se toimii tehokkaasti sanojen lisäämisessä ja hakemisessa. Trie:ssä on juurisolmu, joka edustaa tyhjää merkkijonoa. Jokainen solmu edustaa yhtä merkkiä, ja solmusta voi lähteä kaari toiseen solmuun. Kaari juurisolmusta johonkin solmuun edustaa jonkin sanan etuliitettä. Solmulla voi olla arvo `finish = True`, joka tarkoittaa, että kyseiseen solmuun loppuu joku sana.

#### Aikavaativuus

Sanan lisääminen trie-tietorakenteeseen vie O(n) aikaa, missä n on lisättävän merkkijonon pituus. Sanan hakeminen vie myös O(n) aikaa, missä n on haettavan merkkijonon pituus.

### Damerau-Levenshtein -etäisyys

Etäisyysalgoritmi, joka mittaa kahden sanan samankaltaisuutta. Se ottaa huomioon määrän, kuinka monta kertaa lisätään, poistetaan, korvataan ja transponoidaan merkkijonoa, jotta siitä saataisiin haluttu merkkijono.

Esimerkki: pivi &rarr; pihvi

Algoritmin avulla voidaan laskea, että ylemmän muutoksen etäisyys on 1, sillä pivi &rarr; pihvi vaatii vain yhden merkin lisäyksen. Ohjelmassa on ideana löytää sana, jonka etäisyys syötteeseen on mahdollisimman pieni.

Etäisyysalgoritmiin on lisätty toiminnallisuus, joka huomioi kirjainten sijainnin näppäimistöllä ja niiden lähimmät naapurikirjaimet. Koska kirjoitusvirheet johtuvat usein väärän napin painalluksesta, ohjelma antaa tälläiselle kirjaimen korvaamiselle painon 1/4.

Esimerkki: pliivi &rarr; oliivi

Esimerkissä huomioidaan, että kirjain "o" on lähellä kirjainta "p" näppäimistöllä.

#### Aikavaativuus

Kahden sanan vertaaminen keskenään Damerau-Levenshtein -etäisyydellä vie O(mn) aikaa, missä m ja n ovat verrattavien merkkijonojen pituudet.

## Laajat kielimallit

Olen käyttänyt ChatGPT:tä virheviestien ja käsitteiden selventämiseen. Itse koodin luomiseen en ole käyttänyt mitään laajaa kielimallia. Käytetty malli: GPT-4o mini, eli ilmaisversio.

## Viitteet:

- [Trie | Wikipedia](https://en.wikipedia.org/wiki/Trie)
- [Trie | GeeksForGeeks](https://www.geeksforgeeks.org/trie-insert-and-search/)
- [Damerau Levenshtein | Wikipedia](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
