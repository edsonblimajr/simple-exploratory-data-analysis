import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv("dataset_Facebook.csv")


#Listas Globais
lista_tipo = []
lista_categoria = []
lista_mesPublicacao = []
lista_maximoAlcancePost = []
lista_maximoEngajamentoUsuario = []
lista_maximoConsumidoresPost = []
lista_like = []
lista_compartilhou = []
lista_comentarios = []
lista_interacaoTotal = []

lista_tipo = dados["Type"].tolist()
lista_categoria = dados["Category"].tolist()
lista_mesPublicacao = dados["Post Month"].tolist()
lista_maximoAlcancePost = dados["Lifetime Post Total Reach"].tolist()
lista_maximoEngajamentoUsuario = dados["Lifetime Engaged Users"].tolist()
lista_maximoConsumidoresPost = dados["Lifetime Post Consumers"].tolist()
lista_comentarios = dados["comment"].tolist()
lista_like = dados["like"].tolist()
lista_compartilhou = dados["share"].tolist()
lista_interacaoTotal = dados["Total Interactions"].tolist()

dados = dados.drop(columns=["Page total likes","Post Weekday","Post Hour","Paid","Lifetime Post Total Impressions","Lifetime Post Consumptions"])


plt.bar(lista_tipo, lista_like,color="#e5e5e5")
plt.plot(lista_tipo, lista_like,'o')
plt.title("Quantidade de Curtidas para cada tipo de publicação")
plt.xlabel("Tipo de Publicação")
plt.ylabel("Curtidas")
plt.savefig("curtidaxtipo.png",dpi=300)
plt.show()

plt.bar(lista_tipo, lista_comentarios,color="#e5e5e5")
plt.plot(lista_tipo, lista_comentarios,'o')
plt.title("Quantidade de Comentários para cada tipo de publicação")
plt.xlabel("Tipo de Publicação")
plt.ylabel("Comentários")
plt.savefig("comentariosxtipo.png",dpi=300)
plt.show()

plt.bar(lista_tipo, lista_compartilhou,color="#e5e5e5")
plt.plot(lista_tipo, lista_compartilhou,'o')
plt.title("Quantidade de Compartilhamentos para cada tipo de publicação")
plt.xlabel("Tipo de Publicação")
plt.ylabel("Compartilhamentos")
plt.savefig("compartilhamentosxtipo.png",dpi=300)
plt.show()

plt.bar(lista_tipo, lista_maximoAlcancePost,color="#e5e5e5")
plt.plot(lista_tipo, lista_maximoAlcancePost,'o')
plt.title("Máximo de Alcance do Post para cada tipo de publicação")
plt.xlabel("Tipo de Publicação")
plt.ylabel("Máximo de Alcance do Post")
plt.savefig("maximoalcancextipo.png",dpi=300)
plt.show()

plt.bar(lista_tipo, lista_maximoEngajamentoUsuario,color="#e5e5e5")
plt.plot(lista_tipo, lista_maximoEngajamentoUsuario,'o')
plt.title("Máximo de Engajamento do Post para cada tipo de publicação")
plt.xlabel("Tipo de Publicação")
plt.ylabel("Máximo de Engajamento do Post")
plt.savefig("maximoengajamentoxtipo.png",dpi=300)
plt.show()

plt.bar(lista_tipo, lista_maximoConsumidoresPost,color="#e5e5e5")
plt.plot(lista_tipo, lista_maximoConsumidoresPost,'o')
plt.title("Máximo de Consumidores do Post para cada tipo de publicação")
plt.xlabel("Tipo de Publicação")
plt.ylabel("Máximo de Consumidores do Post")
plt.savefig("maximoconsumidoresxtipo.png",dpi=300)
plt.show()

plt.bar(lista_tipo, lista_interacaoTotal,color="#e5e5e5")
plt.plot(lista_tipo, lista_interacaoTotal,'o')
plt.title("Interacão Total do Post para cada tipo de publicação")
plt.xlabel("Tipo de Publicação")
plt.ylabel("Interacão Total do Post")
plt.savefig("interacaototalxtipo.png",dpi=300)
plt.show()

plt.bar(lista_categoria, lista_like,color="#e5e5e5")
plt.plot(lista_categoria, lista_like,'o')
plt.title("Quantidade de Curtidas para cada categoria de publicação")
plt.xlabel("Categoria de Publicação")
plt.ylabel("Curtidas")
plt.savefig("curtidaxcategoria.png",dpi=300)
plt.show()

plt.bar(lista_categoria, lista_comentarios,color="#e5e5e5")
plt.plot(lista_categoria, lista_comentarios,'o')
plt.title("Quantidade de Comentários para cada categoria de publicação")
plt.xlabel("Categoria de Publicação")
plt.ylabel("Comentários")
plt.savefig("comentariosxcategoria.png",dpi=300)
plt.show()

plt.bar(lista_categoria, lista_compartilhou,color="#e5e5e5")
plt.plot(lista_categoria, lista_compartilhou,'o')
plt.title("Quantidade de Compartilhamentos para cada categoria de publicação")
plt.xlabel("Categoria de Publicação")
plt.ylabel("Compartilhamentos")
plt.savefig("compartilhamentosxcategoria.png",dpi=300)
plt.show()

