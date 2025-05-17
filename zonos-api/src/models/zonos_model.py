
from pydantic import BaseModel


class ZonosPostSchema(BaseModel):
    audio_file_path: str
    text: str
    language: str
    output_file_path: str