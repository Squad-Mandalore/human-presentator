import os
import shutil
from typing import Annotated
import uuid
from fastapi import APIRouter, File, HTTPException, UploadFile, status
from src.service.memo_service import generate_from_picture_and_audio

router = APIRouter(
    prefix="/memo",
    tags=["Memo"],
    responses={404: {"description": "Not found"}},
)


# , response_class=FileResponse
@router.post("/", status_code=status.HTTP_200_OK)
def create_memo_video(
    audio_file: Annotated[UploadFile, File(...)],
    picture: Annotated[UploadFile, File(...)],
):
    try:
        # Temporäre Datei speichern
        temp_audio_path = f"temp_input_{uuid.uuid4()}.wav"
        with open(temp_audio_path, "wb") as buffer:
            shutil.copyfileobj(audio_file.file, buffer)

        temp_picture_path = f"temp_input_{uuid.uuid4()}.jpg"
        with open(temp_picture_path, "wb") as buffer:
            shutil.copyfileobj(picture.file, buffer)

        # Ausgabepfad definieren
        output_path = "/tmp/out"

        generate_from_picture_and_audio(temp_audio_path, temp_picture_path, output_path)

        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}",
        )
    finally:
        # Remove temporary input file
        if os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)
        if os.path.exists(temp_picture_path):
            os.remove(temp_picture_path)
