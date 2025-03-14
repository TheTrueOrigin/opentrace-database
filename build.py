### Build.py

### Imports ###
import sqlite3
import os
import json

### Prod-Pfad ###
produkte_pfad = os.path.join(os.path.dirname(__file__), "Produkte")

### Unternehmen-Pfad ###
unternehmen_pfad = os.path.join(os.path.dirname(__file__), "Unternehmen")

### Bestandteile-Pfad ###
bestandteile_pfad = os.path.join(os.path.dirname(__file__), "Bestandteile")

### Medien-Pfad ###
medien_pfad = os.path.join(os.path.dirname(__file__), "Medien")

### Datenbank-Pfad ###
db_pfad = os.path.join(os.path.dirname(__file__), "database.db")

# Faktoren
with open(os.path.join(os.path.dirname(__file__), "faktoren.json"), "r") as f:
    faktoren = json.load(f)

# Emission ausrechnen mit Distanz, Typ und Faktor
def emission_berechnen(distanz, typ, masse):
    # Flüge Great Circle Distance + 95km
    # Straßen 1,05*Distanz
    # Wasser 1,15*Distanz
    # Schienen nichts
    if typ in ["FLUG"]:
        return (distanz+95)*faktoren[typ]*masse
    if typ in ["LKW"]:
        return 1.05*distanz*faktoren[typ]*masse
    if typ in ["SCHIFF"]:
        return 1.15*distanz*faktoren[typ]*masse
    return distanz*faktoren[typ]*masse

