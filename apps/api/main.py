import os
import uvicorn

def str_to_bool(value: str) -> bool:
    """Verifica si se definió la variable debug"""
    return value.lower() in ("true", "1", "yes")

if __name__ == "__main__":
    debug = str_to_bool(os.getenv("DEBUG", "false"))

    uvicorn.run(
        "app:app",  host="127.0.0.1",
        port=8000,  reload=debug
    )
