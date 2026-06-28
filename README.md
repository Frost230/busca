# Painel de Busca - API Brasil Pro

Painel de busca terminal cross-platform que integra com diversas APIs brasileiras.

## Funcionalidades

- Busca por CPF
- Busca por Nome
- Busca por Nome da Mae
- Busca por Nome do Pai
- Busca por Titulo
- Busca por RG
- Busca por CEP (v1 e v2 com geolocalizacao)
- Busca por CNPJ
- Lista de Bancos
- Busca Banco por Codigo
- Moedas disponiveis para Cambio
- Cotacao de Cambio
- Busca por DDD
- Feriados Nacionais

## Como usar

1. Instale as dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute o painel:
   ```bash
   python painel_busca.py
   ```

## Como enviar para o GitHub

Para enviar os arquivos para o repositorio https://github.com/Frost230/busca:

```bash
# Inicialize o repositorio git
git init

# Adicione os arquivos
git add .

# Crie um commit
git commit -m "Adiciona painel de busca"

# Adicione o repositorio remoto
git remote add origin https://github.com/Frost230/busca.git

# Envie para o GitHub
git branch -M main
git push -u origin main
```

Power by Frost // Society
