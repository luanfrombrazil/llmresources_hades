# Servidor MCP da biblioteca HADES (mcp-server/README.md).
#   docker build -t hades-mcp .
#   docker run -i --rm -v "$PWD:/work" hades-mcp                       # stdio (padrão)
#   docker run --rm -p 8000:8000 -e HADES_MCP_TRANSPORT=streamable-http hades-mcp   # HTTP em /mcp
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    HADES_LIB_ROOT=/opt/hades-lib \
    HADES_MCP_HOST=0.0.0.0 \
    HADES_MCP_PORT=8000

# fonte usada pela prévia PNG
RUN apt-get update && apt-get install -y --no-install-recommends fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/hades-lib
COPY mcp-server/pyproject.toml mcp-server/README.md mcp-server/
COPY mcp-server/hades_mcp mcp-server/hades_mcp
RUN python -m pip install ./mcp-server

# biblioteca (docs, catálogo, componentes, exemplos, hdslib)
COPY . /opt/hades-lib

RUN useradd -m -u 1000 hades && mkdir -p /work && chown hades /work
USER hades
WORKDIR /work
VOLUME ["/work"]
EXPOSE 8000

ENTRYPOINT ["hades-mcp"]
