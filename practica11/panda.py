import pandas as pd
import matplotlib.pyplot as plt

fbk = ["Facebook", 2449, 2006]
twt = ["Twitter", 339, 2006]
ig = ["Instagram", 1000, 2009]
yt = ["Youtube", 2000, 2005]
wsp = ["Whatsapp", 1600, 2009]

lista_redes = [fbk,twt, ig, yt, wsp]

df_redes= pd.Dataframe(lista_redes, columns=["nombre", "cantidad","Año"])
df_redes

plt.plot(df_redes["nombre"], df_redes["cantidad"])
plt.show

plt.title("Diagrama de Lineas")
plt.xlabel("Redes")
plt.ylabel("Cantidad")
plt.show()

df_redes_ordenadas = df_redes.sort_values("Cantidad", asceding=False)
plt.bar(df_redes_ordenadas["Nombre"], df_redes_ordenadas["Cantidad"], color =["r","g","b"])
plt.title("Diagrama de lineas")
plt.xlabel("redes")
plt.ylabel("Cantidad")
plt.show()

lista_colores = ["#3b5998", "#FF0000", "#25d366", "#8a3ab9", "#00acee"]
plt.pie(df_redes_ordenadas["cantidad"],labels=df_redes_ordenadas["Nombre"], colors=lista_colores)
plt.title("grafico de lineas")
plt.show()