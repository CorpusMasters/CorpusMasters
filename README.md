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





