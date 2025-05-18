
import os
import shutil
from typing import Annotated
import uuid
from fastapi import APIRouter, File, Form, HTTPException, UploadFile, status
from fastapi.responses import FileResponse

from src.service.zonos_service import generate_zonos_audio

router = APIRouter(
    prefix="/zonos",
    tags=["Zonos"],
    responses={404: {"description": "Not found"}},

)


@router.post("/", response_class=FileResponse, status_code=status.HTTP_200_OK) 
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

        generate_zonos_audio(temp_input_path, text, language, output_path)

        return FileResponse(
            path=output_path,
            media_type="audio/wav",
            filename="output.wav",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )
    finally:
        # Remove temporary input file
        if os.path.exists(temp_input_path):
            os.remove(temp_input_path)
        # Remove output file after sending the response