### Imports ###
from fastapi import FastAPI
import sqlite3
import os
import re
import base64
from pydantic import BaseModel
from typing import List

db_pfad = os.path.join(os.path.dirname(__file__), "database.db")

class Unternehmen(BaseModel):
    Name: str
    Land: str
    Gründung: int
    Website: str

class Nährwerte(BaseModel):
    Brennwert: str
    Fettgehalt: str
    Gesättigte_Fettsäuren: str
    Kohlenhydrate: str
    Zuckergehalt: str
    Eiweißgehalt: str
    Salzgehalt: str

class Bestandteil(BaseModel):
    Name: str
    Herstellungsort: str
    Unternehmen: Unternehmen

class Produkt(BaseModel):
    Name: str
    Unternehmen: Unternehmen
    Barcode: str
    Bild: str # Base64
    Größe: str
    Kategorie: str
    Herstellungsort: str
    Nährwerte: Nährwerte
    Labels: List[str]
    Allergene: List[str]
    Bestandteile: List[Bestandteil]

# FastAPI app
app = FastAPI()

# Datenbank
conn = sqlite3.connect(db_pfad, check_same_thread=False)
cursor = conn.cursor()

### Funktionen ###

# Produkt Name -> Produkt ID
def name_to_id(name):
    cursor.execute("SELECT id FROM Produkte WHERE Name LIKE ?", (f"%{name}%",))
    result = cursor.fetchall() #ID
    if not result:
        return None
    return [i[0] for i in result]

# Produkt Barcode -> Proddukt ID
def barcode_to_id(barcode):
    cursor.execute("SELECT id FROM Produkte WHERE Barcode = ?", (barcode,))
    result = cursor.fetchone() #ID
    return result[0] if result else None

# Firmen Name -> Liste der Produkt IDs
def company_to_ids(name):
    cursor.execute("SELECT id FROM Unternehmen WHERE Name LIKE ?", (f"%{name}%",))
    results = cursor.fetchall()
    company_ids = [result[0] for result in results]
    placeholders = ", ".join("?" * len(company_ids))
    cursor.execute(f"SELECT id from Produkte WHERE Unternehmen_ID IN ({placeholders})", company_ids)
    return [i[0] for i in cursor.fetchall()]

# ProduktID -> JSON
def get_product(product_id):
    # Produkt
    # Produkt und Unternehmen essenziell
    cursor.execute("SELECT * FROM Produkte WHERE id = ?", (product_id,))
    result_product = cursor.fetchone()
    if not result_product:
        return None
    
    # Unternehmen    
    cursor.execute("SELECT * FROM Unternehmen WHERE id = ?", (result_product[1],))
    result_unternehmen = cursor.fetchone()
    if not result_unternehmen:
        return None
    unternehmen = {
        "Name": result_unternehmen[1],
        "Land": result_unternehmen[2],
        "Gründung": result_unternehmen[3],
        "Website": result_unternehmen[4]
    }
    
    # Allergene
    cursor.execute("SELECT Allergen_ID FROM Produkte_Allergene WHERE Produkt_ID = ?", (product_id,))
    result_allergene = cursor.fetchall()
    allergene = []
    for i in result_allergene:
        cursor.execute("SELECT Allergen FROM Allergene WHERE id = ?", (i[0],))
        allergene.append(cursor.fetchone()[0])
    
    # Labels
    cursor.execute("SELECT Label_ID FROM Produkte_Labels WHERE Produkt_ID = ?", (product_id,))
    result_labels = cursor.fetchall()
    labels = []
    for i in result_labels:
        cursor.execute("SELECT Label FROM Labels WHERE id = ?", (i[0],))
        labels.append(cursor.fetchone()[0])
    
    # Bestandteile
    cursor.execute("SELECT Bestandteil_ID FROM Produkte_Bestandteile WHERE Produkt_ID = ?", (product_id,))
    result_bestandteile = cursor.fetchall()
    bestandteile = []
    for i in result_bestandteile:
        cursor.execute("SELECT * FROM Bestandteile WHERE id = ?", (i[0],))
        bestandteil = cursor.fetchone()
        cursor.execute("SELECT * FROM Unternehmen WHERE id = ?", (bestandteil[1],))
        unternehmen_bestandteil = cursor.fetchone()
        _unternehmen_bestandteil = {
            "Name": unternehmen_bestandteil[1],
            "Land": unternehmen_bestandteil[2],
            "Gründung": unternehmen_bestandteil[3],
            "Website": unternehmen_bestandteil[4]
        }
        bestandteile.append({
            "Name": bestandteil[2],
            "Herstellungsort": bestandteil[3],
            "Unternehmen": _unternehmen_bestandteil
        })

    return {
        "Name": result_product[2],
        "Unternehmen": unternehmen,
        "Barcode": result_product[3],
        "Größe": result_product[4],
        "Kategorie": result_product[5],
        "Herstellungsort": result_product[6],
        "Nährwerte": {
            "Brennwert": result_product[7],
            "Fettgehalt": result_product[8],
            "Gesättigte_Fettsäuren": result_product[9],
            "Kohlenhydrate": result_product[10],
            "Zuckergehalt": result_product[11],
            "Eiweißgehalt": result_product[12],
            "Salzgehalt": result_product[13],
        },
        "Labels": labels,
        "Allergene": allergene,
        "Bestandteile": bestandteile
    }

