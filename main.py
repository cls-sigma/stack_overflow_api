from fastapi import FastAPI

app = FastAPI()



with open("classes.txt", "r") as h:
  clas=h.read()
clas=clas.split(',')
model=pickle.load(open('stack_model.pkl', 'rb'))

def out(sentence):
    predict=model.predict([sentence])
    output=[]
    for i, j in zip(predict[0], classes):
      if i==1:
        output.append(j)
      else:
        pass
    return output

  
@app.post("/tags")
async def predict(doc: str):
    pred=out(doc)
    return {"Tags": pred}
