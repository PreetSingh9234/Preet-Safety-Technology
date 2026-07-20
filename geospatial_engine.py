import plotly.graph_objects as go
import pandas as pd
import random

def generate_factory_map():
    zones = [
        {
            "name": "Chemical Processing Unit",
            "x": 8,
            "y": 7,
            "risk": "CRITICAL",
            "gas": random.randint(100, 150),
            "activity": "HOT WORK"
        },
        {
            "name": "Steel Furnace Zone",
            "x": 6,
            "y": 8,
            "risk": "HIGH",
            "gas": random.randint(70, 110),
            "activity": "Maintenance"
        },
        {
            "name": "Assembly Line",
            "x": 4,
            "y": 4,
            "risk": "WARNING",
            "gas": random.randint(30, 70),
            "activity": "Production"
        },
        {
            "name": "Storage Area",
            "x": 2,
            "y": 2,
            "risk": "SAFE",
            "gas": 20,
            "activity": "Normal"
        }
    ]

    colors = {
        "SAFE": "green",
        "WARNING": "orange",
        "HIGH": "red",
        "CRITICAL": "darkred"
    }

    fig = go.Figure()

    # Risk Zone Layer
    for zone in zones:
        fig.add_trace(
            go.Scatter(
                x=[zone["x"]],
                y=[zone["y"]],
                mode="markers+text",
                marker=dict(size=70, color=colors[zone["risk"]], opacity=0.65),
                text=[
                    f"{zone['name']}<br>Risk: {zone['risk']}<br>Gas: {zone['gas']} ppm<br>Activity: {zone['activity']}"
                ],
                textposition="top center",
                name="Risk Zone"
            )
        )

    # Risk Radius
    fig.add_shape(
        type="circle",
        x0=6.8, y0=5.8, x1=9.2, y1=8.2,
        line=dict(color="red"),
        fillcolor="red", opacity=0.15
    )

    # Worker Layer
    workers = [
        ("Worker-001", 3, 7, "SAFE"),
        ("Worker-003", 5, 5, "WARNING"),
        ("Worker-005", 8, 6, "DANGER"),
        ("Worker-007", 6, 8, "SAFE")
    ]

    for worker, x, y, status in workers:
        fig.add_trace(
            go.Scatter(
                x=[x],
                y=[y],
                mode="markers+text",
                marker=dict(size=22, color="cyan"),
                text=[f"{worker}<br>{status}"],
                textposition="bottom center",
                name="Worker Tracking"
            )
        )

    # Emergency Command Marker
    fig.add_trace(
        go.Scatter(
            x=[8],
            y=[7],
            mode="markers",
            marker=dict(size=120, color="red", opacity=0.25),
            name="AI Emergency Zone"
        )
    )

    fig.update_layout(
        title="🏭 AI Factory Digital Twin - Dynamic Safety Intelligence Map",
        xaxis=dict(title="Plant Coordinate X", range=[0, 10]),
        yaxis=dict(title="Plant Coordinate Y", range=[0, 10]),
        height=650,
        template="plotly_dark"
    )

    return fig

def generate_worker_tracking_map():
    workers = pd.DataFrame({
        "Worker": ["Worker-001", "Worker-003", "Worker-005", "Worker-007"],
        "X": [3, 5, 8, 6],
        "Y": [7, 5, 6, 8],
        "Risk": ["SAFE", "WARNING", "HIGH", "SAFE"]
    })

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=workers["X"],
            y=workers["Y"],
            mode="markers+text",
            marker=dict(size=30, color="cyan"),
            text=workers["Worker"],
            textposition="top center"
        )
    )

    fig.update_layout(
        title="👷 Live Worker Safety Location Intelligence",
        height=500,
        template="plotly_dark"
    )

    return fig

def get_zone_risk_summary():
    return pd.DataFrame([
        {
            "Zone": "Chemical Processing Unit",
            "Risk": "CRITICAL",
            "Cause": "Gas + Hot Work Permit Conflict"
        },
        {
            "Zone": "Steel Furnace Zone",
            "Risk": "HIGH",
            "Cause": "Maintenance Activity"
        },
        {
            "Zone": "Assembly Line",
            "Risk": "WARNING",
            "Cause": "Worker Condition Monitoring"
        },
        {
            "Zone": "Storage Area",
            "Risk": "SAFE",
            "Cause": "Normal Operation"
        }
    ])