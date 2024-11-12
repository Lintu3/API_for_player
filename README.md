PelaajaAPI
Ohjelma on tehty ja testattu Python versiolla 3.11.1 ja  VisualStudioCodella.

Visualstudio codea käytettäessä asenna ensin virtualenviroment(venv) ja aktivoi se.
Tämä onnistuu VS Codessa painamalla ctrl + shift + p jonka jälkeen kirjoita python: create enviroment... tämän jälkeen valitse venv.
(muista että .venv kansio on oltava projektin juuressa!)
Odota että se asentuu!

Kun venv on lisätty avaa terminaali, navigoi projektin juureen ja aktivoi venv.
Jos käytät Windows laitetta voit myös avata kansion .venv/Scripts/ ja valita Activate.ps1 (TESTATTU WINDOWS 10!).
(aktivointi tapahtuu eri tavoilla riippuen koneesi käyttöjärjestelmästä!)
Odota että se aktivoituu!

Kun venv on aktivoitu pitäisi terminaalissa polun edessä lukea: (.venv)

Tämän jälkeen kirjoita terminaaliin: pip install fastapi ja paina enter.
Odota että se asentuu!
Tämän jälkeen kirjoita terminaaliin: pip install uvicorn ja paina enter.
Odota että se asentuu!
Tämän jälkeen kirjoita terminaaliin: pip install sqlalchemy ja paina enter.
Odota että se asentuu!
Nyt pitäisi olla kaikki mitä tarvitset.

Käynnistä uvicorn komennolla: uvicorn app.main:app --reload
Varmista että playerapi_db.db tiedosto ilmestyy kansion juureen.

Avaa selain ja mene osoitteeseen 127.0.0.1:8000/docs

Aja ohjelmaa.
