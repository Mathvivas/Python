from documento import Documento
from telefone import Telefone

## CPF VÁLIDO: 15316264754
cpf_exemplo = '15316264754'
cpf = Documento.criar_documento(cpf_exemplo)
print('CPF', cpf, sep=' = ')

## CNPJ VÁLIDA: 35379838000112
cnpj_exemplo = '35379838000112'
cnpj = Documento.criar_documento(cnpj_exemplo)
print('CNPJ', cnpj, sep=' = ')


tel1 = '552126481234'
tel2 = '11784732309'
telefone = Telefone(tel1)
print('Número', telefone, sep=' = ')
celular = Telefone(tel2)
print('Número', celular, sep=' = ')