from cpf_cnpj import CpfCnpj
import re
padrao = '[0-9]{2}[0-9]{4,5}[0-9]{4}'
texto = "salkdfjdsa 1234456666 ksfjskf 11222223333"
resposta = re.search(padrao,texto)
todos = re.findall(padrao,texto)
print(resposta.group())
print(todos)
cpf = CpfCnpj('04688460007')
print(cpf.documento_formatado)