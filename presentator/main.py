import requests
import tempfile
from pathlib import Path

class ZonosClient:
    def __init__(self, base_url: str = "http://localhost:8001"):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def create_speech(
        self,
        audio_path: Path,
        text: str,
        language: str,
    ) -> requests.Response:
        """
        POST /zonos/:
          - audio_file: binary
          - text: string
          - language: string
        """
        files = {
            "audio_file": audio_path.open("rb"),
        }
        data = {
            "text": text,
            "language": language,
        }
        resp = self.session.post(f"{self.base_url}/zonos/", files=files, data=data)
        # you might want to call resp.raise_for_status() here
        return resp


class MemoClient:
    def __init__(self, base_url: str = "http://localhost:8002"):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def create_memo_video(
        self,
        audio_path: Path,
        picture_path: Path,
    ) -> requests.Response:
        """
        POST /memo/:
          - audio_file: binary
          - picture: binary
        """
        files = {
            "audio_file": audio_path.open("rb"),
            "picture": picture_path.open("rb"),
        }
        resp = self.session.post(f"{self.base_url}/memo/", files=files)
        # resp.json() → your API’s JSON response
        return resp


if __name__ == "__main__":
    zonos = ZonosClient()
    memo = MemoClient()

    # Example usage:
    z_resp = zonos.create_speech(
        audio_path=Path("../zonos-api/sample.wav"),
        text="Hello, world! My name is Agent P an egg laying mammel of action.",
        language="en-us",
    )
    z_resp.raise_for_status()
    print("Zonos status:", z_resp.status_code)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(z_resp.content)
        tmp_path = Path(tmp.name)

    print("Saved Zonos audio to:", tmp_path)

    m_resp = memo.create_memo_video(
        audio_path=tmp_path,
        picture_path=Path("ranni.png"),
    )
    m_resp.raise_for_status()
    print("Memo status:", m_resp.status_code)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as vid_tmp:
        vid_tmp.write(m_resp.content)
        video_path = Path(vid_tmp.name)

    print("Saved Memo video to:", video_path)
