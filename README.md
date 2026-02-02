# Plural REST API Clients

REST API clients for the Plural Console, generated from the [OpenAPI specification](openapi.json) in the repository root.

## Available Clients

### Go

- **Requirements:** Go 1.21+
- **Package:** `github.com/pluralsh/rest-clients/go`
- **Directory:** [go/](go/)
- **Example:** [examples/go/](examples/go/)

### Python

- **Requirements:** Python 3.8+
- **Package:** `pluralsh-console-client`
- **Directory:** [python/](python/)
- **Example:** [examples/python/](examples/python/)

### TypeScript

- **Requirements:** Node.js 20+
- **Package:** `@pluralsh/console-client`
- **Directory:** [typescript/](typescript/)
- **Example:** [examples/typescript/](examples/typescript/)

## Generate Clients

Run from the repository root:

```bash
# All available clients
make generate

# Go
make -C go generate

# Python
make -C python generate

# TypeScript
make -C typescript generate
```

## Repository Structure

```
.
├── openapi.json          # OpenAPI specification
├── go/                   # Go client
├── typescript/           # TypeScript client
├── python/               # Python client
└── examples/             # Example applications
    ├── go/
    ├── typescript/
    └── python/
```
