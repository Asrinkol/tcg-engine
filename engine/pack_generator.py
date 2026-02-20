import sqlite3
import random

PACK_TYPE_RATES = {
    "regular": 0.006,
    "god": 99.004
}

FREE_RATES = {
    "uncommon": 28.0, 
    "1_star": 27.0, 
    "2_star": 20.0, 
    "3_star": 10.0, 
    "shiny": 8.0, 
    "chase": 6.97, 
    "mythical": 0.03
}

HERO_RATES = {
    "3_star": 70.0, 
    "shiny": 20.0, 
    "chase": 9.8, 
    "mythical": 0.2
}


GOD_RATES = {
    "3_star": 30.0, 
    "shiny": 30.0, 
    "chase": 30.0, 
    "mythical": 10.0
}


def get_all_cards():
    conn = sqlite3.connect('database/tcg.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cards")
    cards = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return cards


def roll_rarity(rates):
    rarities = list(rates.keys())
    weights = list(rates.values())
    return random.choices(rarities, weights=weights, k=1)[0]


def generate_pack():

    all_cards = get_all_cards()
    pack = []
    drawn_ids = set()

    pack_type = roll_rarity(PACK_TYPE_RATES)
    
   
    if pack_type == "god":
        pack_structure = ["god"] * 9
    else:
        pack_structure = [
            "common", "common", "common",   
            "uncommon", "uncommon",         
            "free", "free", "free",         
            "hero"                          
        ]

    for slot in pack_structure:
        target_rarity = slot
        
        if slot == "free":
            target_rarity = roll_rarity(FREE_RATES)
        elif slot == "hero":
            target_rarity = roll_rarity(HERO_RATES)
        elif slot == "god":
            target_rarity = roll_rarity(GOD_RATES)
            
        eligible_cards = [c for c in all_cards if c['rarity'] == target_rarity and c['id'] not in drawn_ids]
        
        if not eligible_cards:
            if pack_type == "god" or slot in ["hero", "free"]:
                eligible_cards = [c for c in all_cards if c['rarity'] == '3_star' and c['id'] not in drawn_ids]
            else:
                eligible_cards = [c for c in all_cards if c['rarity'] == 'common' and c['id'] not in drawn_ids]
                
        card_weights = [c['weight'] for c in eligible_cards]
        selected_card = random.choices(eligible_cards, weights=card_weights, k=1)[0]
        
        pack.append(selected_card)
        drawn_ids.add(selected_card['id'])

    return pack, pack_type

if __name__ == "__main__":
   
    my_pack, p_type = generate_pack()
    
    print("="*50)
    if p_type == "god":
        print("🌟👑 AMAN TANRIM! GOD PACK BULUNDU! 👑🌟")
    else:
        print("📦 YENİ MARVEL PAKETİ AÇILDI! (Regular) 📦")
    print("="*50)
    
    for i, card in enumerate(my_pack):
        print(f"Slot {i+1}: [{card['rarity'].upper():<10}] - {card['name']}")
    print("="*50)