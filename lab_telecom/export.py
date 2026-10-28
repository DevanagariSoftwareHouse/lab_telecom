"""Exportacao padronizada de figuras cientificas."""
from pathlib import Path

from startup import EXPORT, ExportConfig


def save_figure(figure, output_dir: str | Path, stem: str,
                config: ExportConfig = EXPORT) -> list[Path]:
    """Salva uma figura em todos os formatos configurados."""
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    paths = []
    for extension in config.formats:
        path = destination / f"{stem}.{extension}"
        figure.savefig(
            path,
            dpi=config.dpi,
            transparent=config.transparent,
            bbox_inches=config.bbox_inches,
        )
        paths.append(path)
    return paths
