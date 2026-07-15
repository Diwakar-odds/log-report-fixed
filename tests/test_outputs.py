import json
import re
from collections import Counter
from pathlib import Path

def _calculate_ground_truth():
    """Helper function to calculate ground truth metrics exactly matching the oracle."""
    paths, ips, total = Counter(), set(), 0
    log_file = Path("/app/access.log")
    
    if not log_file.exists():
        return {"total_requests": 0, "unique_ips": 0, "top_path": ""}
        
    with open(log_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += 1
            ips.add(line.split()[0])
            m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
            if m:
                paths[m.group(1)] += 1
                
    return {
        "total_requests": total,
        "unique_ips": len(ips),
        "top_path": paths.most_common(1)[0][0] if paths else ""
    }

def test_criterion_1_file_exists_and_valid_json():
    """Verifies Success Criterion 1: A valid JSON report file is created precisely at the absolute path /app/report.json."""
    report_path = Path("/app/report.json")
    assert report_path.exists(), "The output file /app/report.json was not generated."
    
    try:
        with open(report_path, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        assert False, "/app/report.json is not structured as valid JSON."
        
    assert isinstance(data, dict), "The top-level structure of report.json must be a JSON object."

def test_criterion_2_required_keys_present():
    """Verifies Success Criterion 2: The JSON structure contains the keys total_requests, unique_ips, and top_path."""
    report_path = Path("/app/report.json")
    assert report_path.exists()
    
    with open(report_path, "r") as f:
        data = json.load(f)
        
    for key in ["total_requests", "unique_ips", "top_path"]:
        assert key in data, f"Required key '{key}' is missing from the generated report object."

def test_criterion_3_metrics_are_accurate():
    """Verifies Success Criterion 3: The values accurately match the parsed analytics derived from /app/access.log."""
    report_path = Path("/app/report.json")
    assert report_path.exists()
    
    with open(report_path, "r") as f:
        data = json.load(f)
        
    expected = _calculate_ground_truth()
    
    assert data["total_requests"] == expected["total_requests"], f"Value mismatch for total_requests: expected {expected['total_requests']}, got {data['total_requests']}"
    assert data["unique_ips"] == expected["unique_ips"], f"Value mismatch for unique_ips: expected {expected['unique_ips']}, got {data['unique_ips']}"
    assert data["top_path"] == expected["top_path"], f"Value mismatch for top_path: expected '{expected['top_path']}', got '{data['top_path']}'"
