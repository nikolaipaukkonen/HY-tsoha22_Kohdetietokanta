# Kohdetietokanta
Kurssityö HY Tietokantasovellus -kurssille kesä 2022

## Sovelluksen tarkoitus
Toteutan kurssityötä varten tietokantasovelluksen, johon voidaan tallentaa erilaisia maantieteellisiä kohteita sijainti- ja muine tietoineen. Tässä tapauksessa kyse on ns. muinaisjäännösrekisteristä, eli tietokannasta, jossa on muinaisjäännöskohteita, joilla on ajoitus ja tyyppi. Käyttäjä voi rekisteröidä uuden käyttäjätunnuksen salasanoineen, minkä jälkeen voi kirjautuneena luoda uusia kohteita ja valita niille ajoituksia (esim. pronssikausi, keskiaika) tai tyyppejä (esim. asuinpaikka, hauta). Sovelluksessa voi lisäksi hakea kohteita nimen, tyypin ja ajoituksen perusteella. Admin-oikeuksilla varustetut käyttäjät voivat lisäksi luoda uusia tyyppejä ja ajoituksia sekä poistaa kohteita. 
Tämän lisäksi käyttäjät voivat kommentoida kohteita vapaamuotoisilla viesteillä. Admin-käyttäjät voivat lisäksi muokata tai poistaa viestejä.
Mikäli aikataulu ja sovelluksen eteneminen antavat myöten, toteutan sovellukseen erillisen karttanäkymän (alustavasti Flask-yhteensopivalla Mapboxilla tai jollakin Google Maps -rajapinnalla), jossa xyz-muotoisilla sijaintitiedoilla varustetut kohteet voidaan esittää visuaalisesti.

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
