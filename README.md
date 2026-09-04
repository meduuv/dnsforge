# DNSForge

> Dependency-free DNS inspection for diagnostics and authorized security review.

[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-111111?style=flat-square)](LICENSE)

DNSForge is a lightweight DNS inspection CLI for troubleshooting domains, comparing resolver responses and producing machine-readable results.

## Features

- A, AAAA, MX, NS, TXT and CNAME lookups
- Reverse DNS
- Resolver comparison
- JSON output
- Clear error handling
- Dependency-free implementation
- No packet crafting or exploitation

## Examples

```bash
dnsforge example.com
dnsforge example.com --type MX --json
dnsforge 8.8.8.8 --reverse
```

Use it only against infrastructure you are authorized to inspect.

## Workflow

```text
hostname / address
       ↓
 DNS query
       ↓
 resolver response
       ↓
 formatted diagnostics
```

JSON output can be consumed by scripts and other defensive tooling.

## Development

Run the repository test suite before making releases or submitting changes.

## Responsible use

DNSForge is intended for diagnostics, troubleshooting, labs and authorized security work. It does not provide exploitation functionality.

## License

MIT. See [`LICENSE`](LICENSE).

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
