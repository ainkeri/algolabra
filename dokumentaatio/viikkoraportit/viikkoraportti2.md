# Viikkoraportti 2

Tällä viikolla aloin luomaan itse trie-tietorakennetta, testejä ja käyttöliittymän yhdistämistä sovelluslogiikkaan. Ohjaajan palautteesta lisäsin nyt määrittelydokumenttiin käyttämäni sanaston.

Tein luokille TrieNode, Trie ja StringService myös yksikkötestejä. Coveragen mukaan sain kaikista 100%, mutta en ole varma, olenko testannut tarpeeksi/oikeilla tavoilla (pytest mukaan en).

Aloin myös yhdistämään käyttöliittymää sovelluslogiikkaan. Sanojen etsiminen toimii, ja jos sana löytyy/ei löydy tietorakenteesta käyttöliittymä kertoo joko että "Word found in trie!" tai "Word not found in trie.". Sana, joka on jo triessä ei lisätä triehen. Jos uuden sanan lisää ja sitten hakee, sana löytyy triestä.

Lisäsin myös taskejä ja käyttöohjeen ohjelmalle. Päivittelin UI:ta mielekkäämmäksi.

Opin viikolla paljon trie-tietorakenteesta, johon olinkin koko viikon keskittynyt. Oletin sen olevan vaikeaa yhdistää tietorakenne ohjelmaani, mutta oikeastaan ainoa mitä jäänyt epäselväksi on ohjelman testaaminen.

Seuraavaksi ajattelin jo alkaa implementoimaan Damerau-Levenshteinin -etäisyyttä ohjelmaani. Luulen, että tämän tekemiseen tulee menemään eniten aikaa.

Kysymyksiä ohjaajalle: mikä/mitkä olisivat hyviä tapoja testata trie-tietorakennetta yksikkötestien rinnalla? Olisi kiva saada tähän vähän apua. Ja vielä testeistä sen verran, että olenko ymmärtänyt materiaalin oikein, että minun tarvitsee testata vain alihakemiston services koodia?

Käytetty tuntimäärä: 12h
