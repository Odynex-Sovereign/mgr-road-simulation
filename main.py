import os
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(
    title="MGR-Road Cloud Telemetry Gateway",
    description="Central ingestion layer for processing physical highway material structural metrics.",
    version="1.0.0"
)

# Standardized structural tracking blueprint for streaming edge array inputs
class TelemetryPayload(BaseModel):
    node_id: str
    hydraulic_pressure_psi: float
    fluid_temp_celsius: float
    copper_matrix_conductivity_pct: float
    valve_clog_risk_coefficient: float

# Diagnostic health response engine
@app.get("/")
def get_system_status() -> Dict[str, str]:
    return {
        "status": "ONLINE",
        "framework": "MGR-Road Core Integration",
        "storage_mount": "/data/mgr_telemetry.db",
        "compute_mode": "Hybrid Edge-Cloud Core"
    }

@app.post("/api/v1/telemetry")
def record_edge_telemetry(payload: TelemetryPayload) -> Dict[str, str]:
    if payload.hydraulic_pressure_psi <= 0:
        raise HTTPException(status_code=400, detail="Invalid physical metrics: Hydraulic pressure must be positive.")
    
    # Real-World Extension: Insert hooks here to stream payload lines directly into TimescaleDB / Postgres
    print(f"[CLOUD INGEST SUCCESS] Node: {payload.node_id} | Pressure: {payload.hydraulic_pressure_psi} PSI")
    return {"message": "Telemetry matrix committed successfully", "status": "SAVED"}

if __name__ == "__main__":
    host_ip = os.getenv("HOST", "0.0.0.0")
    port_num = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host=host_ip, port=port_num)
