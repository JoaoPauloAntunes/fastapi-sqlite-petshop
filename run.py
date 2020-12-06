import uvicorn

uvicorn.run("source.main:app", port=8000, host="0.0.0.0")