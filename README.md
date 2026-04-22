# CorpusMasters
Sudionici projekta:
1. Filip Jović
2. Nika Marinović
3. Ema Tkalec Cavor
# Opis projekta
Projekt se bavi izradom korpusa recenzija doktora preuzetih sa stranice [najdoktor.com](https://najdoktor.com/) te analizom sentimenata nad istima.
Projekt je pokrenut u sklopu kolegija _Obrada prirodnog jezika_ na Filozofskom fakultetu Sveučilišta u Zagrebu.

Za prikupljanje recenzija korišten je program za skrapiranje podataka sa Web-a, koji je razvila grupa [xSentilytics](https://github.com/xSentilytics). Program koristi **Selenium WebDriver** za upravljanje web-preglednikom i dohvaćanje recenzija. Njihov kod modificiran je na nekoliko načina:
- Za razdvajanje rečenica umjesto biblioteke **CLASSLA** koristili smo biblioteku **spaCy**, koja se pokazala učinkovitijom.
- Umjesto Safarija, korišten je web-preglednik Google Chrome.
- Kratice poput _dr._ i _dr.sc._ privremeno se zamjenjuju sa istima bez točke, kako bi se spriječilo pogrešno razdvajanje rečenica. Nakon obrade se vraćaju u izvorni oblik.

Program čita _.py_ datoteku u kojoj su zapisana imena doktora uz pripadajuće linkove. 

Nakon pokretanja programa, dobivena _.xlsx_ datoteka ručno je dorađena kako bi se uklonile manje greške.

# Pilot anotiranje
Kao početna faza projekta provedeno je pilot anotiranje sentimenata 150 nasumično odabranih rečenica iz korupsa kako bi se testirala usklađenost članova tima. Kako ne bi došlo do pristranosti, anotacija je provedena individualno, na način da niti jedan član grupe u trenutku anotiranja ne zna kako su drugi članovi anotirali rečenice. Nakon završetka anotacije, izračunata je _fleiss's kappa_ vrijednost, koja predstavlja stupanj slaganja anotatora. Ista iznosti 0.73, što znači da je slaganje anotatora dovoljno pouzdano.

Sentiment se anotira prema 5-stupanjskoj ljestvici:

**negative**: negativan sentiment

**neutral**: neutralan sentiment

**positive**: pozitivan sentiment

**mixed**: dio rečenice je pozitivan, a dio negativan

**sarcasm**: sarkastični i ironični komentari.

# Finalno anotiranje
Nakon pilot anotiranja provedeno je i kompletno anotiranje svih 2611 rečenica u korpusu, prema istoj 5-stupanjskoj ljestvici.
Anotiranje su ponovno individualno provela sva 3 člana tima, a nakon toga je za data curator ulogu pronađena osoba iz drugog tima, koja je na temelju 3 anotacije odredila onu finalnu. Na kraju su dobivene 2 datoteke - jedna sa svim anotacijama članova, a druga samo sa finalnom. Obje datoteke konvertirane su u _.csv_ format.

Raspored poslova:

Annotation 1: Nika Marinović

Annotation 2: Ema Tkalec Cavor

Annotation 3: Filip Jović

Data curator: Toni Pernar ([xSentilytics](https://github.com/xSentilytics))






