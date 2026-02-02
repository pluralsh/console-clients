# Go example

Minimal example that calls the `/me` endpoint.

## Setup

The module lives in a subdirectory, so add it with the tag that includes the prefix:

```bash
go get github.com/pluralsh/rest-clients/go@go/v0.0.0
go mod tidy
```

If you get 404 from the Go proxy (tag just pushed or private repo), fetch directly:

```bash
GOPRIVATE=github.com/pluralsh/* go get github.com/pluralsh/rest-clients/go@go/v0.0.0
go mod tidy
```

## Run

From this directory:

```bash
go run .
```

Set `CONSOLE_URL` and `CONSOLE_TOKEN` via env vars (e.g. `CONSOLE_TOKEN=your-token`). Default URL is `https://console.plrl-dev-aws.onplural.sh`.
