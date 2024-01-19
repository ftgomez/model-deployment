from typing import Any

import bentoml
from numpy.typing import NDArray
from sentence_transformers import SentenceTransformer
from transformers import pipeline


class BertRunnable(bentoml.Runnable):
    SUPPORTED_RESOURCES = ("cpu",)
    SUPPORTS_CPU_MULTI_THREADING = False

    def __init__(self):
        self.model = SentenceTransformer(
            "sentence-transformers/multi-qa-distilbert-cos-v1"
        )

    @bentoml.Runnable.method(batchable=False)
    def get_embedding(self, input_data: str) -> NDArray[Any]:
        query_emb = self.model.encode(input_data)

        return query_emb


class TransformersClassifierRunnable(bentoml.Runnable):
    SUPPORTED_RESOURCES = ("cpu",)
    SUPPORTS_CPU_MULTI_THREADING = False
    
    def __init__(self):
        self.model = pipeline("sentiment-analysis")
    
    @bentoml.Runnable.method(batchable=False)
    def classify(self, input_data: str) -> list:
        predicted_class = self.model(input_data)
        
        return predicted_class
    

bert_runner = bentoml.Runner(BertRunnable, name="bert")
classifier_runner = bentoml.Runner(TransformersClassifierRunnable, name="classifier")

bento_runners = {
    "bert": bert_runner,
    "classifier": classifier_runner
}
