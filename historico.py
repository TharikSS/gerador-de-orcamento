import json
import os

ARQUIVO_HISTORICO = "historico.json"


def formatar_dinheiro(valor):
    return f"{valor:.2f}".replace(".", ",")


if not os.path.exists(ARQUIVO_HISTORICO):
    print("Nenhum orçamento salvo ainda.")
else:
    with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as arquivo:
        historico = json.load(arquivo)
    print(f"{len(historico)} orçamento(s) salvo(s)")
    print("_" * 40)
    for registro in historico:
        total_texto = formatar_dinheiro(registro["total_final"])
        print(f"{registro['data']} | {registro['nome']} | R$ {total_texto}")