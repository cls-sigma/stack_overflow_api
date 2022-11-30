"""from fastapi import FastAPI
from vosk import Model, KaldiRecognizer
import wave
import json
#pip install vosk pytube @ git+https://github.com/baxterisme/pytube@e50bb734308dda27f2519345bbe6d9e84442a18f
from pytube import YouTube
from io import BytesIO
from pydub import AudioSegment


def model1(url):
    #straeam audio to pydub
    yt = YouTube(url)
    o = BytesIO()
    path=BytesIO()
    videoStream = yt.streams.filter(only_audio=True).all()[0]
    videoStream.stream_to_buffer(o)  # save video to buffer
    o.seek(0)
    audo = AudioSegment.from_file(o)
    audo.set_channels(1)
    audo.export(path, "wav")
    path.seek(0)
    inFileName=path
    '''
    this script reads a mono wav file (inFileName) and writes out a json file (outfileResults) with the speech to text conversion results.  It then writes out another json file (outfileText) that only has the "text" values.
    '''
    #inFileName = 'mon.wav'
    outfileResults = 'results.json'
    outfileText = 'text.json'

    wf = wave.open(inFileName, "rb")

    # initialize a str to hold results
    results = ""
    textResults = []

    # build the vosk-model-small-en-us-0.15 and recognizer objects.
    model = Model("en")
    recognizer = KaldiRecognizer(model, wf.getframerate())
    recognizer.SetWords(True)

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            recognizerResult = recognizer.Result()
            results = results + recognizerResult
            # convert the recognizerResult string into a dictionary
            resultDict = json.loads(recognizerResult)
            # save the 'text' value from the dictionary into a list
            textResults.append(resultDict.get("text", ""))

    ##    else:
    ##        print(recognizer.PartialResult())

    # process "final" result
    results = results + recognizer.FinalResult()
    resultDict = json.loads(recognizer.FinalResult())
    textResults.append(resultDict.get("text", ""))
    print(results, textResults)
    #print(resultDict)
    dic=[results["result"] for i in results]
    n_dic=[]

    for i in dic:
        n_dic+=i
    print(n_dic)
    text = ""
    start=[n_dic[0]["start"]]
    end=[n_dic[-1]["end"]]
    for i in n_dic:
        if i!=n_dic[-1]:
            text += i["word"]
            if (i["end"]-n_dic[n_dic.index(i)+1]["start"]) < 1:
                pass
            else:
                text+="@@@--"
                end.append(i["end"])
                start.append(n_dic[n_dic.index(i)+1]["start"])


    print("start:",len(start), "end", len(end), "text:", text.split("@@@--"))
    liste=[(i,j,k) for i, j, k in zip(start, text.split("@@@--"), end )]
    return liste"""

'''
app=FastAPI()

@app.get("/")
async def appel(url, model):
    liste=model1(url, model)
    return liste
'''


"""app=FastAPI()

@app.get("/")
async def appel():

    return {"hello": "word"}

"""