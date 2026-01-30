# Run from repo root: make -C go generate
# Or from go/: make generate
.PHONY: generate

REPO_ROOT ?= ..
OPENAPI_JSON ?= $(REPO_ROOT)/openapi.json

generate:
	go run github.com/oapi-codegen/oapi-codegen/v2/cmd/oapi-codegen@v2.4.0 -config config.yaml $(OPENAPI_JSON)
	go mod tidy
