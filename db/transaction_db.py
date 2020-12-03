#implemeta la slobrerias
from datetime import datetime
from pydantic import BaseModel

#hereda de BaseModel  y define cad auno de los atributos
class TransactionInDB(BaseModel):
    id_transaction: int = 0
    username: str
    date: datetime = datetime.now()
    value: int
    actual_balance: int

#  Bloque 2: definición de la base de datos ficticia y una función
##diccionario vacio
database_transactions = []
## auti incremental una lista
generator = {"id":0}
## se define una funcion para guardar una transaccion el abse de datos
def save_transaction(transaction_in_db: TransactionInDB):
    generator["id"] = generator["id"] + 1
    transaction_in_db.id_transaction = generator["id"]
    database_transactions.append(transaction_in_db)
    return transaction_in_db