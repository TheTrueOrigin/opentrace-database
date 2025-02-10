### Build.py

### Imports ###
import sqlite3
import os

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
                    raise Exception(f"Unternehmensname {name} stimmt nicht mit Dateiname '{unternehmen_name}.txt' überein")
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
                bestandteile[bestandteil_name]["Name"] = line[6:].strip()
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
                produkte[produkt_name]["Name"] = name
            elif line.startswith("[Barcode]"):
                produkte[produkt_name]["Barcode"] = line[9:].strip()
            elif line.startswith("[Unternehmen]"):
                produkte[produkt_name]["Unternehmen"] = line[13:].strip()
            elif line.startswith("[Größe]"):
                produkte[produkt_name]["Größe"] = line[7:].strip()
            elif line.startswith("[Kategorie]"):
                produkte[produkt_name]["Kategorie"] = line[11:].strip()
            elif line.startswith("[Herstellungsort]"):
                produkte[produkt_name]["Herstellungsort"] = line[17:].strip()

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
                produkte[produkt_name]["Bestandteile"].append(line[13:].strip())

            elif line.startswith("[Allergene]"):
                produkte[produkt_name]["Allergene"] = []
            elif line.startswith("[Allergen]"):
                produkte[produkt_name]["Allergene"].append(line[10:].strip())

            elif line.startswith("[Labels]"):
                produkte[produkt_name]["Labels"] = []
            elif line.startswith("[Label]"):
                produkte[produkt_name]["Labels"].append(line[7:].strip())

### Datenbank erstellen ###
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
        Kategorie TEXT, 
        Herstellungsort TEXT, 
        Brennwert TEXT, 
        Fettgehalt TEXT, 
        Gesättigte_Fettsäuren TEXT,
        Kohlenhydrate TEXT, 
        Zuckergehalt TEXT, 
        Eiweißgehalt TEXT, 
        Salzgehalt TEXT,
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
        PRIMARY KEY (Produkt_ID, Bestandteil_ID),
        FOREIGN KEY (Produkt_ID) REFERENCES Produkte(id) ON DELETE CASCADE,
        FOREIGN KEY (Bestandteil_ID) REFERENCES Bestandteile(id) ON DELETE CASCADE
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
allergenen_ids = {}
labels_ids = {}

for produkt_name, produkt_info in produkte.items():
    for allergen_name in produkt_info["Allergene"]:
        if allergen_name not in allergenen_ids:
            cursor.execute("""
                INSERT INTO Allergene (Allergen) VALUES ('{}');
            """.format(allergen_name))
            allergenen_ids[allergen_name] = cursor.lastrowid
    
    for label_name in produkt_info["Labels"]:
        label_name = "_".join(word.capitalize() for word in label_name.strip().split())
        if label_name not in labels_ids:
            cursor.execute("""
                INSERT INTO Labels (Label) VALUES ('{}');
            """.format(label_name))
            labels_ids[label_name] = cursor.lastrowid

# Bestandteile
bestandteile_ids = {}
for bestandteil_name, bestandteil_info in bestandteile.items():
    if bestandteil_info["Name"] not in bestandteile_ids:
        unternehmen_name = bestandteil_info["Unternehmen"]
        unternehmen_id = unternehmen_ids[unternehmen_name]
        cursor.execute("""
            INSERT INTO Bestandteile (Unternehmen_ID, Name, Herstellungsort) VALUES ({}, '{}', '{}');
        """.format(unternehmen_id, bestandteil_info["Name"], bestandteil_info["Herstellungsort"]))
        bestandteile_ids[bestandteil_info["Name"]] = cursor.lastrowid

# Produkte
produkte_ids = {}
for produkt_name, produkt_info in produkte.items():
    if produkt_info["Name"] not in produkte_ids:
        unternehmen_name = produkt_info["Unternehmen"]
        unternehmen_id = unternehmen_ids[unternehmen_name]
        cursor.execute("""
            INSERT INTO Produkte (
                Unternehmen_ID, Name, Barcode, Größe, Kategorie, 
                Herstellungsort, Brennwert, Fettgehalt, Gesättigte_Fettsäuren, 
                Kohlenhydrate, Zuckergehalt, Eiweißgehalt, Salzgehalt
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (
            unternehmen_id, produkt_info["Name"], produkt_info["Barcode"],
            produkt_info["Größe"], produkt_info["Kategorie"],
            produkt_info["Herstellungsort"], produkt_info["Brennwert"],
            produkt_info["Fettgehalt"], produkt_info["Gesättigte Fettsäuren"],
            produkt_info["Kohlenhydrate"], produkt_info["Zuckergehalt"],
            produkt_info["Eiweißgehalt"], produkt_info["Salzgehalt"]
        ))
        produkte_ids[produkt_info["Name"]] = cursor.lastrowid

# Produkte_Allergene
for produkt_name, produkt_info in produkte.items():
    for allergen_name in produkt_info["Allergene"]:
        allergen_id = allergenen_ids[allergen_name]
        produkt_id = produkte_ids[produkt_info["Name"]]
        cursor.execute("""
            INSERT INTO Produkte_Allergene (Produkt_ID, Allergen_ID) VALUES ({}, {});
        """.format(produkt_id, allergen_id))

# Produkte_Labels
for produkt_name, produkt_info in produkte.items():
    for label_name in produkt_info["Labels"]:
        label_id = labels_ids[label_name]
        produkt_id = produkte_ids[produkt_info["Name"]]
        cursor.execute("""
            INSERT INTO Produkte_Labels (Produkt_ID, Label_ID) VALUES ({}, {});
            """.format(produkt_id, label_id))
        
# Produkte_Bestandteile
for produkt_name, produkt_info in produkte.items():
    for bestandteil_name in produkt_info["Bestandteile"]:
        bestandteil_id = bestandteile_ids[bestandteil_name]
        produkt_id = produkte_ids[produkt_info["Name"]]
        cursor.execute("""
            INSERT INTO Produkte_Bestandteile (Produkt_ID, Bestandteil_ID) VALUES ({}, {});
        """.format(produkt_id, bestandteil_id))
