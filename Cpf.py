from validate_docbr import CPF
class Cpf():
    def __init__(self, cpf) -> None:
        self.__cpf = str(cpf)
        self.valida_cpf()
        self.__cpf_formatado = self.formata_cpf()
        
    #Methods
    def valida_cpf(self):
        if len(self.__cpf) == 11:
            if not CPF(self.__cpf):
                raise ValueError("CPF inválido!")
        else:
            raise ValueError("Quantidade de caracteres inválida para CPF!")
                
    
    def formata_cpf(self):
        parte_a = self.__cpf[:3]
        parte_b = self.__cpf[3:6]
        parte_c = self.__cpf[6:9]
        parte_d = self.__cpf[9:]
        cpf_formatado = (f"{parte_a}.{parte_b}.{parte_c}-{parte_d}")
        return cpf_formatado
    
    #Properties
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def cpf_formatado(self):
        return self.__cpf_formatado