# Käyttöohje

Kloonaa projekti koneellesi.

### Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportti luodaan komennolla:

```bash
poetry run invoke coverage-report
```

### Pylint

Pylintin tarkistukset voidaan suorittaa komennolla:

```bash
poetry run invoke lint
```

## Ohjelman toiminnallisuus

Käynnistäessä ohjelma avautuu ponnahdusikkunaan, jossa on napit `Etsi sanaa tai lausetta` ja `Lisää uusi sana`. Ohjelmassa voidaan tehdä kahta asiaa: hakemaan ja lisäämään sanoja.

### Sanojen hakeminen

Käyttäjä voi hakea sanoja tai lauseita ohjelmasta. Jos sana/lause löytyy, ohjelma ilmoittaa: `Sana/lause löytyi!`. Jos sanaa ei löydy, antaa ohjelma korjausehdotuksen: `Tarkoititko "<korjattu sana>"?`. Lauseen tapauksessa ohjelma antaa korjausehdotuksen: `Tarkoititko "<korjattu lause>"?`.

#### Virhetilanteet

Jos sana on älyttömän pitkä ja täynnä sekaisia merkkejä kuten "adkklqdjjlkedjflkesjdkledsafghjkfrd", ohjelma tulostaa `Sanaa/lausetta ei löytynyt` (yksi merkki vähemmän ja ohjelma olisi antanut korjauksen).

### Sanojen lisääminen

Käyttäjä voi lisätä uusia sanoja ohjelmaan, jos niitä ei vielä löydy ohjelmasta. Jos sanan lisääminen onnistui, ohjelma tulostaa viestin: `Uusi sana "<sana>" lisätty!`. Jos sanan lisääminen epäonnistui (eli sana on jo ohjelmassa) ohjelma tulostaa: `Sana "<sana>" on jo lisätty.`.