plt.bar(lista_categoria, lista_maximoAlcancePost,color="#e5e5e5")
plt.plot(lista_categoria, lista_maximoAlcancePost,'o')
plt.title("Máximo de Alcance do Post para cada categoria de publicação")
plt.xlabel("Categoria de Publicação")
plt.ylabel("Máximo de Alcance do Post")
plt.savefig("maximoalcancexcategoria.png",dpi=300)
plt.show()

plt.bar(lista_categoria, lista_maximoEngajamentoUsuario,color="#e5e5e5")
plt.plot(lista_categoria, lista_maximoEngajamentoUsuario,'o')
plt.title("Máximo de Engajamento do Post para cada categoria de publicação")
plt.xlabel("Categoria de Publicação")
plt.ylabel("Máximo de Engajamento do Post")
plt.savefig("maximoengajamentoxcategoria.png",dpi=300)
plt.show()

plt.bar(lista_categoria, lista_maximoConsumidoresPost,color="#e5e5e5")
plt.plot(lista_categoria, lista_maximoConsumidoresPost,'o')
plt.title("Máximo de Consumidores do Post para cada categoria de publicação")
plt.xlabel("Categoria de Publicação")
plt.ylabel("Máximo de Consumidores do Post")
plt.savefig("maximoconsumidoresxcategoria.png",dpi=300)
plt.show()

plt.bar(lista_categoria, lista_interacaoTotal,color="#e5e5e5")
plt.plot(lista_categoria, lista_interacaoTotal,'o')
plt.title("Interacão Total do Post para cada categoria de publicação")
plt.xlabel("Categoria de Publicação")
plt.ylabel("Interacão Total do Post")
plt.savefig("interacaototalxcategoria.png",dpi=300)
plt.show()

plt.bar(lista_mesPublicacao, lista_like,color="#e5e5e5")
plt.plot(lista_mesPublicacao, lista_like,'o')
plt.title("Quantidade de Curtidas para cada mês de publicação")
plt.xlabel("Mês de Publicação")
plt.ylabel("Curtidas")
plt.savefig("curtidaxmes.png",dpi=300)
plt.show()

plt.bar(lista_mesPublicacao, lista_comentarios,color="#e5e5e5")
plt.plot(lista_mesPublicacao, lista_comentarios,'o')
plt.title("Quantidade de Comentários para cada mês de publicação")
plt.xlabel("Mês de Publicação")
plt.ylabel("Comentários")
plt.savefig("comentariosxmes.png",dpi=300)
plt.show()

plt.bar(lista_mesPublicacao, lista_compartilhou,color="#e5e5e5")
plt.plot(lista_mesPublicacao, lista_compartilhou,'o')
plt.title("Quantidade de Compartilhamentos para cada mês de publicação")
plt.xlabel("Mês de Publicação")
plt.ylabel("Compartilhamentos")
plt.savefig("compartilhamentosxmes.png",dpi=300)
plt.show()

plt.bar(lista_mesPublicacao, lista_maximoAlcancePost,color="#e5e5e5")
plt.plot(lista_mesPublicacao, lista_maximoAlcancePost,'o')
plt.title("Máximo de Alcance do Post para cada mês de publicação")
plt.xlabel("Mês de Publicação")
plt.ylabel("Máximo de Alcance do Post")
plt.savefig("maximoalcancexmes.png",dpi=300)
plt.show()

plt.bar(lista_mesPublicacao, lista_maximoEngajamentoUsuario,color="#e5e5e5")
plt.plot(lista_mesPublicacao, lista_maximoEngajamentoUsuario,'o')
plt.title("Máximo de Engajamento do Post para cada mês de publicação")
plt.xlabel("Mês de Publicação")
plt.ylabel("Máximo de Engajamento do Post")
plt.savefig("maximoengajamentoxmes.png",dpi=300)
plt.show()

plt.bar(lista_mesPublicacao, lista_maximoConsumidoresPost,color="#e5e5e5")
plt.plot(lista_mesPublicacao, lista_maximoConsumidoresPost,'o')
plt.title("Máximo de Consumidores do Post para cada mês de publicação")
plt.xlabel("Mês de Publicação")
plt.ylabel("Máximo de Consumidores do Post")
plt.savefig("maximoconsumidoresxmes.png",dpi=300)
plt.show()

plt.bar(lista_mesPublicacao, lista_interacaoTotal,color="#e5e5e5")
plt.plot(lista_mesPublicacao, lista_interacaoTotal,'o')
plt.title("Interacão Total do Post para cada mês de publicação")
plt.xlabel("Mês de Publicação")
plt.ylabel("Interacão Total do Post")
plt.savefig("interacaototalxmes.png",dpi=300)
plt.show()

correlacao = dados.corr()
plot = sns.heatmap(correlacao, annot = True, fmt=".1f", linewidths=.8)
plot
plot.figure.savefig("correlacao.png",dpi=300)
