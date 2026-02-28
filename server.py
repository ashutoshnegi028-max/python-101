#!/usr/bin/env python3
"""Simple server to host the tracker form and collect submissions.

Run:
  python3 server.py

Then open:
  http://<your-ip>:8000

Saved files:
  data/submissions.ndjson
  data/submissions.csv
"""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HOST = "0.0.0.0"
PORT = 8000
BASE_DIR = Path(__file__).resolve().parent
FORM_FILE = BASE_DIR / "process_call_tracker_form.html"
DATA_DIR = BASE_DIR / "data"
NDJSON_FILE = DATA_DIR / "submissions.ndjson"
CSV_FILE = DATA_DIR / "submissions.csv"


class FormHandler(BaseHTTPRequestHandler):
    def _send_json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_html(self, html: str) -> None:
        body = html.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        if self.path in ("/", "/index.html", "/process_call_tracker_form.html"):
            self._send_html(FORM_FILE.read_text(encoding="utf-8"))
            return

        if self.path == "/api/submissions":
            count = 0
            if NDJSON_FILE.exists():
                with NDJSON_FILE.open("r", encoding="utf-8") as f:
                    count = sum(1 for line in f if line.strip())
            self._send_json(200, {"ok": True, "submissionCount": count})
            return

        self.send_error(404, "Not Found")

    def do_POST(self) -> None:  # noqa: N802
        if self.path != "/api/submissions":
            self.send_error(404, "Not Found")
            return

        content_length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(content_length)

        try:
            payload = json.loads(body.decode("utf-8"))
        except json.JSONDecodeError:
            self._send_json(400, {"ok": False, "error": "Invalid JSON payload"})
            return

        if not payload.get("employeeName"):
            self._send_json(400, {"ok": False, "error": "employeeName is required"})
            return

        DATA_DIR.mkdir(exist_ok=True)

        server_received_at = datetime.now(timezone.utc).isoformat()
        payload["serverReceivedAt"] = server_received_at

        with NDJSON_FILE.open("a", encoding="utf-8") as out:
            out.write(json.dumps(payload, ensure_ascii=False) + "\n")

        self._append_csv(payload)
        self._send_json(201, {"ok": True, "savedAt": server_received_at})

    def _append_csv(self, payload: dict) -> None:
        selected = payload.get("selectedProcesses", [])
        process_counts = payload.get("processCounts", {})
        calls = payload.get("calls", {})

        row = {
            "serverReceivedAt": payload.get("serverReceivedAt", ""),
            "submittedAt": payload.get("submittedAt", ""),
            "employeeName": payload.get("employeeName", ""),
            "selectedProcesses": ", ".join(selected),
            "onboardingCount": process_counts.get("Onboarding", 0),
            "verificationCount": process_counts.get("Verification", 0),
            "claimsCount": process_counts.get("Claims", 0),
            "billingCount": process_counts.get("Billing", 0),
            "escalationsCount": process_counts.get("Escalations", 0),
            "totalCount": payload.get("totalCount", 0),
            "hadCalls": calls.get("hadCalls", ""),
            "callCount": calls.get("callCount", 0),
            "callDurationMinutes": calls.get("callDurationMinutes", 0),
            "callDetails": calls.get("callDetails", ""),
        }

        fieldnames = list(row.keys())
        write_header = not CSV_FILE.exists()
        with CSV_FILE.open("a", encoding="utf-8", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if write_header:
                writer.writeheader()
            writer.writerow(row)


def main() -> None:
    if not FORM_FILE.exists():
        raise FileNotFoundError(f"Missing form file: {FORM_FILE}")

    server = ThreadingHTTPServer((HOST, PORT), FormHandler)
    print(f"Serving on http://{HOST}:{PORT}")
    print("Open this from your laptop/team: http://<server-ip>:8000")
    print(f"Responses will be saved under: {DATA_DIR}")
    server.serve_forever()


if __name__ == "__main__":
    main()
