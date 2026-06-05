"""Geração de relatório real via Ollama local (HTTP). Refinamento de prompt: Sprint 3."""

from app.core.types import Segment, TimelineEntry
from app.services.errors import TemporaryError

_SYSTEM_PROMPT = (
    "Você é um analista comercial. A partir da transcrição e da timeline de sinais, gere um "
    "relatório em Markdown com EXATAMENTE estes títulos:\n"
    "# Relatório de Análise Comercial\n## 1. Resumo Executivo\n## 2. Objeções Identificadas\n"
    "## 3. Momentos de Alto Engajamento\n## 4. Próximos Passos Recomendados\n"
)


class OllamaReportGenerator:
    def __init__(self, base_url: str, model: str = "llama3:8b") -> None:
        self._base_url = base_url.rstrip("/")
        self._model = model

    def _build_prompt(self, segments: list[Segment], timeline: list[TimelineEntry]) -> str:
        transcript = "\n".join(f"[{s.speaker}] {s.text}" for s in segments)
        signals = "\n".join(
            f"{e.start_time} {e.speaker}: {[s['signal_type'] for s in e.signals]}"
            for e in timeline
            if e.signals
        )
        return f"{_SYSTEM_PROMPT}\n\n## Transcrição\n{transcript}\n\n## Sinais\n{signals}\n"

    def generate(self, segments: list[Segment], timeline: list[TimelineEntry]) -> str:
        import httpx

        prompt = self._build_prompt(segments, timeline)
        try:
            response = httpx.post(
                f"{self._base_url}/api/generate",
                json={"model": self._model, "prompt": prompt, "stream": False},
                timeout=120.0,
            )
            response.raise_for_status()
        except httpx.HTTPError as exc:
            raise TemporaryError(f"falha ao chamar o Ollama: {exc}") from exc
        return str(response.json().get("response", ""))
