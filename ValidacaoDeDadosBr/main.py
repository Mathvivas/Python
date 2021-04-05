from documento import Documento
from telefone import Telefone
from data import Datas
from cep import BuscaEndereco

## CPF VÁLIDO: 15316264754
cpf_exemplo = '15316264754'
cpf = Documento.criar_documento(cpf_exemplo)
print('CPF', cpf, sep=' = ')

## CNPJ VÁLIDA: 35379838000112
cnpj_exemplo = '35379838000112'
cnpj = Documento.criar_documento(cnpj_exemplo)
print('\nCNPJ', cnpj, sep=' = ')


tel1 = '552126481234'
tel2 = '11784732309'
telefone = Telefone(tel1)
print('\nNúmero', telefone, sep=' = ')
celular = Telefone(tel2)
print('Número', celular, sep=' = ')


data = Datas()
print('\nData', data, sep=' = ')
print(data.tempo_de_cadastro())


cep = '01001000'
objeto_cep = BuscaEndereco(cep)
print('\nCEP', objeto_cep, sep=' = ')
bairro, cidade, uf = objeto_cep.acessa_via_cep()
print('Bairro', bairro, sep=' = ')
print('Cidade', cidade, sep=' = ')
print('UF', uf, sep=' = ')
