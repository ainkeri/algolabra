# Testausdokumentti

Kaikki testit testaavat pelkästään ohjelman sovelluslogiikkaa. Luokat, joita testaan ovat: `TrieNode`, `Trie`, `DamerauLevenshtein` ja `StringService`.

## Testikattavuusraportti

<img width="762" alt="Screenshot 2024-11-30 at 11 47 58" src="https://github.com/user-attachments/assets/55d4bd5e-ff07-4a1d-beec-466324ca15fc">

## Yksikkötestit

Yksikkötesteillä testaan sanojen lisäämistä ja hakemista, sekä sanojen vertaamista toisiinsa. `TrieNode` luokkaa testataan vain testausluokalla `TestTrieNode`, joka tarkistaa alkusolmujen lisäämisen.

### Sanojen lisääminen

<b>Testausluokka `TestStringService`:</b>
<i>Testausta varten alustettu kaikki sanat words.txt -tiedostosta trie-tietorakenteeseen.</i>

1. `test_valid_string_can_be_added_to_trie`

   - Testaa, että uusi (ei-tyhjä) sana pystytään lisäämään tietorakenteeseen.

2. `test_not_valid_string_can_not_be_added_to_trie`

   - Testaa, että uutta sanaa (tyhjä) ei voida lisätä tietorakenteeseen.

### Sanojen hakeminen

<b>Testausluokka `TestTrie`:</b>

1. `test_str_is_returned_correctly_with_pre_order_traversal`

   - Testaa, onko sanat lisätty trie-tietorakenteeseen oikealla tavalla käyttäen leveyshakua. String-metodin pitäisi palauttaa sanojen kirjaimet leveyshaun mukaisessa järjestyksessä (pre-order).

2. `test_search_word`

   - Testaa, palauttaako ohjelma oikean boolean -arvon, kun haetaan sanoja. Esim. sana "koira" palauttaa True, mutta "nothere" palauttaa False.

<b>Testausluokka `TestStringService`:</b>

1. `test_word_in_trie_is_found`

   - Testaa, löytyykö annettu sana tietorakenteesta. Sana "koira" palauttaa True.

2. `test_word_not_in_trie_is_not_found`

   - Testaa, antaako ohjelma arvon False, kun etsitty sana ei ole tietorakenteessa.

### Sanojen vertaaminen

<b>Testausluokka `TestStringService`:</b>

1. `test_word_is_corrected`

   - Testaa, antaako ohjelma väärinkirjoitetulle sanalle korjausehdotuksen.

2. `test_sentence_is_corrected`

   - Testaa, antaako ohjelma lauseelle korjausehdotuksen, kun se sisältää väärinkirjoitettuja sanoja.

3. `test_word_too_complex_is_not_corrected`

   - Testaa, palauttaako ohjelma tyhjän listan kun ohjelma saa sanan, joka on liian monimutkainen.

<b>Testausluokka `TestDamerauLevenshtein`:</b>

1. `test_words_compared_have_distance_one`

   - Testaa, antaako ohjelma kahdelle sanalle oikean etäisyyden (1).

2. `test_words_compared_have_distance_two`

   - Testaa, antaako ohjelma kahdelle sanalle oikean etäisyyden (2).

3. `test_words_compared_have_distance_three`

   - Testaa, antaako ohjelma kahdelle sanalle oikean etäisyyden (3).

4. `test_words_compared_have_greater_edit_distance`

   - Testaa, antaako ohjelma suuremman etäisyyden (15).

5. `test_compared_word_is_empty_string`

   - Testaa, antaako ohjelma käyttäjän antaman sanan pituuden, kun verrattava sana on tyhjä merkkijono.

6. `test_user_input_is_empty_string`

   - Testaa, antaako ohjelma verrattavan sanan pituuden, kun käyttäjän annettu sana on tyhjä merkkijono.

7. `test_two_empty_words_have_correct_distance`

   - Testaa, antaako arvon 0 kun verrataan kahta tyhjää merkkijonoa.

8. `test_transposition_gives_correct_distance`

   - Testaa, toimiiko transpositio, eli esim. rapsi - raspi lyhin etäisyys on 1.

9. `test_typo_edit_distance_with_adjacent_keys`

   - Testaa, kuinka hyvin ohjelma tunnistaa kirjoitusvirheen, joka johtuu naapurinäppäimen painamisesta. Esim. joira - koira, missä j on k kirjaimen vieressä näppäimistöllä.

## Invarianttitestit

Invarianttitesteillä testataan suuremmilla sanamäärillä sanojen lisäämistä, hakemista ja vertaamista keskenään.

<b>Testausluokka `TestTrie`:</b>

1. `test_adding_to_trie_hypothesis(arvo)`

   - Testaa, onnistuuko uuden sanan lisääminen. Annetaan maksimissaan 500 eri sanaa, joiden pituus on 1 - 500 merkin välillä. Testataan, onnistuuko sanojen lisääminen trie-tietorakenteeseen (eli löytyykö sanat lisäyksen jälkeen).

<b>Testausluokka `TestDamerauLevenshtein`:</b>

1. `test_right_distance_hypothesis`

   - Testaa, antaako etäisyysalgoritmi etäisyyden 0 tai suurempi, kun verrataan maksimissaan 1000 kappaletta 1 - 500 merkin pituisia sanoja listaan sanoja.

2. `test_right_distance_with_same_word_hypothesis`

   - Testaa, antaako etäisyysalgoritmi etäisyyden 0, kun verrataan sanaa itseensä, jossa merkkejä 1 - 100 merkin väliltä. Testin pitää siis palauttaa arvo 0.

3. `test_distance_to_empty_word_is_correct_hypothesis`

   - Testaa, antaako etäisyysalgoritmi toisen sanan pituuden etäisyydeksi, kun verrataan sanaa tyhjään merkkijonoon. Testimerkkijonoja on 1000, jossa merkkejä 1 - 500 merkin väliltä.
