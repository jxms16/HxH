from app.db.client import get_hunters_collection


def seed_hunters(force=False):
    collection = get_hunters_collection()
    if not force and collection.count_documents({}) > 0:
        return

    hunters = [
        {
            "nombre": "Gon Freecss",
            "edad": 12,
            "nen_tipo": "Refuerzo",
            "afiliacion": "Cazador",
            "imagen_url": "https://i.pinimg.com/736x/4a/cc/52/4acc524c922b75bce857318e061dc50d.jpg",
        },
        {
            "nombre": "Killua Zoldyck",
            "edad": 12,
            "nen_tipo": "Transmutación",
            "afiliacion": "Familia Zoldyck",
            "imagen_url": "https://i.pinimg.com/1200x/68/e2/31/68e23146e50bd80ac8d1a7340c668b8e.jpg",
        },
        {
            "nombre": "Kurapika",
            "edad": 17,
            "nen_tipo": "Especialización",
            "afiliacion": "Clan Kurta",
            "imagen_url": "https://i.pinimg.com/736x/c6/93/85/c6938572cd854de5ea3d9532696b2fa2.jpg",
        },
        {
            "nombre": "Leorio Paradinight",
            "edad": 19,
            "nen_tipo": "Emisión",
            "afiliacion": "Asociación de Cazadores",
            "imagen_url": "https://i.pinimg.com/736x/1c/ea/5b/1cea5b7bc91cc30beeeb687b4b6d8286.jpg",
        },
        {
            "nombre": "Hisoka Morow",
            "edad": 28,
            "nen_tipo": "Transmutación",
            "afiliacion": "Cazador Independiente",
            "imagen_url": "https://i.pinimg.com/736x/5d/29/bd/5d29bd072c5678b6d12d6730b087f46a.jpg",
        },
        {
            "nombre": "Chrollo Lucilfer",
            "edad": 26,
            "nen_tipo": "Especialización",
            "afiliacion": "Genei Ryodan",
            "imagen_url": "https://i.pinimg.com/736x/f5/84/21/f58421608777be56529e313751b87fe4.jpg",
        },
        {
            "nombre": "Biscuit Krueger",
            "edad": 57,
            "nen_tipo": "Transmutación",
            "afiliacion": "Cazadora",
            "imagen_url": "https://i.pinimg.com/736x/62/2b/eb/622bebbe00c5a326159731a6aadf3e14.jpg",
        },
        {
            "nombre": "Isaac Netero",
            "edad": 110,
            "nen_tipo": "Refuerzo",
            "afiliacion": "Asociación de Cazadores",
            "imagen_url": "https://i.pinimg.com/736x/f5/0e/69/f50e69efd6002626720f32e6fe5ba246.jpg",
        },
        {
            "nombre": "Meruem",
            "edad": 0,
            "nen_tipo": "Especialización",
            "afiliacion": "Hormigas Quimera",
            "imagen_url": "https://i.pinimg.com/1200x/2c/89/df/2c89df0cb125e1d4985d824db8d4331d.jpg",
        },
        {
            "nombre": "Neferpitou",
            "edad": 1,
            "nen_tipo": "Especialización",
            "afiliacion": "Guardia Real",
            "imagen_url": "https://i.pinimg.com/736x/c2/75/70/c27570632179e1ada980f052db36a4d6.jpg",
        },
        {
            "nombre": "Morel Mackernasey",
            "edad": 45,
            "nen_tipo": "Materialización",
            "afiliacion": "Cazador",
            "imagen_url": "https://i.pinimg.com/1200x/08/6b/18/086b18528fee9234ed42fee757f63174.jpg",
        },
        {
            "nombre": "Knuckle Bine",
            "edad": 28,
            "nen_tipo": "Emisión",
            "afiliacion": "Cazador",
            "imagen_url": "https://i.pinimg.com/736x/fe/b5/26/feb526c2ce84e7bb9be461c2ec469bf4.jpg",
        },
    ]

    if force:
        collection.delete_many({})
        print("🗑️ Cazadores anteriores eliminados")
    
    collection.insert_many(hunters)
    print("✅ Hunters iniciales insertados")

