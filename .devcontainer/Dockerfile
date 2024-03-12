FROM python:3.12.2-alpine

# Instala as dependências do sistema necessárias (exemplo)
RUN apk add --no-cache git bash

# Define o diretório de trabalho
WORKDIR /workspace

# Copia os arquivos do seu projeto para o contêiner
COPY . /workspace

# Instala as dependências do Python (se você tiver um arquivo requirements.txt)
# RUN pip install -r requirements.txt
