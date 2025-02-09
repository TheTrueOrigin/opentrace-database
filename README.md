# opentrace-database
Datenbank für OpenTrace mobile App. Füge deine eigenen Produkte hinzu.

## Überblick
Dieses Github-Repository besteht aus drei Hauptteilen:
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

Die Datenbank wird in der Datei `database.db` gespeichert. Sie besteht aus 5 Tabellen:
- `Produkte`
    - `Name` - Produktname
    - `Barcode` - Barcode des Produkts
    - `Unternehmen` - Hersteller des Produkts
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
    - `Name` - Name des Unternehmens
    - `Land` - Herstellungsort des Unternehmens
    - `Gründzung` - Gründungsjahr des Unternehmens
    - `Website` - Website des Unternehmens
- `Bestandteile`
    - `Name` - Name des Bestandteils
    - `Herstellungsort` - Herkunftsland des Bestandteils
    - `Unternehmen` - Hersteller des Bestandteils
- `Allergene`
    - `Allergen` - Name des Allergens
- `Labels`
    - `Label` - Name des Labels
