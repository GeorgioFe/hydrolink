@app.post("/set_reminder")
async def set_reminder(request: Request):
    global current_interval
    body = await request.json()
    current_interval = body.get("interval")
    if websocket_connection:
        await websocket_connection.send_text(str(current_interval))
    return JSONResponse(content={"message": "Interval received", "interval": current_interval})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    global websocket_connection
    await websocket.accept()
    websocket_connection = websocket
    try:
        while True:
            await websocket.receive_text()  # Keep the connection open
    except WebSocketDisconnect:
        websocket_connection = None