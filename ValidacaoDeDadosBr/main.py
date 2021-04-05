from documento import Documento

## CPF VÁLIDO: 15316264754
cpf_exemplo = '15316264754'
cpf = Documento.criar_documento(cpf_exemplo)
print('CPF', cpf, sep=' = ')

## CNPJ VÁLIDA: 35379838000112
cnpj_exemplo = '35379838000112'
cnpj = Documento.criar_documento(cnpj_exemplo)
print('CNPJ', cnpj, sep=' = ')
