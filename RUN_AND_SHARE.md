# Run and Share: Process & Call Tracker

This setup lets your whole team submit the form, and all responses are saved back to you.

## 1) Start the server

From this folder:

```bash
python3 server.py
```

You should see:

- `Serving on http://0.0.0.0:8000`
- Responses saved in `data/`

## 2) Open it yourself

On the same machine, open:

- `http://127.0.0.1:8000`

## 3) Share with team members (same network/VPN)

Find your machine IP:

```bash
hostname -I
```

Share this URL with your team:

- `http://<your-ip>:8000`

Example:

- `http://192.168.1.23:8000`

## 4) Where your collected data goes

Each submission is stored automatically in:

- `data/submissions.ndjson` (raw JSON per line)
- `data/submissions.csv` (Excel-friendly)

## 5) Open submissions in Excel

Open `data/submissions.csv` directly in Excel to view all team entries.

## 6) If team cannot access your link

Possible reasons:

- not on same network/VPN
- firewall blocking port `8000`
- your laptop is off/sleeping

Quick fix options:

- host this on a small cloud VM (same code)
- run behind ngrok / reverse proxy and share public URL

