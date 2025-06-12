from memo import inference
from importlib import resources


def generate_from_picture_and_audio(
    filepath_picture: str, filepath_audio: str, output_path: str
):
    try:
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


def get_resource_path(dir: str, file: str) -> str:
    with resources.path(f"memo.{dir}", file) as p:
        return str(p)
