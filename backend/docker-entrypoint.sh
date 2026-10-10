#!/bin/sh

# Se qualquer comando falhar (como o alembic), o script para imediatamente
set -e

echo "Rodando as migrations do Alembic..."
alembic upgrade head

echo "Iniciando a API FastAPI com Uvicorn..."
# O 'exec' faz o Uvicorn virar o processo principal do container (ID 1)
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
