# Testausdokumentti

Kaikki testit testaavat pelkästään ohjelman sovelluslogiikkaa. Luokat, joita testaan ovat: `TrieNode`, `Trie`, `DamerauLevenshtein` ja `StringService`.

## Testikattavuusraportti

<img width="770" alt="Screenshot 2024-11-14 at 12 30 16" src="https://github.com/user-attachments/assets/3d3c2af6-af9b-40fc-89b4-c9483e234440">

## Yksikkötestit

Yksikkötesteillä testaan sanojen lisäämistä ja hakemista, sekä sanojen vertaamista toisiinsa. `TrieNode` luokkaa testataan vain testausluokalla `TestTrieNode`, joka tarkistaa alkusolmujen lisäämisen.

### Sanojen lisääminen

Testausluokka `TestStringService` (testausta varten alustettu kaikki sanat words.txt -tiedostosta trie-tietorakenteeseen):

1. `test_valid_string_can_be_added_to_trie`

   - Testaa, että uusi (ei-tyhjä) sana pystytään lisäämään tietorakenteeseen.

2. `test_not_valid_string_can_not_be_added_to_trie`

   - Testaa, että uutta sanaa (tyhjä) ei voida lisätä tietorakenteeseen.

### Sanojen hakeminen

Testausluokka `TestTrie`:

1. `test_str_is_returned_correctly_with_pre_order_traversal`

   - Testaa, onko sanat lisätty trie-tietorakenteeseen oikealla tavalla käyttäen leveyshakua. String-metodin pitäisi palauttaa sanojen kirjaimet leveyshaun mukaisessa järjestyksessä (pre-order).

2. `test_search_word`

   - Testaa, palauttaako ohjelma oikean boolean -arvon, kun haetaan sanoja. Esim. sana "normaaliolot" palauttaa True, mutta "nothere" palauttaa False.

Testausluokka `TestStringService`:

1. `test_word_in_trie_is_found`

   - Testaa, löytyykö annettu sana tietorakenteesta. Sana "koira" palauttaa True.

### Sanojen vertaaminen

Testausluokka `TestStringService`:

1. `test_word_not_in_trie_gets_suggestion`

   - Testaa, antaako ohjelma väärinkirjoitetulle sanalle korjausehdotuksen. Tässä tapauksessa ensimmäinen sana, jonka etäisyys annettuun sanaan on 1: (sirsi - hirsi).

2. `test_sentence_gets_a_suggestion`

   - Testaa, antaako ohjelma lauseelle korjausehdotuksen, kun se sisältää väärinkirjoitettuja sanoja.

3. `test_correct_sentence_is_found`

   - Testaa, palauttaako ohjelma True kun ohjelma saa lauseen, joka on kirjoitettu oikein.

4. `test_word_too_complex_gets_no_suggestion`

   - Testaa, tulostaako ohjelma "Sanaa ei löytynyt" käyttäjän etsiessä liian kompleksista sanaa (ohjelma ei siis anna korjausehdotusta).

Testausluokka `TestDamerauLevenshtein`:

1. `test_words_compared_have_distance_one`

   - Testaa, antaako ohjelma kahdelle sanalle oikean etäisyyden (1).

2. `test_words_compared_have_distance_two`

   - Testaa, antaako ohjelma kahdelle sanalle oikean etäisyyden (2).

3. `test_words_compared_have_distance_three`

   - Testaa, antaako ohjelma kahdelle sanalle oikean etäisyyden (3).

4. `test_words_compared_have_greater_edit_distance`

   - Testaa, antaako ohjelma suuremman etäisyyden (15).

5. `test_one_empty_word_has_right_distance`

   - Testaa, antaako ohjelma toisen sanan pituuden, kun verrattava sana on tyhjä merkkijono.

6. `test_two_empty_words_has_right_distance`

   - Testaa, antaako arvon 0 kun verrataan kahta tyhjää merkkijonoa.

7. `test_transposition_gives_correct_distance`

   - Testaa, toimiiko transpositio, eli esim. rapsi - raspi lyhin etäisyys on 1.

## Invarianttitestit

Invarianttitesteillä testataan suuremmilla sanamäärillä sanojen lisäämistä, hakemista ja vertaamista keskenään.

Testausluokka `TestTrie`:

1. `test_adding_to_trie_hypothesis(arvo)`

   - Testaa, onnistuuko uuden sanan lisääminen. Annetaan maksimissaan 500 eri sanaa, joiden pituus on 1 - 500 merkin välillä. Testataan, onnistuuko sanojen lisääminen trie-tietorakenteeseen (eli löytyykö sanat lisäyksen jälkeen).

Testausluokka `TestDamerauLevenshtein`:

1. `test_right_distance_hypothesis`

   - Testaa, antaako etäisyysalgoritmi pituuden 0 tai suurempi, kun verrataan maksimissaan 1000 kappaletta 1 - 500 merkin pituisia sanoja listaan sanoja.

1. `test_right_distance_between_two_hypothesis`

   - Testaa, antaako etäisyysalgoritmi saman etäisyyden, kun verrataan kahta sanaa, joissa on molemmissa väliltä 1 - 500 merkkiä. Testissä annetaan arvot kahdesti, eli ensin verrataan arvoa 1 arvoon 2 ja sitten arvoa 2 arvoon 1.

1. `test_right_distance_with_same_word_hypothesis`

   - Testaa, antaako etäisyysalgoritmi pituuden 0, kun verrataan sanaa itseensä, jossa merkkejä 1 - 100 kappaleen väliltä. Testin pitää siis palauttaa arvo 0.
