# Build with:  docker build -t my-app .
# Run with:    docker run -p 8000:8000 my-app

FROM python:3-slim

WORKDIR /app

# 1. Copia apenas o arquivo de dependências (Garante o cache do Pip)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Copia o resto do projeto para o container
COPY . .

# 3. Dá permissão e define o entrypoint
RUN chmod +x /app/docker-entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/docker-entrypoint.sh"]
