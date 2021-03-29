from dataclasses import dataclass

from lightning_transformers.core.nlp.huggingface.config import HFTransformerDataConfig


@dataclass
class TokenClassificationDataConfig(HFTransformerDataConfig):
    task_name: str = "ner"
    label_all_tokens: bool = False