# opentrace-database
Die OpenTrace-Datenbank ist ein Open-Source-Projekt, das es ermöglicht, Informationen zu Produkten und Materialien zu sammeln, zu verwalten und für die OpenTrace Mobile App bereitzustellen. Ziel der App ist es, Benutzern eine transparente und umweltbewusste Entscheidungsfindung zu ermöglichen, indem sie die Herkunft und CO2-Emissionen von Konsumgütern nachverfolgen können.

Diese Datenbank wird durch Beiträge von der Open-Source-Community kontinuierlich erweitert. Jeder kann Produkte und deren Details hinzufügen, aktualisieren oder korrigieren, um sicherzustellen, dass die App stets mit den neuesten und genauesten Informationen versorgt wird. Um eine hohe Qualität der Daten zu gewährleisten, erfolgt die Verwaltung der Beiträge über ein GitHub-Repository, in dem alle Änderungen nachvollziehbar sind.

## Eigenen Beitrag
1. [Produkt hier hinzufügen](https://github.com/TheTrueOrigin/opentrace-database/new/main?filename=Produkte/neu.txt&value=[Name]%20Name%0A[Barcode]%20Barcode%0A[Unternehmen]%20Unternehmen%0A[Größe]%20Größe%0A[Kategorie]%20Kategorie%0A[Herstellungsort]%20Ort%0A%0A[Nährwerte]%0A[Brennwert]%20Brennwert%0A[Fettgehalt]%20Fettgehalt%0A[Gesättigte%20Fettsäuren]%20Gesättigte%20Fettsäuren%0A[Kohlenhydrate]%20Kohlenhydrate%0A[Zuckergehalt]%20Zuckergehalt%0A[Eiweißgehalt]%20Eiweißgehalt%0A[Salzgehalt]%20Salzgehalt%0A%0A[Bestandteile]%0A[Bestandteil]%20Bestandteil%201%0A[Bestandteil]%20Bestandteil%202%20%0A(weitere%20Bestandteile)%0A%0A[Allergene]%0A[Allergen]%20Allergen%201%0A[Allergen]%20Allergen%202%0A(weitere%20Allergene)%0A%0A[Labels]%0A[Label]%20Label%201%0A[Label]%20Label%202%0A(weitere%20Labels))
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
- `Kategorie` - Kategorie des Produkts
- `Herstellungsort` - Herstellungsort des Produkts (2-stelliger Ländercode)
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
- `Allergene` Mehrere Allergene aufgeteilt in:
    - `Allergen` - Name des Allergens
- `Labels` Mehrere Labels aufgeteilt in:
    - `Label` - Name des Labels

> [!TIP]
> Nährwerte gelten pro 100g, bzw. 100ml.

Beispiel: `bio_joghurt_mild_3,8%_fett_500g.txt`
```
[Name] Bio Joghurt mild 3,8% Fett 500g
[Barcode] 4104060024757
[Unternehmen] Andechser Natur
[Größe] 150g
[Kategorie] Joghurt
[Herstellungsort] Andechs Bayern Deutschland

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
[Bestandteil] Europa dünnwandiger Kunststoffbecher
[Bestandteil] Europa Papierbanderole
[Bestandteil] Europa Aluverbundplatine

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
    - `Kategorie` - Kategorie des Produkts
    - `Herstellungsort` - Herstellungsort des Produkts (2-stelliger Ländercode)
    - `Brennwert` - Brennwert des Produkts
    - `Fettgehalt` - Fettgehalt des Produkts
    - `Gesättigte Fettsäuren` - Gesättigte Fettsäuren des Produkts
    - `Kohlenhydrate` - Kohlenhydrate des Produkts
    - `Zuckergehalt` - Zuckergehalt des Produkts
    - `Eiweißgehalt` - Eiweißgehalt des Produkts
    - `Salzgehalt` - Salzgehalt des Produkts
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
