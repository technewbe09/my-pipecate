import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "ok", "message": "Pipecat voicebot server is running!"}

@app.get("/client", response_class=HTMLResponse)
async def client_page():
    return """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Pipecat Voice Bot</title>
        <style>
          body { font-family: sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; background: #0f172a; color: #f8fafc; }
          button { padding: 12px 24px; font-size: 16px; border-radius: 8px; border: none; background: #2563eb; color: white; cursor: pointer; }
          button:hover { background: #1d4ed8; }
          #status { margin-top: 16px; font-size: 14px; color: #94a3b8; }
        </style>
      </head>
      <body>
        <h2>Pipecat Voice Assistant</h2>
        <button id="connectBtn" onclick="startCall()">Connect Microphone</button>
        <div id="status">Status: Ready to connect</div>

        <script>
          async function startCall() {
            const status = document.getElementById('status');
            status.innerText = "Requesting mic access...";
            try {
              const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
              status.innerText = "Mic granted! Connected to server.";
            } catch (err) {
              status.innerText = "Error: " + err.message;
            }
          }
        </script>
      </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run("bot:app", host="0.0.0.0", port=7860, reload=False)
