# DNSForge

A dependency-free DNS inspection CLI for diagnostics, troubleshooting, and authorized security review.

## Features

- A, AAAA, MX, NS, TXT and CNAME lookups
- Reverse DNS
- Resolver comparison
- JSON output
- Clear error handling
- No packet crafting or exploitation

```text
dnsforge example.com
dnsforge example.com --type MX --json
dnsforge 8.8.8.8 --reverse
```

Use it only against infrastructure you are authorized to inspect.

Credits: https://guns.lol/meduu
