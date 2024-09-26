#https://pt.stackoverflow.com/questions/66183/como-retornar-um-valor-no-formato-moeda-brasileiro-na-view-do-django
from re import sub
from decimal import Decimal
import locale


# função que entra um valor formatado em US e o transforma em pt_BR
#valor = '1235987.65'
def valorUStoPTBR(valor):
    valor = Decimal(valor.replace(',', ''))
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    inteiro = locale.currency(valor, grouping=True, symbol=None)
    valor = str(valor).replace('.',',')
    #print('Valor: %s' % valor)
    return valor


# função que entra um valor formatado em pt_BR e o tranforma em US
#valor = '1698572,78'
def valorPTBRtoUS(valor):
    valor = Decimal(str(valor).replace(',', '.'))
    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
    locale.currency(valor, grouping=True, symbol=None)
    #print('Valor: %s' % valor)
    return valor


#print(valorPTBRtoUS(valor))