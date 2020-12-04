##definición de UserInDB

from typing import Dict
from pydantic import BaseModel

#Herencia en python.. se define clase UserInDB
class UserInDB(BaseModel):
    # se define el tipo de dato 
    username: str
    password: str
    balance: int

## 2: definición de la base de datos ficticia
#Determibamos la estrcutura de los elementos que estan dentro de database_user, debe tener un strin y un objeto UserInDB
database_users = Dict[str, UserInDB]
#SE agregan datos a database_user
database_users = {
# el nombre es la llave : mapeamos el objeto con cada dato de los objetos  UserInDB
    "camilo24": UserInDB(**{"username":"camilo24",
                            "password":"root",
                            "balance":12000}),
    "andres18": UserInDB(**{"username":"andres18",
                            "password":"hola",
                            "balance":36000}),
}

#Bloque 3: definición de funciones sobre la base de datos fictica

#funcion para reornar el objeto UserInDb
def get_user(username: str):
    # si el nombre dado esta dentro de las llaves
    if username in database_users.keys():
        #retorna el objeto completo
        return database_users[username]
    else:
        #si no, no retorna nada
        return None
# funcion recibe un userindb un objeto
def update_user(user_in_db: UserInDB):
    #Coje le nombre o la llave  que recibe y lo actualiza 
    database_users[user_in_db.username] = user_in_db
    return user_in_db
