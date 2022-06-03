# Tačka u mnogouglu

Za izradu ovog zadatka sam koristio programski jezik **Python**.

## Kako program radi

Prilikom pokretanja programa, od korisnika se traži da unese broj tačaka mnogougla.
Unesena vrednost mora biti broj i mora biti veća od 2. Zato što da bi konstruisali mnogougao potrebno nam je 3 ili više tačaka. Zatim se od korisinika traži da unese X i Y koordinate za svaku tačku. Vrednost koordinate može biti ceo broj ili decimalni broj i program ne prihvata druge tipove vrednosti. Program ne dozvoljava unos istih tačaka. Kada se unesu koordinate svih tačaka od korisnika se traži da unese koordinate tačke za koju želi da proveri da li se nalazi u mnogouglu ili ne. Nakon unosa tačke se sortiraju u smeru suprotnom od kazaljke na satu u slučaju da korisnik unese tačke u pogrešnom redosledu. Sortiranje se vrši tako što se prvo nadje tačka koja predstavlja centar mnogougla, zatim konstruišemo vektor od centra i tačke koja je pomerena za 1 po X osi od centra. Za svaku tačku konstruišemo vektor izmedju centra i te tačke i računamo ugao izmedju tog i centralnog vektora i na osnovu vrednosti tih uglova sortiramo tačke. Posle sortiranja program proverava da li je mnogougao konveksan, i ako nije izvršenje programa će biti prekinut sa porukom da mnogougao nije konveksan. Konveksnost se proverava tako što za svaku tačku konstruišemo dva vektora(stranice mnogougla) od te i sledeće naredne dve tačke. Proizvod ta dva vektora nam govori da li je drugi vektor od ta dva "nagnut" u levu stranu(zato što se krećemo u smeru suprotnom od kazaljke na satu), ukoliko nije mnogougao nije konveksan. Posle provere konveksnosti program proverava za svaki vektor(stranicu) da li se tražena tačka nalazi sa njene leve strane(zato što se krećemo u smeru suprotnom od kazaljke na satu). Ova provera se vrši na sličan način kao provera konveksnosti sa razlikom da se drugi vektor konstruiše izmedju tražene tačke i tačke na kraju prvog vektora. Ukoliko se tačka nalazi sa leve strane svakog vektora(stranice) tačka se nalazi u mnogouglu. Na kraju program ispisuje rezultat na konzolu i otvara novi prozor u kome je prikazan grafik mnogougla i pozicija tražene tačke. Izvršenje programa može biti prekinuto u svakom trenutku pritiskom ctrl-c.

## Pokretanje programa

Pre pokretanje programa potrebno je instalirati mathplotlib paket.
```
pip install matplotlib
```

Program se pokreće komandom:

```
./main.py
```
Ili:
```
python3 main.py
```

## Testiranje programa

Za testiranje programa je potreban pytest paket.
```
pip install pytest
```
Test se pokreće komandom:
```
pytest polygon_test.py
```
