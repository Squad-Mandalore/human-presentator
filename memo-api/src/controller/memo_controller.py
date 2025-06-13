import os
from pathlib import Path
import shutil
from typing import Annotated
import uuid
from fastapi import APIRouter, File, HTTPException, UploadFile, status
from fastapi.responses import FileResponse
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
        audio_filename = f"audio_{uuid.uuid4()}"
        audio_path_file = f"{audio_filename}.wav"
        with open(audio_path_file, "wb") as buffer:
            shutil.copyfileobj(audio_file.file, buffer)

        picture_filename = f"picture_{uuid.uuid4()}"
        picture_path_file = f"{picture_filename}.jpg"
        with open(picture_path_file, "wb") as buffer:
            shutil.copyfileobj(picture.file, buffer)

        # Ausgabepfad definieren
        output_path = f"{Path(__file__).parent}/assets/videos"
        output_path_file = f"{output_path}/{picture_filename}_{audio_filename}.mp4"

        generate_from_picture_and_audio(audio_filename, picture_filename, output_path)

        return FileResponse(
            path=output_path_file,
            media_type="video/mp4",
            filename="memo_video.mp4",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}",
        )
    finally:
        # Remove temporary input file
        if os.path.exists(audio_path_file):
            os.remove(audio_path_file)
        if os.path.exists(picture_path_file):
            os.remove(picture_path_file)
