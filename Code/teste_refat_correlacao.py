
# Verificar se o arquivo existe
# Método Try

from importlib.resources import path
import os.path





class Vazoes ():
    """_summary_  
    Return
    O arquivo em txt ou csv
    Arquivo preenchido com as previsões em relação as usinas.
    """
    def __init__(path: Path, mes: int, posto: int):
        """Parâmetros de entrada:
        path (Path): _description_
        mes (int): _description_
        posto (int): _description_
        """
        pass
    
    def teste():






#--------------------------------------------------------------------
def verificar_arquivo():
    """_summary_
    """
    try:
        with open('vazoes', 'r') as f:
            verificar_arquivo(f)
    except IOError:
        print ('Arquivo não encontrado!')        

    #ou:
    #os.path.isfile('vazoes')
#---------------------------------------------
