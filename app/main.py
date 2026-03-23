from fastapi import FastAPI


app = FastAPI(title="agent-runtime-core")


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
