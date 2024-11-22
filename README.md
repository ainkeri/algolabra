# Kirjoitusvirheiden korjaaja

Algoritmit ja Tekoäly Harjoitustyö 2024.

## Dokumentaatio

- [Määrittelydokumentti](https://github.com/ainkeri/algolabra/blob/main/dokumentaatio/m%C3%A4%C3%A4rittelydokumentti.md)
- [Testausdokumentti](https://github.com/ainkeri/algolabra/blob/main/dokumentaatio/testausdokumentti.md)
- [Toteutusdokumentti](https://github.com/ainkeri/algolabra/blob/main/dokumentaatio/toteutusdokumentti.md)

## Viikkoraportit

- [Viikko 1](https://github.com/ainkeri/algolabra/tree/main/dokumentaatio/viikkoraportit/viikkoraportti1.md)
- [Viikko 2](https://github.com/ainkeri/algolabra/tree/main/dokumentaatio/viikkoraportit/viikkoraportti2.md)
- [Viikko 3](https://github.com/ainkeri/algolabra/tree/main/dokumentaatio/viikkoraportit/viikkoraportti3.md)
- [Viikko 4](https://github.com/ainkeri/algolabra/tree/main/dokumentaatio/viikkoraportit/viikkoraportti4.md)

## Komentorivikomennot

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
