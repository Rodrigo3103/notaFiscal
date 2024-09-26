cnpj = '54412549000112'
xNome = 'Ambev Distribuidora de Bebidas'
CRT = '31'

textoNotaFiscal = f"""
CRT = {CRT}
CNPJCPF = {cnpj}
xNome = {xNome}
xFant = Mineracao Sao Pedro
IE = 618007261112
xLgr = Rod. SP 191, KM 148
nro = SN
xCpl = 
xBairro = Matao
cMun = 3547007
xMun = Santa Maria da Serra
cUF = 35
UF = SP
CEP = 17370-000
cPais = 1058
xPais = BRASIL
Fone = (19) 3481-1011"""


#with open('NotasFiscal/configuracoes.txt', 'w') as arquivo:
 #   arquivo.write(textoNotaFiscal)
  #  arquivo.close()



import sys

coding = sys.stdout.encoding
a = "eu tenho uma maçã"
print(a)

print('peão')