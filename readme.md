# 📊 Análise de Mensagens de Fraude em WhatsApp e Telegram

## 📌 Descrição

Este projeto tem como objetivo a **análise de mensagens com potencial de fraude** coletadas de grupos públicos do WhatsApp e Telegram. Os dados foram obtidos a partir de datasets previamente processados, contendo mensagens filtradas por palavras-chave relacionadas a golpes financeiros.

O foco do projeto é:

* Consolidar os dados
* Preparar para análise
* Possibilitar uso em estudos de detecção de fraudes

---

## 📂 Estrutura do Projeto

```
.
├── processed_texts_telegram.p
├── processed_texts_whatsapp.p
├── gerar_excel.py
├── fraudes_completo.xlsx
└── README.md
```

---

## 📥 Dataset

Os dados utilizados são provenientes de arquivos no formato `.p` (pickle), contendo listas de mensagens de texto.

* `processed_texts_telegram.p`: mensagens coletadas do Telegram
* `processed_texts_whatsapp.p`: mensagens coletadas do WhatsApp

Essas mensagens foram previamente filtradas com base em palavras-chave relacionadas a fraudes, como:

* empréstimo
* investimento
* dinheiro
* conta suspensa

⚠️ Importante:

> As mensagens possuem **alta probabilidade de serem fraudes**, mas não são 100% rotuladas.

---

## ⚙️ Como Executar

### 1. Instalar dependências

```bash
pip install pandas openpyxl
```

---

### 2. Executar o script

```bash
python gerar_excel.py
```

---

### 3. Resultado

Será gerado o arquivo:

```
fraudes_completo.xlsx
```

Com a seguinte estrutura:

| mensagem          | origem   |
| ----------------- | -------- |
| texto da mensagem | telegram |
| texto da mensagem | whatsapp |

---

## 🧪 Funcionalidades

* Leitura de arquivos `.p` (pickle)
* Consolidação de datasets
* Limpeza básica de texto
* Exportação para Excel
* Identificação da origem da mensagem

---

## 💡 Possíveis Extensões

Este projeto pode ser expandido para:

* Classificação automática de fraudes (Machine Learning)
* Identificação de categorias de golpes:

  * empréstimo fraudulento
  * phishing
  * documentos falsos
* Análise comparativa entre plataformas
* Detecção de padrões linguísticos

---

## 📊 Aplicações

* Pesquisa acadêmica (TCC)
* Segurança da informação
* Detecção de spam/golpes
* Processamento de linguagem natural (NLP)

---

## ⚠️ Observações

* Os dados não possuem rótulos explícitos (fraude vs não fraude)
* Recomenda-se validação manual para tarefas supervisionadas
* O dataset é enviesado para mensagens suspeitas

---

## 👩‍💻 Autora

Projeto desenvolvido para fins acadêmicos.

---

## 📄 Licença

Este projeto é destinado exclusivamente para fins educacionais e de pesquisa.
