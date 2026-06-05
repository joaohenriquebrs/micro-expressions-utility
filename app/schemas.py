"""Schemas Pydantic de entrada/saída da API (contratos OpenAPI).

Campos novos devem ter valor padrão para manter retrocompatibilidade do frontend.
"""

from datetime import datetime

from pydantic import BaseModel

from app.models import JobStatus


class MeetingCreatedResponse(BaseModel):
    """Resposta do upload: id da reunião e status inicial do job."""

    meeting_id: int
    status: JobStatus


class MeetingStatusResponse(BaseModel):
    """Status atual do processamento (consultado via polling)."""

    meeting_id: int
    status: JobStatus


class MeetingSummary(BaseModel):
    """Item da listagem de reuniões do usuário."""

    id: int
    filename: str
    status: JobStatus
    created_at: datetime


class MeetingReportResponse(BaseModel):
    """Relatório consolidado em Markdown (nulo enquanto não `completed`)."""

    meeting_id: int
    status: JobStatus
    report_markdown: str | None = None
