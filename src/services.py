import bentoml
from bentoml.io import JSON
from .runners import bento_runners


bert_svc = bentoml.Service("bert", runners=[bento_runners["bert"]])
classifier_svc = bentoml.Service("classifier", runners=[bento_runners["classifier"]])



@bert_svc.api(input=JSON(), output=JSON())
def embeddings(input_data: JSON()):
    sentence = input_data["instances"][0]
    dicc = {"predictions": bento_runners["bert"].get_embedding.run(sentence)}

    return dicc

@classifier_svc.api(input=JSON(), output=JSON())
def classification(input_data: JSON()):
    sentence = input_data["instances"][0]
    dicc = {"predictions": bento_runners["classifier"].classify.run(sentence)}
    
    return dicc