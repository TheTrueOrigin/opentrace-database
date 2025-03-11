# opentrace-database
Die OpenTrace-Datenbank ist ein Open-Source-Projekt, das es ermöglicht, Informationen zu Produkten und Materialien zu sammeln, zu verwalten und für die OpenTrace Mobile App bereitzustellen. Ziel der App ist es, Benutzern eine transparente und umweltbewusste Entscheidungsfindung zu ermöglichen, indem sie die Herkunft und CO2-Emissionen von Konsumgütern nachverfolgen können.

Diese Datenbank wird durch Beiträge von der Open-Source-Community kontinuierlich erweitert. Jeder kann Produkte und deren Details hinzufügen, aktualisieren oder korrigieren, um sicherzustellen, dass die App stets mit den neuesten und genauesten Informationen versorgt wird. Um eine hohe Qualität der Daten zu gewährleisten, erfolgt die Verwaltung der Beiträge über ein GitHub-Repository, in dem alle Änderungen nachvollziehbar sind.

## Eigenen Beitrag
1. [Produkt hier hinzufügen](https://github.com/TheTrueOrigin/opentrace-database/new/main?filename=Produkte/neu.txt&value=%5BName%5D%20-%0A%5BBarcode%5D%20-%20%28EAN%2013%29%0A%5BUnternehmen%5D%20-%0A%5BGr%C3%B6%C3%9Fe%5D%20-%20%0A%5BGesamtgewicht%5D%20-%20kg%20oder%20g%0A%5BKategorie%5D%20-%0A%5BHerstellungsort%5D%20-%0A%0A%5BExport%5D%0A%5BExportdistanz%5D%20-%20km%0A%5BExporttyp%5D%20-%0A%0A%5BExportdistanz%5D%20-%20km%20%28mehrere%20Exportabschnitte%20m%C3%B6glich%29%0A%5BExporttyp%5D%20-%0A%0A%5BN%C3%A4hrwerte%5D%0A%5BBrennwert%5D%20-%20in%20kj%20und%20in%20kcal%20%28_kJ%2F_kcal%29%0A%5BFettgehalt%5D%20-%20g%0A%5BGes%C3%A4ttigte%20Fetts%C3%A4uren%5D%20-%20g%0A%5BKohlenhydrate%5D%20-%20g%0A%5BZuckergehalt%5D%20-%20g%0A%5BEiwei%C3%9Fgehalt%5D%20-%20g%0A%5BSalzgehalt%5D%20-%20g%0A%0A%5BBestandteil%5D%20-%0A%5BGewicht%5D%20-%20kg%20oder%20g%0A%0A%5BTransport%5D%0A%5BTransportdistanz%5D%20-%20km%0A%5BTransporttyp%5D%20-%0A%0A%5BBestandteil%5D%20-%0A%5BGewicht%5D%20-%20kg%20oder%20g%0A%0A%5BTransport%5D%0A%5BTransportdistanz%5D%20-%20km%0A%5BTransporttyp%5D%20-%0A%0A%5BTransportdistanz%5D%20-%20mehrere%20Transporteabschnitte%2FBestandteile%20m%C3%B6glich%0A%5BTransporttyp%5D%20-%0A%0A%5BAllergene%5D%0A%5BAllergen%5D%20-%0A%5BAllergen%5D%20merhere...%0A%0A%5BLabels%5D%0A%5BLabel%5D%20-%0A%5BLabel%5D%20mehrere...)
2. [Unternehmen hier hinzufügen](https://github.com/TheTrueOrigin/opentrace-database/new/main?filename=Unternehmen/neu.txt&value=[Unternehmen]%0A[Name]%20Name%0A[Land]%20Land%0A[Gründung]%20Gründung%0A[Website]%20Website)
3. [Bestandteil hier hinzufügen](https://github.com/TheTrueOrigin/opentrace-database/new/main?filename=Bestandteile/neu.txt&value=[Bestandteil]%0A[Name]%20Name%0A[Herstellungsort]%20Ort%0A[Unternehmen]%20Unternehmen)

## Überblick
Dieses Github-Repository besteht aus vier Hauptteilen:
- `Produkte` - Produkte, die in der Datenbank verfügbar sind
- `Unternehmen` - Unternehmen, die Produkte/Bestandteile herstellen
- `Bestandteile` - Bestandteile, die in den Produkten enthalten sind
- `Medien` - Medien-Dateien für die Datenbank

> [!TIP]
> Du kannst ein Issue oder einen Pull Request erstellen, um deine eigenen Produkte hinzuzufügen.
> Um deine eigene Datenbank zu erhalten, kannst du entweder die Release-Datei herunterladen oder sie mit `python build.py` erstellen.<br>
> Verwende die Dateien [Produkte-Beispiel](./Produkte/beispiel.txt) und [Unternehmen-Beispiel](./Unternehmen/beispiel.txt) als Vorlagen.

## Format
Um ein neues Produkt zu erstellen, folge dem folgenden Format.
1. Erstelle eine neue Datei im `Produkte` Ordner. Ersetze Leerzeichen mit einem Unterstrich. Das Produkt besteht aus:
- `Name` - Produktname
- `Barcode` - Barcode des Produkts
- `Unternehmen` - Hersteller des Produkts
- `Größe` - Größe des Produkts
- `Gesamtgewicht` - Gewicht des Produkts (kg oder g)
- `Kategorie` - Kategorie des Produkts
- `Herstellungsort` - Herstellungsort des Produkts
- `Export` Mehrere Transportabschnitte
    - `Exportdistanz` - Distanz des Transports
    - `Exporttyp` - Typ des Transports
- `Nährwerte` Nährwerte in 100g/ml aufgeteilt in:
    - `Brennwert` - Brennwert des Produkts
    - `Fettgehalt` - Fettgehalt des Produkts
    - `Gesättigte Fettsäuren` - Gesättigte Fettsäuren des Produkts
    - `Kohlenhydrate` - Kohlenhydrate des Produkts
    - `Zuckergehalt` - Zuckergehalt des Produkts
    - `Eiweißgehalt` - Eiweißgehalt des Produkts
    - `Salzgehalt` - Salzgehalt des Produkts
- `Bestandteile` Mehrere Bestandteile aufgeteilt in:
    - `Bestandteil` - Name des Bestandteils
    - `Gewicht` - Gewicht des Bestandteils
    - `Transport` - Mehrere Transportabschnitte des Produkts
        - `Transportdistanz` - Distanz des Transportabschnitte
        - `Transporttyp` - Transporttyp
- `Allergene` Mehrere Allergene aufgeteilt in:
    - `Allergen` - Name des Allergens
- `Labels` Mehrere Labels aufgeteilt in:
    - `Label` - Name des Labels

> [!TIP]
> Nährwerte gelten pro 100g, bzw. 100ml.<br>
> Export-/Transporttypen sind KSF (Kurzstreckenflug/unter 1000km), LSF (Langstreckenflug), LKW, ZUG, SCHIFF, E (Elektro)<br>
> Nutze für Distanzen auf Land [Google Maps](maps.google.com), auf See [Airrates](airrates.com) und in der Luft [Distance](distance.to)

Beispiel: `bio_joghurt_mild_3,8%_fett_500g.txt`
```
[Name] Bio Joghurt mild 3,8% Fett 500g
[Barcode] 4104060024757
[Unternehmen] Andechser Natur
[Größe] 500g
[Gesamtgewicht] 523g
[Kategorie] Joghurt
[Herstellungsort] Andechs Bayern Deutschland

[Export]
[Exportdistanz] 530km
[Exporttyp] LKW

[Nährwerte]
[Brennwert] 273kJ/65kcal
[Fettgehalt] 3,8g
[Gesättigte Fettsäuren] 2,6g
[Kohlenhydrate] 3,7g
[Zuckergehalt] 3,7g
[Eiweißgehalt] 4,1g
[Salzgehalt] 0,16g

[Bestandteile]
[Bestandteil] Bio-Milch Alpenvorland
[Gewicht] 500g

[Transport]
[Transportdistanz] 38km
[Transporttyp] LKW

[Bestandteil] Europa dünnwandiger Kunststoffbecher
[Gewicht] 15g

[Transport]
[Transportdistanz] 630km
[Transporttyp] LKW

[Bestandteil] Europa Papierbanderole
[Gewicht] 6g

[Transport]
[Transportdistanz] 630km
[Transporttyp] LKW

[Bestandteil] Europa Aluverbundplatine
[Gewicht] 2g

[Transport]
[Transportdistanz] 630km
[Transporttyp] LKW

[Allergene]
[Allergen] Milch
[Allergen] Laktose

[Labels]
[Label] EU-Bio-Siegel
[Label] Bioland
[Label] Bayerisches Bio-Siegel
[Label] Klima-Bauer
```
2. Füge eine Produkt-Bilddatei zum `Medien` Ordner hinzu. Beispiel: `bio_joghurt_mild_3,8%_fett_500g.png`

> [!WARNING]
> Die Datei muss denselben Namen haben wie die Produkt-Datei. Ersetze Leerzeichen mit einem Unterstrich.

3. Erstelle eine Datei für das Unternehmen. Beispiel: `andechser_natur.txt`
```
[Unternehmen]
[Name] Andechser Natur
[Land] Deutschland
[Gründung] 1908
[Website] andechser-natur.de
```
> [!WARNING]
> Die Datei muss denselben Namen haben wie das Unternehmen in der Produkt-Datei. Ersetze Leerzeichen mit einem Unterstrich.

4. Erstelle eine Datei für jedes Bestandteil. Beispiel: `europa_papierbanderole.txt`
```
[Bestandteil]
[Name] Europa Papierbanderole
[Herstellungsort] Europa
[Unternehmen] Unbekannt
```
> [!WARNING]
> Die Datei muss denselben Namen haben wie das Bestandteil in der Produkt-Datei. Ersetze Leerzeichen mit einem Unterstrich.

> [!TIP]
> Wenn ein Bestandteile verschiedene Herstellungsorte hat, erstelle eine Datei für jeden Herstellungsort und füge den 
> Herstellungsort in dem Dateinamen an. Entsprechend muss der Bestandteilname in der Produkt-Datei angepasst werden.

## Zusammenfügen in die Datenbank
Produkt- und Unternehmen-Dateien werden mit `python build.py` zusammengefügt.
Der Skript formatiert alle Produktdetails und Unternehmen und fügt sie der Datenbank hinzu.

Die Datenbank wird in der Datei `database.db` gespeichert. Sie besteht aus 5 Haupttabellen:
- `Produkte`
    - `id` - ID des Produkts
    - `Unternehmen_ID` - ID des Herstellers
    - `Name` - Produktname
    - `Barcode` - Barcode des Produkts
    - `Größe` - Größe des Produkts
    - `Gesamtgewicht` - Gewicht des Produkts
    - `Kategorie` - Kategorie des Produkts
    - `Herstellungsort` - Herstellungsort des Produkts (2-stelliger Ländercode)
    - `Brennwert` - Brennwert des Produkts
    - `Fettgehalt` - Fettgehalt des Produkts
    - `Gesättigte Fettsäuren` - Gesättigte Fettsäuren des Produkts
    - `Kohlenhydrate` - Kohlenhydrate des Produkts
    - `Zuckergehalt` - Zuckergehalt des Produkts
    - `Eiweißgehalt` - Eiweißgehalt des Produkts
    - `Salzgehalt` - Salzgehalt des Produkts
    - `Emission` - Gesamtemissioon des Produkts
    - `Distanz` - Gesamtdistanz des Produkttransports und der Produktbestandteile
- `Unternehmen`
    - `id` - ID des Unternehmens
    - `Name` - Name des Unternehmens
    - `Land` - Herstellungsort des Unternehmens (2-stelliger Ländercode)
    - `Gründung` - Gründungsjahr des Unternehmens
    - `Website` - Website des Unternehmens
- `Bestandteile`
    - `id` - ID des Bestandteils
    - `Unternehmen_ID` - ID des Herstellers
    - `Name` - Name des Bestandteils
    - `Herstellungsort` - Herkunftsland des Bestandteils (2-stelliger Ländercode)
- `Allergene`
    - `id` - ID des Allergens
    - `Allergen` - Name des Allergens
- `Labels`
    - `id` - ID des Labels
    - `Label` - Name des Labels

## Wie werden CO2-Emissionen ausgerechnet
Die CO2-Emission wird mit dieser Formel bestimmt:
```
Distanz * Gewicht * Emissionfaktor
```

Emissionsfaktoren:
```
Kurzsreckenflug: 0.0011
Langstreckenflug: 0.0005
Lastkraftwagen: 0.0001
Zug: 0.00004
Schiff: 0.00003
Elektrisch: 0
```