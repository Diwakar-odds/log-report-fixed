There is an Apache-style access log located at the absolute path `/app/access.log`. Analyze the network traffic recorded in this log file and generate a summary report saved exactly as a JSON file at `/app/report.json`.

The resulting JSON object must contain the following keys:
1. `total_requests`: The total number of non-empty log lines processed.
2. `unique_ips`: The total number of unique client IP addresses (the first space-separated token on each log line).
3. `top_path`: The most frequently requested HTTP resource path (e.g., `/index.html`), extracted cleanly from the standard HTTP request section (supporting methods like GET, POST, PUT, DELETE, HEAD, PATCH).

### Success Criteria
1. A valid JSON file is created precisely at `/app/report.json`.
2. The JSON structure contains the keys `total_requests`, `unique_ips`, and `top_path`.
3. The values associated with these keys accurately match the parsed analytics derived from `/app/access.log`.

You have 120 seconds to complete this task.
