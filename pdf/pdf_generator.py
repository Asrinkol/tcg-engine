import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, landscape
from reportlab.lib.units import mm
from reportlab.lib import colors

CARD_WIDTH = 63 * mm
CARD_HEIGHT = 88 * mm

def draw_pack(c, pack, start_x, start_y):
    for i, card in enumerate(pack):
        row = i // 3  
        col = i % 3   
        
        x = start_x + (col * CARD_WIDTH)
        y = start_y + ((2 - row) * CARD_HEIGHT)
        
        image_path = card['image_path']
        
        if os.path.exists(image_path):
            c.drawImage(image_path, x, y, width=CARD_WIDTH, height=CARD_HEIGHT, preserveAspectRatio=True)
        else:
            c.setStrokeColor(colors.black)
            c.setFillColor(colors.lightgrey)
            c.rect(x, y, CARD_WIDTH, CARD_HEIGHT, fill=1)
            
            c.setFillColor(colors.black)
            c.setFont("Helvetica-Bold", 10)
            c.drawString(x + 5*mm, y + 45*mm, card['name'][:15])
            
            c.setFont("Helvetica", 8)
            c.drawString(x + 5*mm, y + 35*mm, f"Rarity: {card['rarity']}")
            c.drawString(x + 5*mm, y + 25*mm, f"No: {card['number']}")

def draw_card_backs(c, start_x, start_y, back_image_path="assets/cards/card_back.jpg"):
    for i in range(9):
        row = i // 3
        col = i % 3
        
        x = start_x + (col * CARD_WIDTH)
        y = start_y + ((2 - row) * CARD_HEIGHT)
        
        if os.path.exists(back_image_path):
            c.drawImage(back_image_path, x, y, width=CARD_WIDTH, height=CARD_HEIGHT, preserveAspectRatio=True)
        else:
            c.setStrokeColor(colors.black)
            c.setFillColor(colors.darkblue)
            c.rect(x, y, CARD_WIDTH, CARD_HEIGHT, fill=1)

            c.setFillColor(colors.white)
            c.setFont("Helvetica-Bold", 14)
            c.drawCentredString(x + (CARD_WIDTH/2), y + (CARD_HEIGHT/2) + 5, "MARVEL")
            c.setFont("Helvetica", 10)
            c.drawCentredString(x + (CARD_WIDTH/2), y + (CARD_HEIGHT/2) - 10, "TCG")

def generate_a3_pdf(pack1, pack2, output_filename="output/marvel_packs.pdf"):
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    
    page_width, page_height = landscape(A3)
    c = canvas.Canvas(output_filename, pagesize=landscape(A3))
    
    grid_width = 3 * CARD_WIDTH
    grid_height = 3 * CARD_HEIGHT
    
    margin_y = (page_height - grid_height) / 2
    margin_x_left = 5 * mm
    margin_x_right = page_width - 5 * mm - grid_width
    
    draw_pack(c, pack1, margin_x_left, margin_y)
    draw_pack(c, pack2, margin_x_right, margin_y)
    
    c.showPage()
    
    draw_card_backs(c, margin_x_left, margin_y)
    draw_card_backs(c, margin_x_right, margin_y)
    
    c.save()
    print(f"📄 PDF başarıyla oluşturuldu: {output_filename}")