from configparser import NoOptionError
from xml.dom import NotFoundErr  
from os import listdir




class caracter_base:
    def __init__ (self) -> None:
        self.caracter_bases = [i for i in listdir(".") if i.endswith(".txt") and i.startswith("Base_")]
    
    def return_base(self,nome):
        
        if 'Base_'+nome+'.txt' not in caracter_bases:
            raise NotFoundErr(f"{nome} não foi encontrado")
        
        return_list = []
        example = None
        
        with open("Base_"+nome+".txt","r") as arq:
            for caracter in arq.readlines():
                if caracter.startswith("ex.:"):
                    example = caracter[4:].split()
                    continue
                
                return_list.append(caracter.split())
        
        return (example,return_list)
    
    @staticmethod
    def base_format(caracter_base,pre:str=None,pos:str=None,ins:str=None,ins_index:int=-1,insert:bool=True):
        for i in range(len(caracter_base)):
            if ins is not None:
                if ins_index is None: raise NoOptionError("O indece da inserção não foi especificado")
                
                if insert:
                    caracter_base[i] = caracter_base[i][:ins_index]+ins+caracter_base[i][ins_index:]
                else:
                    caracter_base[i] = caracter_base[i][:ins_index]+ins+caracter_base[i][ins_index+len(ins):]
                    
            if pos is not None:
                caracter_base[i] = caracter_base[i] + pos
                
            if pre is not None:
                caracter_base[i] = pre + caracter_base[i]
        
        
                    
        