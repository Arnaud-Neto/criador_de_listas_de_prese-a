
class arq_info():
    def __init__(self,url,separador:str,start_colunm_index:int=0,start_line_index:int=1,nome_index:int=None,email_index:int=None,evento_index:int=None,nome_evento_index:int=None,data_evento_index:int=None,horario_evento_index:int=None,hora_inicio_evento_index:int=None,hora_termino_evento_index:int=None,local_evento_index:int=None) -> None:
        self.arq = []
        self.start_colunm_index = start_colunm_index
        with open(url,"r") as arq:
            Cline = start_line_index
            for line in arq.readlines():
                if Cline > 0:
                    Cline -= 1
                    continue
                line = line.split(separador)[start_colunm_index:]
                if len(self.arq) == 0:self.arq = [[] for i in range(len(line))]
                for i in range(len(line)):
                    self.arq[i].append(line[i])
        
        self.nome_index = nome_index
        self.email_index = email_index
        self.evento_index = evento_index
        self.nome_evento_index = nome_evento_index
        self.data_evento_index = data_evento_index
        self.horario_evento_index = horario_evento_index
        self.hora_termino_evento_index = hora_termino_evento_index
        self.hora_inicio_evento_index = hora_inicio_evento_index
        self.local_evento_index = local_evento_index
        
    def getNomes(self):
        return self.arq[self.nome_index - self.start_colunm_index]
    
    def getNomesEventos(self):
        return self.arq[self.nome_evento_index - self.start_colunm_index]
    
    def getEmails(self):
        return self.arq[self.email_index - self.start_colunm_index]
    
    def getEventos(self):
        return self.arq[self.evento_index - self.start_colunm_index]
    
    def getDatasEventos(self):
        return self.arq[self.data_evento_index - self.start_colunm_index]
    
    def getHorariosEventos(self):
        return self.arq[self.horario_evento_index - self.start_colunm_index]
    
    def getHoraTeminoEvento(self):
        return self.arq[self.hora_termino_evento_index - self.start_colunm_index]
    
    def getHoraInicioEvento(self):
        return self.arq[self.hora_inicio_evento_index - self.start_colunm_index]
    
    def getLocalEvento(self):
        return self.arq[self.local_evento_index - self.start_colunm_index]
    
    
    
    @staticmethod
    def getNomes(Obj:object,index:int) -> list:
        return Obj.arq[index - Obj.start_colunm_index]
    
    @staticmethod
    def getNomesEventos(Obj:object,index:int) -> list:
        return Obj.arq[index - Obj.start_colunm_index]
    
    @staticmethod
    def getEmails(Obj:object,index:int) -> list:
        return Obj.arq[index - Obj.start_colunm_index]
    
    @staticmethod
    def getEventos(Obj:object,index:int) -> list:
        return Obj.arq[index - Obj.start_colunm_index]
    
    @staticmethod
    def getDatasEventos(Obj:object,index:int) -> list:
        return Obj.arq[index - Obj.start_colunm_index]
    
    @staticmethod
    def getHorariosEventos(Obj:object,index:int) -> list:
        return Obj.arq[index - Obj.start_colunm_index]
    
    @staticmethod
    def getHoraTeminoEvento(Obj:object,index:int) -> list:
        return Obj.arq[index - Obj.start_colunm_index]
    
    @staticmethod
    def getHoraInicioEvento(Obj:object,index:int) -> list:
        return Obj.arq[index - Obj.start_colunm_index]
    
    @staticmethod
    def getLocalEvento(Obj:object,index:int) -> list:
        return Obj.arq[index - Obj.start_colunm_index]
                    
                

        
        
    