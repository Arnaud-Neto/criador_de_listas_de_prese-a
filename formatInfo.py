import erros
import caracter_bases.get_caracter_base as caracter_bases





def nome_assinatura(caracter_base:list,nomes:list,caracter_linha:str = "_", linha:bool=True,tam_max_nome:int=200,tam_total:int=400):
    if not linha: 
        caracter_linha = " "
    
    return_str = ''    
    for i in range(len(nomes)):
        r = ["{caracter_base[i]} {nomes[i]}"]
        e = 0
        while len(r[e])>tam_max_nome:
            r.append(' '*(len(caracter_base[i])+1)+ r[e][tam_max_nome:] )
            r[e] = r[e][:tam_max_nome]
            e +=1
            
        r[e].ljust(caracter_linha,tam_total)
        
        return_str = return_str+"\n"+"\n".join(r)
        
    return return_str

