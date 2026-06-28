#!/usr/bin/env python3
import requests
import json
import sys
import os
from typing import Optional, Dict, Any

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print("""
             
        ⣴⣿⣿⣿⣷⣄
     ⢀⣼⣿⣿⣿⣿⣿⣿⣇
    ⢠⣿⡿⠙⠁⠀⣿⡿⠛⣿⣧
   ⢰⡟⠁⠀⠀⢀⣼⣿⡇⠀⠸⣿⡆
   ⢨⣷⣦⣤⢶⣫⣾⣿⡇⠀⠀⠹⣷
    ⠀⠙⣿⣾⣋⣁⠀⢻⣿⣤⣀⣀⣽⡇
     ⠀⣿⣿⠿⠿⣿⣿⣿⣝⡿⠿⠟⠁
     ⠀⡟⠀⠀⠀⠀⢻⣿⣿⡟⠁⠀
     ⠀⡇⠀⠀⠀⠀⣼⣿⡿⠀⠀
     ⠀⡇⠀⠀⠀⣰⠟⠋⠀⠀
     ⠀⡇⠀⠀⢰⠃⠀⠀⠀
     ⠀⢸⠀⠀⢠⠃⠀⠀⠀
     ⠀⠨⣀⡠⠁⠀⠀⠀
             
    """)
    print("=" * 60)
    print("          PAINEL DE BUSCA - API BRASIL PRO              ")
    print("=" * 60)
    print()

def print_footer():
    print()
    print("=" * 60)
    print("          Power by Frost // Society")
    print("=" * 60)
    print()

def buscar_cpf(cpf: str) -> Optional[Dict[str, Any]]:
    url = f"http://apisbrasilpro.site/api/busca_cpf.php?cpf={cpf}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erro: {e}")
        return None

def buscar_nome(nome: str) -> Optional[Dict[str, Any]]:
    url = f"http://apisbrasilpro.site/api/busca_nome.php?nome={nome}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erro: {e}")
        return None

def buscar_mae(mae: str) -> Optional[Dict[str, Any]]:
    url = f"http://apisbrasilpro.site/api/busca_mae.php?mae={mae}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erro: {e}")
        return None

def buscar_pai(pai: str) -> Optional[Dict[str, Any]]:
    url = f"http://apisbrasilpro.site/api/busca_pai.php?pai={pai}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erro: {e}")
        return None

def buscar_titulo(titulo: str) -> Optional[Dict[str, Any]]:
    url = f"http://apisbrasilpro.site/api/busca_titulo.php?titulo={titulo}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erro: {e}")
        return None

def buscar_rg(rg: str) -> Optional[Dict[str, Any]]:
    url = f"http://apisbrasilpro.site/api/busca_rg.php?rg={rg}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erro: {e}")
        return None

def buscar_cep_v1(cep: str) -> Optional[Dict[str, Any]]:
    url = f"https://brasilapi.com.br/api/cep/v1/{cep}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erro: {e}")
        return None

def buscar_cep_v2(cep: str) -> Optional[Dict[str, Any]]:
    url = f"https://brasilapi.com.br/api/cep/v2/{cep}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erro: {e}")
        return None

def buscar_cnpj(cnpj: str) -> Optional[Dict[str, Any]]:
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erro: {e}")
        return None

def buscar_bancos() -> Optional[Dict[str, Any]]:
    url = "https://brasilapi.com.br/api/banks/v1"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erro: {e}")
        return None

def buscar_banco_por_codigo(codigo: str) -> Optional[Dict[str, Any]]:
    url = f"https://brasilapi.com.br/api/banks/v1/{codigo}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erro: {e}")
        return None

def buscar_moedas_cambio() -> Optional[Dict[str, Any]]:
    url = "https://brasilapi.com.br/api/cambio/v1/moedas"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erro: {e}")
        return None

def buscar_cotacao_cambio(moeda: str, data: str) -> Optional[Dict[str, Any]]:
    url = f"https://brasilapi.com.br/api/cambio/v1/cotacao/{moeda}/{data}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erro: {e}")
        return None

