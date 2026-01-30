# console-client-go

Go REST client for the [Plural Console](https://plural.sh) API. Generated from the OpenAPI spec using [oapi-codegen](https://github.com/oapi-codegen/oapi-codegen).

## Installation

```bash
go get github.com/pluralsh/console-client-go
```

## Usage

```go
package main

import (
	"context"
	"net/http"

	"github.com/pluralsh/console-client-go/client"
)

func main() {
	baseURL := "https://your-console.example.com"
	httpClient := &http.Client{}
	c, err := client.NewClient(baseURL, client.WithHTTPClient(httpClient))
	if err != nil {
		panic(err)
	}

	// Add auth (e.g. Bearer token) via a custom client
	authClient := &http.Client{
		Transport: &roundTripper{
			base: http.DefaultTransport,
			header: http.Header{"Authorization": []string{"Bearer YOUR_TOKEN"}},
		},
	}
	c, _ = client.NewClient(baseURL, client.WithHTTPClient(authClient))

	ctx := context.Background()
	resp, err := c.ListClusters(ctx)
	// ...
}

type roundTripper struct {
	base   http.RoundTripper
	header http.Header
}

func (r *roundTripper) RoundTrip(req *http.Request) (*http.Response, error) {
	for k, v := range r.header {
		req.Header[k] = v
	}
	return r.base.RoundTrip(req)
}
```

All API operations and types are in package `client`. Use your editor’s autocomplete to discover methods and types.

## Regenerating the client

When `openapi.json` in the repo root changes, from this directory:

```bash
cd go
go run github.com/oapi-codegen/oapi-codegen/v2/cmd/oapi-codegen@v2.4.0 -config config.yaml ../openapi.json
go mod tidy
go build ./...
```

Or from the repo root: `make -C go generate`.

## Requirements

- Go 1.21+
