from dataclasses import dataclass
from pathlib import Path


# it will treat as a entity
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