### Zusammenfügen der Informationen ###
# Unternehmen
unternehmen = {}
for unternehmen_datei in [unternehmen for unternehmen in os.listdir(unternehmen_pfad) if unternehmen.endswith(".txt") and not "beispiel" in os.path.splitext(unternehmen)[0]]:
    unternehmen_name = " ".join(word.capitalize() for word in os.path.splitext(unternehmen_datei)[0].strip().split())
    unternehmen[unternehmen_name] = {}
    _unternehmen_pfad = os.path.join(unternehmen_pfad, unternehmen_datei)
    with open(_unternehmen_pfad, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("[Name]"):
                name = line[6:].strip()
                if unternehmen_name.lower() != name.replace(" ", "_").lower():
                    raise Exception(f"Unternehmensname {name} stimmt nicht mit Dateiname '{unternehmen_name.lower()}.txt' überein")
                unternehmen[unternehmen_name]["Name"] = name
            elif line.startswith("[Land]"):
                unternehmen[unternehmen_name]["Land"] = line[6:].strip()
            elif line.startswith("[Gründung]"):
                unternehmen[unternehmen_name]["Gründung"] = line[10:].strip()
            elif line.startswith("[Website]"):
                unternehmen[unternehmen_name]["Website"] = line[9:].strip()

# Bestandteile
bestandteile = {}
for bestandteil_datei in [bestandteil for bestandteil in os.listdir(bestandteile_pfad) if bestandteil.endswith(".txt") and not "beispiel" in os.path.splitext(bestandteil)[0]]:
    bestandteil_name = " ".join(word.capitalize() for word in os.path.splitext(bestandteil_datei)[0].strip().split())
    bestandteile[bestandteil_name] = {}
    bestandteil_pfad = os.path.join(bestandteile_pfad, bestandteil_datei)
    with open(bestandteil_pfad, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("[Name]"):
                name = line[6:].strip()
                if bestandteil_name.lower() != name.replace(" ", "_").lower():
                    raise Exception(f"Bestandteilsname {name} stimmt nicht mit Dateiname '{bestandteil_name.lower()}.txt' überein")
                bestandteile[bestandteil_name]["Name"] = name
            elif line.startswith("[Herstellungsort]"):
                bestandteile[bestandteil_name]["Herstellungsort"] = line[17:].strip()
            elif line.startswith("[Unternehmen]"):
                bestandteile[bestandteil_name]["Unternehmen"] = line[13:].strip()
# Produkte
produkte = {}
for produkt_datei in [produkt for produkt in os.listdir(produkte_pfad) if produkt.endswith(".txt") and not "beispiel" in os.path.splitext(produkt)[0]]:
    produkt_name = " ".join(word.capitalize() for word in os.path.splitext(produkt_datei)[0].strip().split())
    produkte[produkt_name] = {}
    produkt_pfad = os.path.join(produkte_pfad, produkt_datei)
    with open(produkt_pfad, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("[Name]"):
                name = line[6:].strip()
                if produkt_name.lower() != name.replace(" ", "_").lower():
                    raise Exception(f"Produktname {name} stimmt nicht mit Dateiname '{produkt_name}.txt' überein")
                if not os.path.exists(os.path.join(medien_pfad, "{}.jpg".format(name.replace(" ", "_").lower()))):
                    raise Exception(f"Kein Medium für Produkt {name}")
                produkte[produkt_name]["Name"] = name
            elif line.startswith("[Barcode]"):
                produkte[produkt_name]["Barcode"] = line[9:].strip()
            elif line.startswith("[Unternehmen]"):
                produkte[produkt_name]["Unternehmen"] = line[13:].strip()
            elif line.startswith("[Größe]"):
                produkte[produkt_name]["Größe"] = line[7:].strip()
            elif line.startswith("[Gesamtgewicht]"):
                gewicht = line[15:].strip()
                if "kg" in gewicht:
                    gewicht = int(gewicht.replace("kg", "").strip())
                elif "g" in gewicht:
                    gewicht = int(gewicht.replace("g", "").strip())/1000
                produkte[produkt_name]["Gesamtgewicht"] = gewicht
            elif line.startswith("[Kategorie]"):
                produkte[produkt_name]["Kategorie"] = line[11:].strip()
            elif line.startswith("[Herstellungsort]"):
                produkte[produkt_name]["Herstellungsort"] = line[17:].strip()
            elif line.startswith("[Exportdistanz]"):
                distanz = line[15:].strip()
                if not "Exportdistanz" in produkte[produkt_name]:
                    produkte[produkt_name]["Exportdistanz"] = []
                if "km" in distanz:
                    distanz = int(distanz.replace("km", "").strip())
                else:
                    raise Exception(f"Bitte die Exportdistanz {distanz} in km eingeben bei {produkt_name}.txt")
                produkte[produkt_name]["Exportdistanz"].append(distanz)
            elif line.startswith("[Exporttyp]"):
                typ = line[11:].strip()
                if not "Exporttyp" in produkte[produkt_name]:
                    produkte[produkt_name]["Exporttyp"] = []
                    produkte[produkt_name]["Exportfaktor"] = []
                    produkte[produkt_name]["Exportemission"] = []
                if typ not in faktoren:
                    typen = list(faktoren.keys())
                    raise Exception(f"Bitte einen der Typen {typen} in {produkt_name}.txt wählen")
                produkte[produkt_name]["Exporttyp"].append(typ)
                produkte[produkt_name]["Exportfaktor"].append(faktoren[typ])
                emission = emission_berechnen(produkte[produkt_name]["Exportdistanz"][-1], produkte[produkt_name]["Exporttyp"][-1], produkte[produkt_name]["Gesamtgewicht"])
                produkte[produkt_name]["Exportemission"].append(emission)
            
            elif line.startswith("[Brennwert]"):
                produkte[produkt_name]["Brennwert"] = line[11:].strip()
            elif line.startswith("[Fettgehalt]"):
                produkte[produkt_name]["Fettgehalt"] = line[12:].strip()
            elif line.startswith("[Gesättigte Fettsäuren]"):
                produkte[produkt_name]["Gesättigte Fettsäuren"] = line[23:].strip()
            elif line.startswith("[Kohlenhydrate]"):
                produkte[produkt_name]["Kohlenhydrate"] = line[15:].strip()
            elif line.startswith("[Zuckergehalt]"):
                produkte[produkt_name]["Zuckergehalt"] = line[14:].strip()
            elif line.startswith("[Eiweißgehalt]"):
                produkte[produkt_name]["Eiweißgehalt"] = line[14:].strip()
            elif line.startswith("[Salzgehalt]"):
                produkte[produkt_name]["Salzgehalt"] = line[12:].strip()

            elif line.startswith("[Bestandteile]"):
                produkte[produkt_name]["Bestandteile"] = []
            elif line.startswith("[Bestandteil]"):
                produkte[produkt_name]["Bestandteile"].append({"Name": line[13:].strip(), "Transportdistanz": [], "Transporttyp": [], "Transportfaktor": [], "Transportemission": []})
            elif line.startswith("[Transportdistanz]"):
                if "km" in line[18:]:
                    distanz = int(line[18:].replace("km", "").strip())
                else:
                    raise Exception(f"Bitte die Transportdistanz {line[18:].strip()} in km eingeben bei {produkt_name}.txt")
                produkte[produkt_name]["Bestandteile"][-1]["Transportdistanz"].append(distanz)
            elif line.startswith("[Transporttyp]"):
                typ = line[14:].strip()
                if typ not in faktoren:
                    typen = list(faktoren.keys())
                    raise Exception(f"Bitte einen der Typen {typen} in {produkt_name}.txt wählen")
                produkte[produkt_name]["Bestandteile"][-1]["Transporttyp"].append(typ)
                produkte[produkt_name]["Bestandteile"][-1]["Transportfaktor"].append(faktoren[typ])
                emission = emission_berechnen(produkte[produkt_name]["Bestandteile"][-1]["Transportdistanz"][-1], produkte[produkt_name]["Bestandteile"][-1]["Transporttyp"][-1], produkte[produkt_name]["Bestandteile"][-1]["Transportfaktor"][-1])
                produkte[produkt_name]["Bestandteile"][-1]["Transportemission"].append(emission)
            elif line.startswith("[Gewicht]"):
                gewicht = line[9:].strip()
                if "kg" in gewicht:
                    gewicht = int(gewicht.replace("kg", "").strip())
                elif "g" in gewicht:
                    gewicht = int(gewicht.replace("g", "").strip())/1000
                else:
                    raise Exception(f"Bitte das Gewicht {gewicht} in g oder kg eingeben bei {produkt_name}.txt")
                produkte[produkt_name]["Bestandteile"][-1]["Gewicht"] = gewicht

            elif line.startswith("[Allergene]"):
                produkte[produkt_name]["Allergene"] = []
            elif line.startswith("[Allergen]"):
                produkte[produkt_name]["Allergene"].append(line[10:].strip())

            elif line.startswith("[Labels]"):
                produkte[produkt_name]["Labels"] = []
            elif line.startswith("[Label]"):
                produkte[produkt_name]["Labels"].append(line[7:].strip())

    gesamt_emission = 0
    gesamt_distanz = 0
    if len(produkte[produkt_name]["Exportdistanz"]) != len(produkte[produkt_name]["Exporttyp"]):
        raise (f"Bitte gleich viele Exportdistanzen wie Exporttypen in {produkt_name}.txt")
    else:
        gesamt_emission += sum(produkte[produkt_name]["Exportemission"])
        gesamt_distanz += sum(produkte[produkt_name]["Exportdistanz"])
    for bestandteil in produkte[produkt_name]["Bestandteile"]:
        if len(bestandteil["Transportdistanz"]) != len(bestandteil["Transporttyp"]):
            raise (f"Bitte gleich viele Transportdistanzen wie Transporttypen im Bestandteil {bestandteil["Name"]} in {produkt_name}.txt")
        else:
            gesamt_emission += sum(bestandteil["Transportemission"])
            gesamt_distanz += sum(bestandteil["Transportdistanz"])
    produkte[produkt_name]["Emission"] = gesamt_emission
    produkte[produkt_name]["Distanz"] = gesamt_distanz

### Datenbank erstellen ###
# Datenbank löschen, falls sie existiert
if os.path.exists(db_pfad):
    os.remove(db_pfad)
conn = sqlite3.connect(db_pfad)
cursor = conn.cursor()

# Unternehmen
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Unternehmen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Land TEXT,
        Gründung INTEGER,
        Website TEXT
    );
    """)

# Produkte
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Produkte (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Unternehmen_ID INTEGER,
        Name TEXT,
        Barcode TEXT,
        Größe TEXT, 
        Gesamtgewicht INTEGER,
        Kategorie TEXT, 
        Herstellungsort TEXT, 
        Brennwert TEXT, 
        Fettgehalt TEXT, 
        Gesättigte_Fettsäuren TEXT,
        Kohlenhydrate TEXT, 
        Zuckergehalt TEXT, 
        Eiweißgehalt TEXT, 
        Salzgehalt TEXT,
        Emission FLOAT,
        Distanz INTEGER,
        FOREIGN KEY (Unternehmen_ID) REFERENCES Unternehmen(id) ON DELETE CASCADE
    );
    """)

# Allergene
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Allergene (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        Allergen TEXT
    );
    """)

# Labels
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Labels (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        Label TEXT
    );
    """)

