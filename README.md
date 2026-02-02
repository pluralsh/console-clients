# Plural REST API Clients

REST API clients for the Plural Console, generated from the [OpenAPI specification](openapi.json) in the repository root.

## Available Clients

| Language                     | Package                                 | Directory                  | Example                                      |
| ---------------------------- | --------------------------------------- | -------------------------- | -------------------------------------------- |
| **Go** (1.21+)               | `github.com/pluralsh/console-client-go` | [go/](go/)                 | [examples/go/](examples/go/)                 |
| **TypeScript** (Node.js 20+) | `@pluralsh/console-client`              | [typescript/](typescript/) | [examples/typescript/](examples/typescript/) |
| **Python** (3.8+)            | `pluralsh-console-client`               | [python/](python/)         | [examples/python/](examples/python/)         |

### Generate Clients

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

## Requirements

- **Go**: Go 1.21+
- **TypeScript**: Node.js 20+
- **Python**: Python 3.8+

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
