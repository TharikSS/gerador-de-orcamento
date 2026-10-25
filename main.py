from datetime import datetime

from reportlab.pdfgen import canvas

EMPRESA = "O.P.S"

def calcular_total(itens):
    total = 0
    for item in itens:
        total += item["quantidade"] * item["valor"]
    return total


def mostrar_resumo(nome, telefone, itens, total, desconto, valor_desconto):
   print()
   print(f"Orçamento para: {nome} - {telefone}")
   print("_" *40)
   for item in itens:
       subtotal = item["quantidade"] * item["valor"]
       subtotal_texto = f"{subtotal:.2f}".replace(".", ",")
       quantidade_texto = f"{item['quantidade']:g}".replace(".", ",")
       print(f"{quantidade_texto} x {item['descricao']} ... R$ {subtotal_texto}")
   print("_" *40)
   subtotal_texto = f"{total:.2f}".replace(".", ",")
   desconto_texto = f"{valor_desconto:.2f}".replace(".", ",")
   final_texto = f"{total - valor_desconto:.2f}".replace(".", ",")
   print(f"Subtotal: R$ {subtotal_texto}")
   print(f"Desconto ({desconto:g}%): R$ {desconto_texto}")
   print(f"Total: R$ {final_texto}")
                                                
   
def gerar_pdf(nome, telefone, itens, total, desconto, valor_desconto, arquivo):
    pdf = canvas.Canvas(arquivo)
    y = 800
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(50, y, EMPRESA)
    y = y - 25
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y, f"Orçamento para: {nome} - {telefone}")
    y = y - 30
    for item in itens:
        subtotal = item["quantidade"] * item["valor"]
        subtotal_texto = f"{subtotal:.2f}".replace(".", ",")
        quantidade_texto = f"{item['quantidade']:g}".replace(".", ",")
        pdf.drawString(50, y, f"{quantidade_texto} x {item['descricao']} ... R$ {subtotal_texto}")
        y = y - 20  
    pdf.line(50, y - 15, 545, y - 15)   
    subtotal_texto = f"{total:.2f}".replace(".", ",")
    desconto_texto = f"{valor_desconto:.2f}".replace(".", ",")
    final_texto = f"{total - valor_desconto:.2f}".replace(".", ",")
    pdf.drawString(50, y - 50, f"Subtotal: R$ {subtotal_texto}")
    pdf.drawString(50, y - 70, f"Desconto ({desconto:g}%): R$ {desconto_texto}")
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y  - 90, f"Total: R$ {final_texto}")
    pdf.save()

def pedir_numero(pergunta):
    while True: 
        texto = input(pergunta)
        try:
            return float(texto.replace(",", "."))
        except ValueError:
            print("Valor invalido. Use apenas números, como 2,5")


nome = input("nome do cliente: ").title()
telefone = input("telefone: ")

itens = []

while True:
    descricao = input("Descrição do item (ou 'fim'): ")
    if descricao == "fim":
        break
    quantidade = pedir_numero("Quantidade: ")
    valor = pedir_numero("Valor unitário: ")
    item = {"descricao": descricao, "quantidade": quantidade, "valor": valor}
    itens.append(item)

desconto = pedir_numero("Desconto em % (0 se não houver): ")

total = calcular_total(itens)   
valor_desconto = total * (desconto / 100)
mostrar_resumo(nome, telefone, itens, total, desconto, valor_desconto)

agora = datetime.now()
nome_arquivo = f"orcamento_{agora.strftime('%d-%m-%Y_%H-%M-%S')}.pdf"
gerar_pdf(nome, telefone, itens, total, desconto, valor_desconto, nome_arquivo)
print(f"PDF salvo como: {nome_arquivo}")