# Bestandteile
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Bestandteile (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Unternehmen_ID INTEGER,
        Name TEXT,
        Herstellungsort TEXT,
        FOREIGN KEY (Unternehmen_ID) REFERENCES Unternehmen(id) ON DELETE CASCADE
    );
    """)

# Produkte_Export
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Produkte_Export (
        Exportdistanzen_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Produkt_ID INTEGER,
        Distanz INTEGER,
        Typ TEXT,
        Faktor FLOAT,
        Emission FLOAT, 
        FOREIGN KEY (Produkt_ID) REFERENCES Produkt(id) ON DELETE CASCADE
    );
    """)

# Produkte_Labels
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Produkte_Labels (
        Produkt_ID INTEGER, 
        Label_ID INTEGER,
        PRIMARY KEY (Produkt_ID, Label_ID),
        FOREIGN KEY (Produkt_ID) REFERENCES Produkte(id) ON DELETE CASCADE,
        FOREIGN KEY (Label_ID) REFERENCES Labels(id) ON DELETE CASCADE
    );
    """)

# Produkte_Allergene
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Produkte_Allergene (
        Produkt_ID INTEGER, 
        Allergen_ID INTEGER,
        PRIMARY KEY (Produkt_ID, Allergen_ID),
        FOREIGN KEY (Produkt_ID) REFERENCES Produkte(id) ON DELETE CASCADE,
        FOREIGN KEY (Allergen_ID) REFERENCES Allergene(id) ON DELETE CASCADE
    );
    """)