### Endpoints
# Return Produkt JSON with Produkt ID
@app.get("/produkt/id/{id}")
def get_item(id: int):
    return get_product(id)

# Return Produkt JSON with Produkt Barcode
@app.get("/produkt/barcode/{barcode}")
def get_item(barcode: str):
    product_id = barcode_to_id(barcode)
    if not product_id:
        return None
    return get_product(product_id)

# Return Produkt JSON with Produkt Name
@app.get("/produkt/name/{name}")
def get_item(name: str):
    produkte = list(set(name_to_id(name)+(company_to_ids(name))))
    if not produkte:
        return None
    
    _produkte = []
    for produkt in produkte:
        _produkte.append(get_product(produkt))
    return _produkte

# Product JSON -> create file
@app.post("/produkt/create")
def get_item(data: Produkt):
    produkt_pfad = os.path.join(os.path.dirname(__file__), "Produkte", data.Name.strip().replace(" ", "_").lower()+".txt")
    if os.path.exists(produkt_pfad):
        {"status_code": 0, "status_message": "Produkt existiert schon"}

    # Unternehmen herstellen, falls noch nicht vorhanden
    unternehmen_pfad = os.path.join(os.path.dirname(__file__), "Unternehmen", data.Unternehmen.Name.strip().replace(" ", "_").lower()+".txt")
    if not os.path.exists(unternehmen_pfad):
        company_content = "[Unternehmen]\n[Name] {}\n[Land] {}\n[Gründung] {}\n[Website] {}".format(
            " ".join(word.capitalize() for word in data.Unternehmen.Name.strip().split()),
            " ".join(word.capitalize() for word in data.Unternehmen.Land.strip().split()),
            data.Unternehmen.Gründung,
            re.sub(r"^https?://(www\.)?", "", data.Unternehmen.Website)
        )
        with open(unternehmen_pfad, "w") as file:
            file.write(company_content)

    """# Bild hinzufügen, falls noch nicht vorhanden
    bild_pfad = os.path.join(os.path.dirname(__file__), "Medien", data.Unternehmen.Name.strip().replace(" ", "_").lower()+".jpg")
    if not os.path.exists(bild_pfad):
        if data.Bild.startswith("data:image/jpeg;base64,"):
            base64_string = base64_string.split(",")[1]
        else:
            return {"status_code": 1, "status_message": "Bitte JPEG Bild"}
        
        bild_data = base64.b64decode(base64_string)
        if bild_data[:3] == b'\xff\xd8\xff':
            with open(bild_pfad, 'wb') as file:
                file.write(bild_data)
        else:
            return {"status_code": 2, "status_message": "Invalides Bild"}
    else:
        return {"status_code": 3, "status_message": "Bild existiert schon"}"""
        
    # Bestandteile hinzufügen falls noch nicht vorhanden
    bestandteile_content = ""
    for bestandteil in data.Bestandteile:
        # Unternehmen herstellen, falls noch nicht vorhanden
        unternehmen_pfad = os.path.join(os.path.dirname(__file__), "Unternehmen", bestandteil.Unternehmen.Name.strip().replace(" ", "_").lower()+".txt")
        if not os.path.exists(unternehmen_pfad):
            company_content = "[Unternehmen]\n[Name] {}\n[Land] {}\n[Gründung] {}\n[Website] {}".format(
                " ".join(word.capitalize() for word in bestandteil.Unternehmen.Name.strip().split()),
                " ".join(word.capitalize() for word in bestandteil.Unternehmen.Land.strip().split()),
                bestandteil.Unternehmen.Gründung,
                re.sub(r"^https?://(www\.)?", "", bestandteil.Unternehmen.Website)
            )
            with open(unternehmen_pfad, "w") as file:
                file.write(company_content)

        bestandteil_pfad = os.path.join(os.path.dirname(__file__), "Bestandteile", bestandteil.Name.strip().replace(" ", "_").lower()+".txt")
        if not os.path.exists(bestandteil_pfad):
            bestandteil_content = "[Bestandteil]\n[Name] {}\n[Herstellungsort] {}\n[Unternehmen] {}".format(
                " ".join(word.capitalize() for word in bestandteil.Name.strip().split()),
                " ".join(word.capitalize() for word in bestandteil.Herstellungsort.strip().split()),
                " ".join(word.capitalize() for word in bestandteil.Unternehmen.Name.strip().split()),
            )
            bestandteile_content += "\n[Bestandteil] {}".format(" ".join(word.capitalize() for word in bestandteil.Name.strip().split()))
            with open(bestandteil_pfad, "w") as file:
                file.write(bestandteil_content)

    allergene_content = ""
    for allergen in data.Allergene:
        allergene_content += "\n[Allergen] {}".format(allergen)

    labels_content = ""
    for label in data.Labels:
        labels_content += "\n[Label] {}".format(label)

    produkt_content = "[Name] {}\n[Barcode] {}\n[Unternehmen] {}\n[Größe] {}\n[Kategorie] {}\n[Herstellungsort] {}\n\n[Nährwerte]\n[Brennwert] {}\n[Fettgehalt] {}\n[Gesättigte Fettsäuren] {}\n[Kohlenhydrate] {}\n[Zuckergehalt] {}\n[Eiweißgehalt] {}\n[Salzgehalt] {}\n\n[Bestandteile]{}\n\n[Allergene]{}\n\n[Labels]{}".format(
        " ".join(word.capitalize() for word in data.Name.strip().split()),
        data.Barcode,
        " ".join(word.capitalize() for word in data.Unternehmen.Name.strip().split()),
        data.Größe,
        " ".join(word.capitalize() for word in data.Kategorie.strip().split()),
        " ".join(word.capitalize() for word in data.Herstellungsort.strip().split()),
        data.Nährwerte.Brennwert,
        data.Nährwerte.Fettgehalt,
        data.Nährwerte.Gesättigte_Fettsäuren,
        data.Nährwerte.Kohlenhydrate,
        data.Nährwerte.Zuckergehalt,
        data.Nährwerte.Eiweißgehalt,
        data.Nährwerte.Salzgehalt,
        bestandteile_content,
        allergene_content,
        labels_content,
    )

    with open(produkt_pfad, "w") as file:
        file.write(produkt_content)

    return {"status_code": 4, "status_message": "Produkt erfolgreich erstellt"}

@app.on_event("shutdown")
def shutdown():
    global conn, cursor
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("Database closed")