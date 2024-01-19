import bentoml
from sentence_transformers import SentenceTransformer
from typing import Any

from bentoml.io import JSON
from numpy.typing import NDArray

class BertRunnable(bentoml.Runnable):
    SUPPORTED_RESOURCES = ("cpu",)
    SUPPORTS_CPU_MULTI_THREADING = False
    
    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/multi-qa-distilbert-cos-v1')
        
    @bentoml.Runnable.method(batchable=False)
    def get_embedding(self, input_data: str) -> NDArray[Any]:
        query_emb = self.model.encode(input_data)
        
        return query_emb
    
bert_runner = bentoml.Runner(BertRunnable, name="bert")
svc = bentoml.Service("bert", runners=[bert_runner])

@svc.api(input=JSON(), output=JSON())
def embeddings(input_data: JSON()):
    sentence = input_data["instances"]
    dicc = {
        "predictions": bert_runner.get_embedding.run(sentence)
    }
    
    return dicc