# Produkte_Bestandteile
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Produkte_Bestandteile (
        Produkt_ID INTEGER, 
        Bestandteil_ID INTEGER,
        Gewicht INTEGER,
        PRIMARY KEY (Produkt_ID, Bestandteil_ID),
        FOREIGN KEY (Produkt_ID) REFERENCES Produkte(id) ON DELETE CASCADE,
        FOREIGN KEY (Bestandteil_ID) REFERENCES Bestandteile(id) ON DELETE CASCADE
    );
    """)

# Produkt_Bestandteile_Transport
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Produkte_Bestandteile_Transport (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Produkt_ID INTEGER,
        Bestandteil_ID INTEGER,
        Distanz INTEGER,
        Typ TEXT,
        Faktor FLOAT,
        Emission FLOAT,
        FOREIGN KEY (Produkt_ID, Bestandteil_ID) REFERENCES Produkte_Bestandteile(Produkt_ID, Bestandteil_ID) ON DELETE CASCADE
    );
    """)

### Datenbank füllen ###
# Unternehmen
unternehmen_ids = {}
for unternehmen_name, unternehmen_info in unternehmen.items():
    if unternehmen_info["Name"] not in unternehmen_ids:
        cursor.execute("""
            INSERT INTO Unternehmen (Name, Land, Gründung, Website) VALUES (?, ?, ?, ?);
        """, (unternehmen_info["Name"], unternehmen_info["Land"], unternehmen_info["Gründung"], unternehmen_info["Website"]))
        unternehmen_ids[unternehmen_info["Name"]] = cursor.lastrowid

# Allergene
# Labels
allergenen_ids = {}
labels_ids = {}

for produkt_name, produkt_info in produkte.items():
    for allergen_name in produkt_info["Allergene"]:
        if allergen_name not in allergenen_ids:
            cursor.execute("""
                INSERT INTO Allergene (Allergen) VALUES (?);
            """, (allergen_name,))
            allergenen_ids[allergen_name] = cursor.lastrowid
    
    for label_name in produkt_info["Labels"]:
        if label_name not in labels_ids:
            cursor.execute("""
                INSERT INTO Labels (Label) VALUES (?);
            """, (label_name,))
            labels_ids[label_name] = cursor.lastrowid

# Bestandteile
bestandteile_ids = {}
for bestandteil_name, bestandteil_info in bestandteile.items():
    if bestandteil_info["Name"] not in bestandteile_ids:
        unternehmen_name = bestandteil_info["Unternehmen"]
        unternehmen_id = unternehmen_ids[unternehmen_name]
        cursor.execute("""
            INSERT INTO Bestandteile (Unternehmen_ID, Name, Herstellungsort) VALUES (?, ?, ?);
        """, (unternehmen_id, bestandteil_info["Name"], bestandteil_info["Herstellungsort"]))
        bestandteile_ids[bestandteil_info["Name"]] = cursor.lastrowid

