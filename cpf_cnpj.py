from validate_docbr import CPF, CNPJ
class CpfCnpj():
    def __init__(self, documento) -> None:
        self.__documento = str(documento)
        self.__tipo_documento = str("")
        self.__documento_formatado = str("")
        self.valida_documento()        
        
    #Methods 
    def valida_cpf(self):
        valida = CPF()
        if not valida.validate(self.__documento):
            raise ValueError("CPF inválido!")
        
    def formata_cpf(self):
        formata = CPF()
        cpf_formatado = formata.mask(self.__documento)
        return cpf_formatado
    
    def valida_cnpj(self):
        valida = CNPJ()
        if not valida.validate(self.__documento):
            raise ValueError("CNPJ inválido!")
        
    def formata_cnpj(self):
        formata = CNPJ()
        cnpj_formatado = formata.mask(self.__documento)
        return cnpj_formatado
    
    def define_tipo_doc(self):
        if len(self.__documento) == 11:
            self.__tipo_documento = "CPF"   
        elif len(self.__documento) == 14:
            self.__tipo_documento = "CNPJ"
        else:
            raise ValueError("Quantidade de caracteres incompatíveis com CPF ou CPNJ.")
    
    def valida_documento(self):
        self.define_tipo_doc()
        if self.__tipo_documento == "CPF":
            self.valida_cpf()
            self.__documento_formatado = self.formata_cpf()
        elif self.__tipo_documento == "CNPJ":
            self.valida_cnpj()
            self.__documento_formatado = self.formata_cnpj()
    
    #Properties
    @property
    def documento(self):
        return self.__documento
    
    @property
    def documento_formatado(self):
        return self.__documento_formatado