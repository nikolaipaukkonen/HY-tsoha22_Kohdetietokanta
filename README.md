# Kohdetietokanta
Kurssityö HY Tietokantasovellus -kurssille kesä 2022. Toteutus Pythonilla, Flaskilla ja PostgreSQL:llä. 



## Välipalautus 2
Sovelluksen pohja on toiminnassa ja sen toteutus etenee. Tällä hetkellä käyttäjän luonti, sisäänkirjautuminen ja uloskirjautuminen toimivat. Kohteiden lisääminen *Add locations*-valinnalla ei ole vielä toiminnassa, eikä Mapbox-ikkunasta voi vielä valita kohteen sijaintia leveys- ja pituusasteiden tuomiseksi. Myöskään Admin-ominaisuuksia ei ole vielä toteutettu -- tarkoituksena olisi, että admin-käyttäjät voivat poistaa muiden käyttäjien lisäämiä kohteita. Myös kommentointimahdollisuus puuttuu versiosta.

Tietoturvaa (esim. SQL-injektioiden suhteen) ei ole vielä huomioitu laajemmin. Tietokannan osoite, Mapboxin API-avain yms. asiat on piilotettu .env-tiedostoon (muokkaushistoriassa näkyvä testivaiheen API-avain on vanhentunut).

Sovellusta voi testata [Herokussa](https://tsoha-locations.herokuapp.com/).

Tavoitteet seuraavaan välipalautukseen:
- Working dynamic comment section for sites
- ~~Mapbox integration working (can add actual location for sites)~~
- ~~Navigation bar~~
- Admin user status & tools
- Error handling

## Sovelluksen tarkoitus
Toteutan kurssityötä varten tietokantasovelluksen, johon voidaan tallentaa erilaisia maantieteellisiä kohteita sijainti- ja muine tietoineen. Tässä tapauksessa kyse on ns. muinaisjäännösrekisteristä, eli tietokannasta, jossa on muinaisjäännöskohteita, joilla on ajoitus ja tyyppi. Käyttäjä voi rekisteröidä uuden käyttäjätunnuksen salasanoineen, minkä jälkeen voi kirjautuneena luoda uusia kohteita ja valita niille ajoituksia (esim. pronssikausi, keskiaika) tai tyyppejä (esim. asuinpaikka, hauta). Sovelluksessa voi lisäksi hakea kohteita nimen, tyypin ja ajoituksen perusteella. Admin-oikeuksilla varustetut käyttäjät voivat lisäksi luoda uusia tyyppejä ja ajoituksia sekä poistaa kohteita. 
Tämän lisäksi käyttäjät voivat kommentoida kohteita vapaamuotoisilla viesteillä. Admin-käyttäjät voivat lisäksi muokata tai poistaa viestejä.
Mikäli aikataulu ja sovelluksen eteneminen antavat myöten, toteutan sovellukseen erillisen karttanäkymän (alustavasti Flask-yhteensopivalla Mapboxilla tai jollakin Google Maps -rajapinnalla), jossa xy-muotoisilla sijaintitiedoilla varustetut kohteet voidaan esittää visuaalisesti.



## Tietokannan kuvaus
| Taulu | Sarakkeet |
| ----- | --------- |
| Kohde | nimi, ajoitus_id, tyyppi_id, tekijä_id |
| Käyttäjät | käyttäjänimi, sähköposti, salasana |
| Sijainnit | kohde_id, x, y, z TAI sanallinen kuvaus (paikkakunta) |
| Tyypit | tyyppi_nimi |
| Ajoitukset | ajoituksen_nimi |

## Asennus

## Käyttöohje