# Produkte
produkte_ids = {}
for produkt_name, produkt_info in produkte.items():
    if produkt_info["Name"] not in produkte_ids:
        unternehmen_name = produkt_info["Unternehmen"]
        unternehmen_id = unternehmen_ids[unternehmen_name]
        cursor.execute("""
            INSERT INTO Produkte (
                Unternehmen_ID, Name, Barcode, Größe, Gesamtgewicht, Kategorie, 
                Herstellungsort, Brennwert, Fettgehalt, Gesättigte_Fettsäuren, 
                Kohlenhydrate, Zuckergehalt, Eiweißgehalt, Salzgehalt, Emission, Distanz
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (
            unternehmen_id, produkt_info["Name"], produkt_info["Barcode"],
            produkt_info["Größe"], produkt_info["Gesamtgewicht"], produkt_info["Kategorie"],
            produkt_info["Herstellungsort"], produkt_info["Brennwert"],
            produkt_info["Fettgehalt"], produkt_info["Gesättigte Fettsäuren"],
            produkt_info["Kohlenhydrate"], produkt_info["Zuckergehalt"],
            produkt_info["Eiweißgehalt"], produkt_info["Salzgehalt"],
            produkt_info["Emission"], produkt_info["Distanz"]
        ))
        produkte_ids[produkt_info["Name"]] = cursor.lastrowid

#Produkte_Export
for produkt_name, produkt_info in produkte.items():
    produkt_id = produkte_ids[produkt_info["Name"]]
    for distanz, typ, faktor, emission in zip(produkt_info["Exportdistanz"], produkt_info["Exporttyp"], produkt_info["Exportfaktor"], produkt_info["Exportemission"]):
        cursor.execute("""
            INSERT INTO Produkte_Export (Produkt_ID, Distanz, Typ, Faktor, Emission) VALUES (?, ?, ?, ?, ?);
        """, (produkt_id, distanz, typ, faktor, emission))

# Produkte_Allergene
for produkt_name, produkt_info in produkte.items():
    for allergen_name in produkt_info["Allergene"]:
        allergen_id = allergenen_ids[allergen_name]
        produkt_id = produkte_ids[produkt_info["Name"]]
        cursor.execute("""
            INSERT INTO Produkte_Allergene (Produkt_ID, Allergen_ID) VALUES (?, ?);
        """, (produkt_id, allergen_id))

# Produkte_Labels
for produkt_name, produkt_info in produkte.items():
    for label_name in produkt_info["Labels"]:
        label_id = labels_ids[label_name]
        produkt_id = produkte_ids[produkt_info["Name"]]
        cursor.execute("""
            INSERT INTO Produkte_Labels (Produkt_ID, Label_ID) VALUES (?, ?);
            """, (produkt_id, label_id))
        
# Produkte_Bestandteile
for produkt_name, produkt_info in produkte.items():
    for bestandteil in produkt_info["Bestandteile"]:
        bestandteil_name = bestandteil["Name"]
        try:
            bestandteil_id = bestandteile_ids[bestandteil_name]
        except:
            raise Exception(f"Produktbestandteil {bestandteil_name} scheint in der Bestandteil-Datei anders benannt zu sein")
        produkt_id = produkte_ids[produkt_info["Name"]]
        cursor.execute("""
            INSERT INTO Produkte_Bestandteile (Produkt_ID, Bestandteil_ID) VALUES (?, ?);
        """, (produkt_id, bestandteil_id))

# Produkte_Bestandteile_Transport
for produkt_name, produkt_info in produkte.items():
    for bestandteil in produkt_info["Bestandteile"]:
        bestandteil_name = bestandteil["Name"]
        try:
            bestandteil_id = bestandteile_ids[bestandteil_name]
        except:
            raise Exception(f"Produktbestandteil {bestandteil_name} scheint in der Bestandteil-Datei anders benannt zu sein")
        produkt_id = produkte_ids[produkt_info["Name"]]
        for distanz, typ, faktor, emission in zip(bestandteil["Transportdistanz"], bestandteil["Transporttyp"], bestandteil["Transportfaktor"], bestandteil["Transportemission"]):
            cursor.execute("""
                INSERT INTO Produkte_Bestandteile_Transport (Produkt_ID, Bestandteil_ID, Distanz, Typ, Faktor, Emission) VALUES (?, ?, ?, ?, ?, ?);
            """, (produkt_id, bestandteil_id, distanz, typ, faktor, emission))

# Commit the database
conn.commit()
conn.close()
