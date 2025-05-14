from memo import inference
from importlib import resources


def get_resource_path(dir: str, file: str) -> str:
    with resources.path(f"memo.{dir}", file) as p:
        return str(p)


def main():
    # --config memo/configs/inference.yaml
    # --input_image memo/assets/examples/dicaprio.jpg
    # --input_audio memo/assets/examples/speech.wav --output_dir outputs

    args = [
        "--config",
        get_resource_path("configs", "inference.yaml"),
        "--input_image",
        get_resource_path("assets.examples", "dicaprio.jpg"),
        "--input_audio",
        get_resource_path("assets.examples", "speech.wav"),
        "--output_dir",
        "/tmp/out",
        # "--seed", "1234",
    ]

    inference.main(args)


if __name__ == "__main__":
    main()
