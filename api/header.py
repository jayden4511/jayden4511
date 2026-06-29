from http.server import BaseHTTPRequestHandler

SVG = """<svg width="680" height="160" viewBox="0 0 680 160" xmlns="http://www.w3.org/2000/svg">
  <path d="M 40 88 Q 170 30 340 88 Q 510 146 640 88"
        fill="none" stroke="#7c3aed" stroke-width="1" opacity="0.35"/>
  <path d="M 40 88 Q 170 146 340 88 Q 510 30 640 88"
        fill="none" stroke="#a78bfa" stroke-width="0.6" opacity="0.25"/>
  <circle cx="40" cy="88" r="2.5" fill="#7c3aed" opacity="0.5"/>
  <circle cx="640" cy="88" r="2.5" fill="#7c3aed" opacity="0.5"/>
  <text x="340" y="100"
        font-family="'Segoe UI', system-ui, sans-serif"
        font-size="38" font-weight="300" letter-spacing="16"
        fill="#e6edf3" text-anchor="middle">jayden-frisancho</text>
  <text x="340" y="132"
        font-family="'Segoe UI', system-ui, sans-serif"
        font-size="11" font-weight="400" letter-spacing="3"
        fill="#8b949e" text-anchor="middle">cs @ ucf · backend · ai / ml</text>
</svg>"""

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        encoded = SVG.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "image/svg+xml; charset=utf-8")
        self.send_header("Cache-Control", "public, max-age=3600")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def log_message(self, format, *args):
        pass
