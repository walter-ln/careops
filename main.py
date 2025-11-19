from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import logging

app = FastAPI(
    title="CareOps+ API (Aula 2 – Versão Vulnerável)",
    version="0.2.0",
    description="Versão da aplicação com vulnerabilidades intencionais para estudo OWASP."
)

templates = Jinja2Templates(directory="templates")

# Logger inseguro: registra dados sensíveis
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("careops")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "message": "CareOps+ — Aula 2 (versão vulnerável)"}
    )


@app.get("/health")
async def health():
    return {"status": "ok"}


# ---------------------------------------------
# 1. Endpoint vulnerável: Input não validado
# ---------------------------------------------
@app.get("/echo", response_class=HTMLResponse)
async def echo(msg: str = ""):
    # Reflete diretamente o input sem sanitização (XSS risk)
    html = f"<h1>Echo:</h1><p>{msg}</p>"
    return HTMLResponse(content=html)


# -----------------------------------------------------------
# 2. Endpoint sem autenticação: Broken Access Control (A01)
# -----------------------------------------------------------
fake_db = {
    "1": {"id": 1, "name": "João Silva", "diagnosis": "Hipertensão"},
    "2": {"id": 2, "name": "Maria Oliveira", "diagnosis": "Asma"},
}

@app.get("/patient/{patient_id}")
async def get_patient(patient_id: str):
    logger.info(f"[INSECURE LOG] Consulta ao paciente {patient_id}")
    if patient_id in fake_db:
        return fake_db[patient_id]
    return JSONResponse({"error": "not found"}, status_code=404)


# ---------------------------------------------------------
# 3. Endpoint crítico (exposição de segredos / A02, A09)
# ---------------------------------------------------------
@app.get("/debug/config")
async def debug_config():
    # Exposição intencional para estudo
    config = {
        "SECRET_KEY": "123456",
        "DB_PASSWORD": "senha_super_secreta",
        "DEBUG_MODE": True
    }
    logger.warning(f"[CRITICAL] Configuração sensível exposta: {config}")
    return config