def buscar_ddd(ddd: str) -> Optional[Dict[str, Any]]:
    url = f"https://brasilapi.com.br/api/ddd/v1/{ddd}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erro: {e}")
        return None

def buscar_feriados(ano: str) -> Optional[Dict[str, Any]]:
    url = f"https://brasilapi.com.br/api/feriados/v1/{ano}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erro: {e}")
        return None

def exibir_resultado(resultado: Any):
    print()
    print("-" * 60)
    print("Resultado:")
    print("-" * 60)
    print(json.dumps(resultado, indent=4, ensure_ascii=False))
    print("-" * 60)
    print_footer()
    print()

def menu_principal():
    while True:
        clear_screen()
        print_banner()
        print("MENU PRINCIPAL")
        print("1. Busca por CPF")
        print("2. Busca por Nome")
        print("3. Busca por Nome da Mae")
        print("4. Busca por Nome do Pai")
        print("5. Busca por Titulo")
        print("6. Busca por RG")
        print("7. Busca por CEP (v1)")
        print("8. Busca por CEP (v2 - Geolocalizacao)")
        print("9. Busca por CNPJ")
        print("10. Lista de Bancos")
        print("11. Busca Banco por Codigo")
        print("12. Moedas disponiveis para Cambio")
        print("13. Cotacao de Cambio")
        print("14. Busca por DDD")
        print("15. Feriados Nacionais")
        print("0. Sair")
        print()

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "0":
            print("Saindo...")
            sys.exit(0)
        elif opcao == "1":
            cpf = input("Digite o CPF: ").strip()
            resultado = buscar_cpf(cpf)
            if resultado:
                exibir_resultado(resultado)
        elif opcao == "2":
            nome = input("Digite o Nome: ").strip()
            resultado = buscar_nome(nome)
            if resultado:
                exibir_resultado(resultado)
        elif opcao == "3":
            mae = input("Digite o Nome da Mae: ").strip()
            resultado = buscar_mae(mae)
            if resultado:
                exibir_resultado(resultado)
        elif opcao == "4":
            pai = input("Digite o Nome do Pai: ").strip()
            resultado = buscar_pai(pai)
            if resultado:
                exibir_resultado(resultado)
        elif opcao == "5":
            titulo = input("Digite o Titulo: ").strip()
            resultado = buscar_titulo(titulo)
            if resultado:
                exibir_resultado(resultado)
        elif opcao == "6":
            rg = input("Digite o RG: ").strip()
            resultado = buscar_rg(rg)
            if resultado:
                exibir_resultado(resultado)
        elif opcao == "7":
            cep = input("Digite o CEP: ").strip()
            resultado = buscar_cep_v1(cep)
            if resultado:
                exibir_resultado(resultado)
        elif opcao == "8":
            cep = input("Digite o CEP: ").strip()
            resultado = buscar_cep_v2(cep)
            if resultado:
                exibir_resultado(resultado)
        elif opcao == "9":
            cnpj = input("Digite o CNPJ: ").strip()
            resultado = buscar_cnpj(cnpj)
            if resultado:
                exibir_resultado(resultado)
        elif opcao == "10":
            resultado = buscar_bancos()
            if resultado:
                exibir_resultado(resultado)
        elif opcao == "11":
            codigo = input("Digite o Codigo do Banco: ").strip()
            resultado = buscar_banco_por_codigo(codigo)
            if resultado:
                exibir_resultado(resultado)
        elif opcao == "12":
            resultado = buscar_moedas_cambio()
            if resultado:
                exibir_resultado(resultado)
        elif opcao == "13":
            moeda = input("Digite a Moeda (ex: USD): ").strip().upper()
            data = input("Digite a Data (YYYY-MM-DD): ").strip()
            resultado = buscar_cotacao_cambio(moeda, data)
            if resultado:
                exibir_resultado(resultado)
        elif opcao == "14":
            ddd = input("Digite o DDD: ").strip()
            resultado = buscar_ddd(ddd)
            if resultado:
                exibir_resultado(resultado)
        elif opcao == "15":
            ano = input("Digite o Ano: ").strip()
            resultado = buscar_feriados(ano)
            if resultado:
                exibir_resultado(resultado)
        else:
            print("Opcao invalida!")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
