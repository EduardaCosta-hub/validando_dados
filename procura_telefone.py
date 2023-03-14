import re
padrao = '[0-9]{2}[0-9]{4,5}[0-9]{4}'
texto = "salkdfjdsa 1234456666 ksfjskf 11222223333"
resposta = re.search(padrao,texto)
print(resposta.group)