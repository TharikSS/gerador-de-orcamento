# Gerador de Orçamento em PDF

Programa em Python que gera orçamentos em PDF para prestadores de serviço.

## O que faz

- Pede nome e telefone do cliente
- Cadastra vários itens, com quantidade fracionada (ex.: 2,5 metros)
- Valida o que foi digitado e pede de novo em caso de erro
- Calcula subtotal, desconto em porcentagem e total
- Gera um PDF com data e hora no nome, sem sobrescrever os anteriores

## Como usar

1. Crie e ative o ambiente virtual:

```
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Instale as dependências:

```
pip install -r requirements.txt
```

3. Rode o programa:

```
python main.py
```

## Tecnologias

Python e a biblioteca reportlab.

## Autor

Tharik