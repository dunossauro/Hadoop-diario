import xlrd

#Função que lê o arquivo xls
def entrada(arq_xls):

    xls = xlrd.open_workbook(arq_xls)
    plan = xls.sheets()[0]

    for x in range(plan.nrows):
        yield plan.row_values(x)

#Conversão das strings para numeros
mes_num = {'JAN':1,'FEV':2,'MAR':3,'ABR':4,
           'MAI':5,'JUN':6,'JUL':7,'AGO':8,
           'SET':9,'OUT':10,'NOV':11,'DEZ':12,
           'JAN ':1,'FEV ':2,'MAR ':3,'ABR ':4,
           'MAI ':5,'JUN ':6,'JUL ':7,'AGO ':8,
           'SET ':9,'OUT ':10,'NOV ':11,'DEZ ':12}

#Acerto para a mudança dos nomes dos arquivos
arq = []
num = range(17,100)
for x in num:
  arq.append("%s%s%s"%("ROB",x,".xls"))

num = range(2000,2016)
for x in num:
  arq.append("%s%s%s"%("DCE",x,".xls"))

#Onde a mágica acontece
for data in arq: #Iteração do nome dos arquivos

  for linha in entrada(data): #iteração da chamada da função
      
      for x in mes_num: #Iteração para resolver problemas na formatação
          if linha[3] == x:
            linha[3] = mes_num[linha[3]]
                        
            print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s"%(
              int(linha[1]),linha[3],int(linha[2]),
                  linha[12],linha[7],linha[9],
                  linha[10],linha[8],linha[11]))
