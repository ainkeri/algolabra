# Viikkoraportti 3

Ohjelma on edennyt tällä viikolla hyvin. Opin Damerau-Levenshtein-etäisyydestä, jota oikeastaan suurimman osan ajasta tutkin.

Lisäsin Damerau-Levenshtein -etäisyyden ohjelmaan, toimii halutusti käyttöliittymässä. Jos sanaa ei löydy trie-tietorakenteesta, ohjelma ehdottaa lähintä muistuttavaa sanaa. Loin myös testejä luokalle. Testausraportti aloitettu, kirjattu kaikki tällä hetkellä olevat testit. Tein yksikkötestien lisäksi invarianttitestejä, jotta voi tarkistaa ohjelman toimivan isommilla syötteillä.

Vaikeuksia tuottanut eniten testaaminen, koska (ajaessani poetry run invoke test) aina uusien testien tekeminen laskee toisten luokkien testauskattavuutta. Luulen, että testini ovat ihan hyvillä malleilla, mutta tähän kaipaisin ehkä vinkkiä taas.

Ensi viikolla ajattelin pureutua taas testaamiseen kehittämiseen, mutta myös toiminnallisuuteen, jossa pitempien sanojen hakemiseen ohjelmasta onnistuisi. Tällöin ohjelmalla voisi korjata lauseista mahdollisia kirjoitusvirheitä.

Kysymyksiä ohjaajalle: millaisia muita testejä voisitte ehdottaa? Olisiko esim. suorituskykytestaukset sellaisia testejä, mitä minun kannattaisi lisätä?

Käytetty tuntimäärä: 17 h
