from fastapi import FastAPI

app = FastAPI()



#Chargement du model
model=pickle.load_model(open('stack_model', 'rb'))
classes=pickle.load_model(open('classes.pkl', 'rb'))

def out(predict):
    output=[]
    for i, j in zip(prediction, classes):
      if i==1:
        output.append(j)
      else:
        pass
    return output

  
@app.post("/tags")
async def predict(doc: str):
    pred=model.predict(doc)
    return {"Tags": out(pred)}
