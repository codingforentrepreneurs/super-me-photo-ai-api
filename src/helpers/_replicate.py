from functools import lru_cache

from decouple import config
from replicate.client import Client

REPLICATE_API_TOKEN = config("REPLICATE_API_TOKEN")
REPLICATE_MODEL = config("REPLICATE_MODEL")
REPLICATE_MODEL_VERSION = config("REPLICATE_MODEL_VERSION")

@lru_cache
def get_replicate_client():
    return Client(api_token=REPLICATE_API_TOKEN)

@lru_cache
def get_replicate_model_version():
    replicate_client = get_replicate_client()
    rep_model = replicate_client.models.get(REPLICATE_MODEL)
    rep_version = rep_model.versions.get(REPLICATE_MODEL_VERSION)
    return rep_version


def generate_image(prompt):
    input_args = {
        "prompt": prompt,
        "num_outputs": 2,
        "output_format": "jpg",
    }
    replicate_client = get_replicate_client()
    rep_version = get_replicate_model_version()
    pred = replicate_client.predictions.create(
        version=rep_version,
        input=input_args
    )
    return {
        "id": pred.id,
        "status": pred.status
    }