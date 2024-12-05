# Viikkoraportti 6

Tällä viikolla sain paljon ideoita ja parannusehdotuksia ohjaajalta. Muutin ohjelman rakennetta niin, että sanan etsimiselle ja vertaamiselle on täysin omat metodit. Tällä korjaantui turha etäisyyden laskeminen lisätessä sanaa. Optimoin myös sanojen vertaamista, vanhassa versiossa talletin kaikki sanat triessä listaan, joka oli vähän turhaa. Loin uudet metodit, joiden avulla sanoja etsiessä iteroidaan läpi suoraan trie-tietorakennetta.

Lisäsin myös Damerau-Levenshtein -etäisyyteen ominaisuuden, joka huomioi näppäimistön kirjaimet. Nyt kun käyttäjä esim. etsii pliivi, ohjelma ehdottaa oliivi, koska o ja p ovat toisiaan lähellä näppäimistöllä. Loin tälle oman kovakoodatun sanakirjan DamerauLevenshtein -luokkaan, joka ainakin itselle näyttää hieman hassulta. Jouduin sisällyttämään siihen monia kirjaimia, koska muuten ohjelma olisi kaatunut (jos esim. ei lisätä kirjaimelle "š" omaa avainta). Ohjaaja mainitsi, että tälle korjaukselle voisi antaa painoksi esim. 1/4. Lisäsin tälle oman if-ehdon algoritmiin. Ohjelma tuntuu toimivan ja korjausehdotukset ovat järkevämpiä.

Siirsin käyttöohjeet README:stä erilliseen dokumenttiin ja lisäsin infoa ohjelman käytöstä. Muuttelin testejä.

Sain lisättyä kaiken mitä keskusteltiin ohjaajan kanssa. Vinkkejä voin ottaa vastaan jos esim. näppäimistön kirjainten huomioimisen voisi tehdä paremmin. Tai muita laajennusehdotuksia tarvittaessa. Muuten hyvillä malleilla eikä oikeastaan vaikeuksia. Tuntuu, että ohjelma aika lailla valmiina.

Käytetty tuntimäärä: 9 h
