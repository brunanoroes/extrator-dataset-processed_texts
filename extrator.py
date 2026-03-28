import pickle
import pandas as pd

# carregar arquivos
with open("processed_texts_telegram.p", "rb") as f:
    telegram = pickle.load(f)

with open("processed_texts_whatsapp.p", "rb") as f:
    whatsapp = pickle.load(f)

# juntar tudo
dados = telegram + whatsapp

# criar DataFrame
df = pd.DataFrame(dados, columns=["mensagem"])

# (opcional) criar coluna de origem
origem = ["telegram"] * len(telegram) + ["whatsapp"] * len(whatsapp)
df["origem"] = origem

# (opcional) limpar texto
df["mensagem"] = df["mensagem"].apply(lambda x: " ".join(x.split()))

# salvar no Excel
df.to_excel("fraudes_completo.xlsx", index=False)

print("Arquivo gerado com sucesso!")