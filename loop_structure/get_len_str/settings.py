from pydantic_settings import BaseSettings
from pathlib import Path
from typing import ClassVar

class GlobalConfig(BaseSettings):
    TEST_STRING: str = 'The quick brown fox jumps over the lazy dog'
    EXPECTED_LENGTH: int = 35

    base_dir: ClassVar[Path] = Path(__file__).parent / 'srv'
    FILE_NAME: ClassVar[Path] = Path(base_dir / "large_test.txt")
    META_FILE: ClassVar[Path] = Path(base_dir / "large_test_metadata.json")
    NUM_PARAGRAPHS: int = 1
    SPACE_RATIO: float = 0.18

config = GlobalConfig()