import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo CSV
df = pd.read_csv("dados.csv")

# Mostra as 5 primeiras linhas
print("Prévia dos dados:")
print(df.head())

# --- Estatísticas básicas ---
media_renda = df.groupby("lia_na_infancia")["renda_mensal"].mean()
media_livros = df.groupby("lia_na_infancia")["livros_por_mes"].mean()

print("\nMédia de renda por hábito de leitura na infância:")
print(media_renda)

print("\nMédia de livros lidos por mês na vida adulta:")
print(media_livros)

# Paleta de cores consistente
cores_renda = ["#4CAF50", "#F44336"]  # verde e vermelho
cores_livros = ["#2196F3", "#FF9800"]  # azul e laranja
cor_educacao = "#9C27B0"  # roxo
colormap_empilhado = "tab20c"  # para o gráfico empilhado

# --- Gráfico 1: renda média x leitura na infância ---
plt.figure(figsize=(7,5))
media_renda.plot(kind="bar", color=cores_renda)
plt.title("Renda média por hábito de leitura na infância", fontsize=14, fontweight="bold")
plt.ylabel("Renda mensal (R$)", fontsize=12)
plt.xlabel("Lia na infância", fontsize=12)
plt.xticks(rotation=0, fontsize=10)
plt.yticks(fontsize=10)

# Valores sobre as barras
for i, v in enumerate(media_renda):
    plt.text(i, v + 100, f"R${v:.2f}", ha='center', fontweight='bold', fontsize=10)

plt.tight_layout()
plt.savefig("grafico_renda.png", dpi=300)
plt.show()

# --- Gráfico 2: livros por mês x leitura na infância ---
plt.figure(figsize=(7,5))
media_livros.plot(kind="bar", color=cores_livros)
plt.title("Livros lidos por mês por hábito de leitura na infância", fontsize=14, fontweight="bold")
plt.ylabel("Média de livros por mês", fontsize=12)
plt.xlabel("Lia na infância", fontsize=12)
plt.xticks(rotation=0, fontsize=10)
plt.yticks(fontsize=10)

# Valores sobre as barras
for i, v in enumerate(media_livros):
    plt.text(i, v + 0.2, f"{v:.1f}", ha='center', fontweight='bold', fontsize=10)

plt.tight_layout()
plt.savefig("grafico_livros.png", dpi=300)
plt.show()

# --- Gráfico 3: distribuição por nível educacional ---
plt.figure(figsize=(8,5))
contagem = df["nivel_educacional"].value_counts()
contagem.plot(kind="bar", color=cor_educacao)
plt.title("Distribuição de nível educacional", fontsize=14, fontweight="bold")
plt.ylabel("Quantidade de pessoas", fontsize=12)
plt.xlabel("Nível educacional", fontsize=12)
plt.xticks(rotation=30, fontsize=10)
plt.yticks(fontsize=10)

# Valores sobre as barras
for i, v in enumerate(contagem):
    plt.text(i, v + 1, str(v), ha='center', fontweight='bold', fontsize=10)

plt.tight_layout()
plt.savefig("grafico_educacional.png", dpi=300)
plt.show()

# --- Gráfico 4: Escolaridade por hábito de leitura ---
escolaridade_por_leitura = df.groupby("lia_na_infancia")["nivel_educacional"].value_counts().unstack().fillna(0)
print("\nDistribuição de escolaridade por hábito de leitura na infância:")
print(escolaridade_por_leitura)

plt.figure(figsize=(8,5))
escolaridade_por_leitura.plot(kind="bar", stacked=True, figsize=(8,5), colormap=colormap_empilhado)
plt.title("Escolaridade por hábito de leitura na infância", fontsize=14, fontweight="bold")
plt.ylabel("Quantidade de pessoas", fontsize=12)
plt.xlabel("Lia na infância", fontsize=12)
plt.xticks(rotation=0, fontsize=10)
plt.yticks(fontsize=10)
plt.legend(title="Nível educacional", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10, title_fontsize=12)

plt.tight_layout()
plt.savefig("escolaridade_por_leitura.png", dpi=300)
plt.show()
