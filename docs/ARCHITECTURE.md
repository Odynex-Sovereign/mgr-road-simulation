# MGR-Road Digital Twin Simulation Architecture

This specification document outlines the asset assembly pipelines for translating physical field stress into the unified data graph via [NVIDIA OpenUSD](https://developer.nvidia.com/openusd "OpenUSD for Developers | NVIDIA Developer").

## 1. Unified Scene Description (OpenUSD) Scene Hierarchy

```text
/root (UsdStage)
└── /MGR_Road_Tile_Array (UsdGeomXform)
    ├── /Top_Wear_Layer (UsdGeomMesh) -> Sub-layered with Warp elastic deformation weights
    ├── /Microfluidic_Core (UsdGeomMesh) -> Evaluated via Modulus CFD velocity nodes
    └── /Telemetry_Enclosure (UsdGeomXform)
        └── /Jetson_Orin_Module (UsdGeomXform)
```

## 2. Interoperability & Assembly
* **OpenUSD Core Compliance:** All structural layers are stored as individual `.usd` / `.usda` layers. Non-destructive composition arcs (`references` and `payloads`) handle assembly to maintain optimization boundaries across cluster environments.
* **SimReady Schema Integration:** Layers map physical material configurations (Young's modulus, Poisson's ratio, kinematic fluid viscosities) to ensure downstream compatibility with physical AI pipelines.
