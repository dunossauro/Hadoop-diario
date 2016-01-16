import matplotlib.pyplot as plt
import pandas

dados = pandas.read_csv('coleta.csv')

dados.plot(x="ano",kind='line')
