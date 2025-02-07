# opentrace-database
Datenbank für OpenTrace mobile App. Füge deine eigenen Produkte hinzu.

## Überblick
Dieses Github-Repository besteht aus drei Hauptfeldern:
- `Produkte` - Produkte, die in der Datenbank verfügbar sind
- `Zutaten` - Zutaten, aus denen die Produkte bestehen
- `Unternehmen` - Unternehmen, die die Produkte herstellen
- `Medien` - Medien-Dateien für die Datenbank
- `Nährwerte` - Nährwerte für die Produkte
- `Allergene` - Allergene für die Produkte
- `Labels` - Labels für die Produkte

> [!TIP]
> Du kannst ein Issue oder einen Pull Request erstellen, um deine eigenen Produkte hinzuzufügen.
> Um deine eigene Datenbank zu erhalten, kannst du entweder die Release-Datei herunterladen oder sie mit `python build.py` erstellen.

## Format
Um ein neues Produkt zu erstellen, folge dem folgenden Format. Beispiel: Meßmer Tee Klassik
1. Erstelle eine neue Datei im `Produkte` Ordner. Beispiel: `meßmer-tee-klassik.txt`
```
[Produkt]
[Name] Meßmer Tee Klassik
[Barcode] 4001257218503
[Unternehmen] Meßmer
[Größe] 20pcs
[Kategorie] Tee
```
2. Füge eine Produkt-Bilddatei zum `Medien` Ordner hinzu. Beispiel: `meßmer-tee-klassik.png`
3. Füge eine Unternehmen-Datei zum `Unternehmen` Ordner hinzu. Beispiel: `meßmer.txt`
```
[Unternehmen]
[Name] Meßmer
[Land] Österreich
[Gründzung] 1990
[Website] https://www.meßmer.at
```
4. Füge eine Zutatendatei zum `Zutaten` Ordner hinzu. Beispiel: `meßmer-tee-klassik.txt`
```
[Zutaten]
[Zutat] Tata Tea Limited Schwarztee Blätter
[Herkunftsland] Indien
[Unternehmen] Tata Tea Limited

[Zutat] Nalli Silks Seide
[Herkunftsland] Indien
[Unternehmen] Nalli Silks Seide

[Zutat] Geissinger Karton Verpackung
[Herkunftsland] Österreich
[Unternehmen] Geissinger
```
4. Füge eine Nährwertdatei zum `Nährwerte` Ordner hinzu. Beispiel: `meßmer-tee-klassik.txt`. (pro 100g/ml)
```
[Nährwerte]
[Brennwert] 3kJ/1kcal
[Fett] 0g
[Gesättigte Fettsäuren] 0g
[Kohlenhydrate] 0.2g
[Zucker] 0.1g
[Eiweiß] 0g
[Salz] 0,01g
```
5. Füge eine Allergenen-Datei zum `Allergene` Ordner hinzu. Beispiel: `meßmer-tee-klassik.txt`
```
[Allergene]
[Allergen] Histamin
```
6. Füge eine Labels-Datei zum `Labels` Ordner hinzu. Beispiel: `meßmer-tee-klassik.txt`
```
[Labels]
[Label] Glutenfrei
```
## Zusammenfügen in die Datenbank
Nachdem alle Dateien erstellt wurden, kannst du sie mit `python build.py` zusammenfügen.
Der Skript formatiert alle Allergene, Labels, Nährwerte, Unternehmen, Zutaten und Produkte und fügt sie der Datenbank hinzu.
> [!WARNING]
> Allergene, Labels, Nährwerte, Zutaten und Medien müssen dieselbe Bezeichnung wie die Produkt-Datei haben. (Bsp: meßmer-tee-klassik.txt) <br>
Die Datenbank wird in der Datei `database.db` gespeichert. Sie besteht aus 6 Tabellen:
- `Produkte` - Produkte, die in der Datenbank verfügbar sind
- `Zutaten` - Zutaten, aus denen die Produkte bestehen
- `Unternehmen` - Unternehmen, die die Produkte herstellen
- `Nährwerte` - Nährwerte für die Produkte
- `Allergene` - Allergene für die Produkte
- `Labels` - Labels für die Produkte
