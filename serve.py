#!/usr/bin/env python3
"""
serve.py — local preview server for the codelab.

Use this instead of `python3 -m http.server`. The built-in server sends
`Content-Type: text/html` with NO charset, so browsers guess (often Latin-1)
and emoji / punctuation turn into mojibake (🎉 -> ðŸŽ‰, · -> Â·). This server
forces `charset=utf-8` on every text response, so everything renders correctly.

Usage:
    python3 serve.py            # http://localhost:8000
    python3 serve.py 8080       # custom port
"""

import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

class UTF8Handler(SimpleHTTPRequestHandler):
    def guess_type(self, path):
        ctype = super().guess_type(path)
        # Append charset for text-based types so browsers decode as UTF-8.
        textish = ctype.startswith("text/") or ctype in (
            "application/javascript", "application/json", "image/svg+xml",
        )
        if textish and "charset" not in ctype:
            ctype += "; charset=utf-8"
        return ctype

if __name__ == "__main__":
    print(f"Serving the codelab at http://localhost:{PORT}  (Ctrl+C to stop)")
    ThreadingHTTPServer(("", PORT), UTF8Handler).serve_forever()
