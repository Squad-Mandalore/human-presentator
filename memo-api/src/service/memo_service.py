import torch
from memo import inference
from importlib import resources
import gc


def clear_gpu_memory():
    """Clear GPU memory cache"""
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        torch.cuda.synchronize()
        gc.collect()


def generate_from_picture_and_audio(
    filepath_picture: str, filepath_audio: str, output_path: str
):
    try:
        # Clear GPU memory before processing
        clear_gpu_memory()

        args = [
            "--config",
            get_resource_path("configs", "inference.yaml"),
            "--input_image",
            filepath_audio,
            "--input_audio",
            filepath_picture,
            "--output_dir",
            output_path,
            # "--seed", "1234",
        ]

        inference.main(args)

    except Exception as err:
        print(err)
        raise err
    finally:
        # Always clear GPU memory after processing (success or failure)
        clear_gpu_memory()


def get_resource_path(dir: str, file: str) -> str:
    with resources.path(f"memo.{dir}", file) as p:
        return str(p)
