"""Paper v0.3.2, section 4.2: authored numerical illustration, not an agent."""
import json
from math import isclose

def calculate(history):
    identity, constraint, drive, signal = 0.6, 0.6, 0.7, 0.6
    rho, beta, threshold = 0.8, 0.5, 0.2
    u = identity * constraint
    incoming = drive * signal
    h = max(0.0, min(incoming, u))
    held = max(0.0, min(1.0, rho * history + (1 - rho) * h))
    force = incoming - u
    gate = force + beta * held
    return dict(H_previous=history, U=u, E_in=incoming, h=h,
                H_before_release=held, F=force, G=gate,
                threshold=threshold, gate_open=gate > threshold)

if __name__ == "__main__":
    low, high = calculate(0.0), calculate(0.5)
    assert isclose(low["G"], 0.096) and not low["gate_open"]
    assert isclose(high["G"], 0.296) and high["gate_open"]
    print(json.dumps({"kind": "authored_numeric_example_not_behavior_result",
                      "low_history": low, "high_history": high}, indent=2))
