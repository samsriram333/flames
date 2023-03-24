from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Names(BaseModel):
    EnterYourName: str
    EnterCrushName: str
    
@app.get("/")    
async def test():
    str = "Welcome to my flames website"
    return str

@app.post("/flames")
async def flames_algorithm(names: Names):
    EnterYourName = list(names.EnterYourName.replace(" ","").lower())
    EnterCrushName  = list(names.EnterCrushName.replace(" ","").lower())
    for i in EnterYourName[:]:
        if i in EnterCrushName:
            EnterYourName.remove(i)
            EnterCrushName.remove(i)

    name = EnterYourName + EnterCrushName
    len_names_real = len(name)

    len_names  = len_names_real - 1
    word = list("flames")

    while len(word) > 1:
        index_value = len_names%len(word)
        word.pop(index_value)
        if index_value == 0 and index_value == len(word):
            print(f"index_value :{index_value}")
        else:
            str1 , str2 = word[:index_value],word[index_value:]
            word = str2 + str1

    result = ""     
    for i in word:
        result = i

    flames_dict = {"f":"Friend","l":"Love","a":"Affection","m":"Marriage","e":"Enemy","s":"Sister"} 
    final = {"Combination" : flames_dict[result] }       
    return final
