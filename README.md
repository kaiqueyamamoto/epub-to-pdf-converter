# EPUB to PDF Converter

## Descrição

Este projeto fornece uma ferramenta para converter arquivos no formato EPUB para PDF. Foi desenvolvido usando Python e utiliza bibliotecas como `ebooklib` para leitura de arquivos EPUB, `reportlab` para criação de arquivos PDF, e `lxml` para processamento de HTML contido nos arquivos EPUB.

## Pré-requisitos

Antes de iniciar, certifique-se de que você tenha Python instalado em sua máquina. Este projeto foi testado com Python 3.8+. Você também precisará instalar as dependências necessárias listadas abaixo.

## Dependências

- ebooklib
- reportlab
- lxml

Você pode instalar todas as dependências necessárias executando o seguinte comando:

```bash
pip install ebooklib reportlab lxml
```

```bash
projeto/
│   main.py          - Script principal para conversão de EPUB para PDF.
│   README.md        - Este arquivo.
├── input/           - Pasta onde os arquivos EPUB devem ser colocados para conversão.
└── output/          - Pasta onde os arquivos PDF convertidos serão salvos.
```
