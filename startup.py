"""Configuracoes comuns aos experimentos do Lab Telecom."""
from dataclasses import dataclass


@dataclass(frozen=True)
class ExportConfig:
    formats: tuple[str, ...] = ("svg", "pdf", "png")
    dpi: int = 300
    transparent: bool = False
    bbox_inches: str = "tight"


EXPORT = ExportConfig()
