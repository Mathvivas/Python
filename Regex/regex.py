import re

email1 = 'Meu número é 91234-1234'
email2 = 'Fale comigo em 97483-3452, esse é meu celular'
email3 = '97463-4625 é meu celular'
email4 = 'lalalalalala 97462-4210 hdjiwhfyafgdfs hdhfgryldmn'

padrao = '[0-9]{5}[-][0-9]{4}'

retorno1 = re.search(padrao, email1)
retorno2 = re.search(padrao, email2)
retorno3 = re.search(padrao, email3)
retorno4 = re.search(padrao, email4)

print(retorno1.group())
print(retorno2.group())
print(retorno3.group())
print(retorno4.group())