import re

def clean_text(text):
    # Regex para limpar texto e remover caracteres indesejados
    text = re.sub(r"[^a-zA-Z0-9\s,\.!?áéíóúâêîôûãõçÁÉÍÓÚÂÊÎÔÛÃÕÇ'-]", "", text)
    return text
