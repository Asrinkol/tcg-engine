import datetime
from engine.pack_generator import generate_pack
from pdf.pdf_generator import generate_a3_pdf

def main():
    pack1, p_type1 = generate_pack()
    pack2, p_type2 = generate_pack()
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_name = f"output/marvel_packs_{timestamp}.pdf"
    
    generate_a3_pdf(pack1, pack2, output_filename=output_name)

if __name__ == "__main__":
    main()