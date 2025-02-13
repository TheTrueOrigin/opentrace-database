# opentrace-database
Die OpenTrace-Datenbank ist ein Open-Source-Projekt, das es ermöglicht, Informationen zu Produkten und Materialien zu sammeln, zu verwalten und für die OpenTrace Mobile App bereitzustellen. Ziel der App ist es, Benutzern eine transparente und umweltbewusste Entscheidungsfindung zu ermöglichen, indem sie die Herkunft und CO2-Emissionen von Konsumgütern nachverfolgen können.

Diese Datenbank wird durch Beiträge von der Open-Source-Community kontinuierlich erweitert. Jeder kann Produkte und deren Details hinzufügen, aktualisieren oder korrigieren, um sicherzustellen, dass die App stets mit den neuesten und genauesten Informationen versorgt wird. Um eine hohe Qualität der Daten zu gewährleisten, erfolgt die Verwaltung der Beiträge über ein GitHub-Repository, in dem alle Änderungen nachvollziehbar sind.

## Eigenen Beitrag
1. Fork der Repository erstellen
2. Eigenen Fork clonen `git clone https://github.com/username/opentrace-database`
3. Änderungen vornehmen (s. unten)
4. Pull-Request erstellen

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
- `Herstellungsort` - Herstellungsort des Produkts
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

Beispiel: `meßmer_tee_klassik.txt`
```
[Name] Meßmer Tee Klassik
[Barcode] 4001257218503
[Unternehmen] Meßmer
[Größe] 20pcs
[Kategorie] Tee
[Herstellungsort] Österreich

[Nährwerte]
[Brennwert] 3kJ/1kcal
[Fettgehalt] 0g
[Gesättigte Fettsäuren] 0g
[Kohlenhydrate] 0.2g
[Zuckergehalt] 0.1g
[Eiweißgehalt] 0g
[Salzgehalt] 0,01g

[Bestandteile]
[Bestandteil] Tata Tea Limited Schwarztee Blätter
[Bestandteil] Nalli Silks Seide
[Bestandteil] Geissinger Karton Verpackung

[Allergene]
[Allergen] Histamin

[Labels]
[Label] Glutenfrei
```
2. Füge eine Produkt-Bilddatei zum `Medien` Ordner hinzu. Beispiel: `meßmer_tee_klassik.png`

> [!WARNING]
> Die Datei muss denselben Namen haben wie die Produkt-Datei. Ersetze Leerzeichen mit einem Unterstrich.

3. Erstelle eine Datei für das Unternehmen. Beispiel: `meßmer.txt`
```
[Unternehmen]
[Name] Meßmer
[Land] Österreich
[Gründung] 1990
[Website] https://www.meßmer.at
```
> [!WARNING]
> Die Datei muss denselben Namen haben wie das Unternehmen in der Produkt-Datei. Ersetze Leerzeichen mit einem Unterstrich.

4. Erstelle eine Datei für jedes Bestandteil. Beispiel: `tata_tea_limited_schwarztee_blätter.txt`
```
[Bestandteil]
[Name] Tata Tea Limited Schwarztee Blätter
[Herstellungsort] Indien
[Unternehmen] Tata Tea Limited
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
    - `Herstellungsort` - Herstellungsort des Produkts
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
    - `Land` - Herstellungsort des Unternehmens
    - `Gründzung` - Gründungsjahr des Unternehmens
    - `Website` - Website des Unternehmens
- `Bestandteile`
    - `id` - ID des Bestandteils
    - `Unternehmen_ID` - ID des Herstellers
    - `Name` - Name des Bestandteils
    - `Herstellungsort` - Herkunftsland des Bestandteils
- `Allergene`
    - `id` - ID des Allergens
    - `Allergen` - Name des Allergens
- `Labels`
    - `id` - ID des Labels
    - `Label` - Name des Labels

## Endpunkte
- GET `/produkt/id/{id}` - Gibt das Produkt mit jeweiliger ID im JSON-Format aus
- GET `/produkt/barcode/{barcode}` - Gibt das Produkt mit jeweiligem Barcode im JSON-Format aus
- GET `/produkt/name/{name}` - Gibt Produkte mit ähnlichem Namen im JSON-Format aus
- POST `/produkt/create` - Erstelle ein Produkt

## Produkt JSON-Schema
Beispiel: `Meßmer Tee Klassik`
```json
{
  "Name": "Meßmer Tee Klassik",
  "Unternehmen": {
    "Name": "Meßmer",
    "Land": "Österreich",
    "Gründung": 1990,
    "Website": "meßmer.at"
  },
  "Barcode": "4001257218503",
  "Größe": "20pcs",
  "Kategorie": "Tee",
  "Herstellungsort": "Österreich",
  "Nährwerte": {
    "Brennwert": "3kJ/1kcal",
    "Fettgehalt": "0g",
    "Gesättigte_Fettsäuren": "0g",
    "Kohlenhydrate": "0.2g",
    "Zuckergehalt": "0.1g",
    "Eiweißgehalt": "0g",
    "Salzgehalt": "0,01g"
  },
  "Labels": [
    "Glutenfrei"
  ],
  "Allergene": [
    "Histamin"
  ],
  "Bestandteile": [
    {
      "Name": "Nalli Silks Seide",
      "Herstellungsort": "Indien",
      "Unternehmen": {
        "Name": "Nalli Silks",
        "Land": "Indien",
        "Gründung": 1990,
        "Website": "nallisilks.com"
      }
    },
    {
      "Name": "Tata Tea Limited Schwarztee Blätter",
      "Herstellungsort": "Indien",
      "Unternehmen": {
        "Name": "Tata Tea Limited",
        "Land": "Indien",
        "Gründung": 1893,
        "Website": "tata.com"
      }
    },
    {
      "Name": "Geissinger Karton Verpackung",
      "Herstellungsort": "Österreich",
      "Unternehmen": {
        "Name": "Geissinger",
        "Land": "Österreich",
        "Gründung": 1990,
        "Website": "geissinger.at"
      }
    }
  ]
}
```
