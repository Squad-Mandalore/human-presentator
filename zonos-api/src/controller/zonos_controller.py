
import os
import shutil
from typing import Annotated
import uuid
from fastapi import APIRouter, File, Form, HTTPException, UploadFile, status
from fastapi.responses import FileResponse

from src.models.zonos_model import ZonosPostSchema
from src.service.zonos_service import create_zonos_model

router = APIRouter(
    prefix="/zonos",
    tags=["Zonos"],
    responses={404: {"description": "Not found"}},

)


@router.post("/", status_code=status.HTTP_201_CREATED) 
def create_zonos_speech(
    audio_file: Annotated[UploadFile, File(...)],
    text: Annotated[str, Form(...)],
    language: Annotated[str, Form(...)]
):
    try:
        # Temporäre Datei speichern
        temp_input_path = f"temp_input_{uuid.uuid4()}.wav"
        with open(temp_input_path, "wb") as buffer:
            shutil.copyfileobj(audio_file.file, buffer)

        # Ausgabepfad definieren
        output_path = f"output_{uuid.uuid4()}.wav"

        # Schema vorbereiten
        zonos_schema = ZonosPostSchema(
            audio_file_path=temp_input_path,
            text=text,
            language=language,
            output_file_path=output_path
        )


        create_zonos_model(zonos_schema)

        return FileResponse(
            path=zonos_schema.output_file_path,
            media_type="audio/wav",
            filename="output.wav",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )
    finally:
        # Optional: Temporäre Datei nach Verwendung löschen
        if os.path.exists(temp_input_path):
            os.remove(temp_input_path)