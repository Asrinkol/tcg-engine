import sqlite3

DB_PATH = "tcg.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cards (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         number TEXT,
         rarity TEXT NOT NULL,
         image_path TEXT,
         weight INTEGER DEFAULT 1
    )
    """)
  
    cards_data = [
        # MYTHICAL (1 Kart - %0.03 / %0.2)
        ('The One Above All', 'MYTH-001', 'mythical', 'assets/cards/myth_001.jpg', 1),

        # CHASE (6 Kart: Infinity Stones - %6.97 / %9.8)
        ('Space Stone', 'CHS-001', 'chase', 'assets/cards/chs_001.jpg', 10),
        ('Mind Stone', 'CHS-002', 'chase', 'assets/cards/chs_002.jpg', 10),
        ('Reality Stone', 'CHS-003', 'chase', 'assets/cards/chs_003.jpg', 10),
        ('Power Stone', 'CHS-004', 'chase', 'assets/cards/chs_004.jpg', 10),
        ('Time Stone', 'CHS-005', 'chase', 'assets/cards/chs_005.jpg', 10),
        ('Soul Stone', 'CHS-006', 'chase', 'assets/cards/chs_006.jpg', 10),

        # SHINY (Variant Foil - %8 / %20)
        ('Iron Man Mark 85 (Holo)', 'SHN-001', 'shiny', 'assets/cards/shn_001.jpg', 50),
        ('Captain America (Mjolnir)', 'SHN-002', 'shiny', 'assets/cards/shn_002.jpg', 50),
        ('Thor (Stormbreaker)', 'SHN-003', 'shiny', 'assets/cards/shn_003.jpg', 50),
        ('Spider-Man (Iron Spider)', 'SHN-004', 'shiny', 'assets/cards/shn_004.jpg', 50),

        # 3 STAR (Legend - %10 / %70)
        ('Iron Man', '3ST-001', '3_star', 'assets/cards/3st_001.jpg', 100),
        ('Captain America', '3ST-002', '3_star', 'assets/cards/3st_002.jpg', 100),
        ('Thor', '3ST-003', '3_star', 'assets/cards/3st_003.jpg', 100),
        ('Hulk', '3ST-004', '3_star', 'assets/cards/3st_004.jpg', 100),
        ('Black Panther', '3ST-005', '3_star', 'assets/cards/3st_005.jpg', 100),
        ('Doctor Strange', '3ST-006', '3_star', 'assets/cards/3st_006.jpg', 100),

        # 2 STAR (Elite - %20)
        ('Black Widow', '2ST-001', '2_star', 'assets/cards/2st_001.jpg', 100),
        ('Hawkeye', '2ST-002', '2_star', 'assets/cards/2st_002.jpg', 100),
        ('Loki', '2ST-003', '2_star', 'assets/cards/2st_003.jpg', 100),
        ('Vision', '2ST-004', '2_star', 'assets/cards/2st_004.jpg', 100),
        ('Scarlet Witch', '2ST-005', '2_star', 'assets/cards/2st_005.jpg', 100),
        ('Ant-Man', '2ST-006', '2_star', 'assets/cards/2st_006.jpg', 100),

        # 1 STAR (Enhanced - %27)
        ('Falcon', '1ST-001', '1_star', 'assets/cards/1st_001.jpg', 100),
        ('Winter Soldier', '1ST-002', '1_star', 'assets/cards/1st_002.jpg', 100),
        ('War Machine', '1ST-003', '1_star', 'assets/cards/1st_003.jpg', 100),
        ('Wong', '1ST-004', '1_star', 'assets/cards/1st_004.jpg', 100),
        ('Valkyrie', '1ST-005', '1_star', 'assets/cards/1st_005.jpg', 100),
        ('Okoye', '1ST-006', '1_star', 'assets/cards/1st_006.jpg', 100),

        # UNCOMMON (Operative - %28)
        ('Nick Fury', 'UNC-001', 'uncommon', 'assets/cards/unc_001.jpg', 100),
        ('Maria Hill', 'UNC-002', 'uncommon', 'assets/cards/unc_002.jpg', 100),
        ('Phil Coulson', 'UNC-003', 'uncommon', 'assets/cards/unc_003.jpg', 100),
        ('Happy Hogan', 'UNC-004', 'uncommon', 'assets/cards/unc_004.jpg', 100),
        ('Peggy Carter', 'UNC-005', 'uncommon', 'assets/cards/unc_005.jpg', 100),
        ('Heimdall', 'UNC-006', 'uncommon', 'assets/cards/unc_006.jpg', 100),

        # COMMON (Civilian - Guaranteed)
        ('SHIELD Agent', 'COM-001', 'common', 'assets/cards/com_001.jpg', 100),
        ('Hydra Agent', 'COM-002', 'common', 'assets/cards/com_002.jpg', 100),
        ('Chitauri Warrior', 'COM-003', 'common', 'assets/cards/com_003.jpg', 100),
        ('Ultron Sentry', 'COM-004', 'common', 'assets/cards/com_004.jpg', 100),
        ('Wakandan Guard', 'COM-005', 'common', 'assets/cards/com_005.jpg', 100),
        ('Nova Corps Officer', 'COM-006', 'common', 'assets/cards/com_006.jpg', 100),
        ('Sorcerer Apprentice', 'COM-007', 'common', 'assets/cards/com_007.jpg', 100),
        ('Daily Bugle Reporter', 'COM-008', 'common', 'assets/cards/com_008.jpg', 100),
    ]

    cursor.executemany('''
    INSERT INTO cards (name, number, rarity, image_path, weight)
    VALUES (?, ?, ?, ?, ?)
    ''', cards_data)

    conn.commit()
    print(f"Toplam {cursor.rowcount} kart başariyla eklendi!")
    conn.close()

if __name__ == "__main__": 
    create_tables()