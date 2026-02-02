# Run from repo root: make -C python generate
# Or from python/: make generate
.PHONY: generate clean

REPO_ROOT ?= ..
OPENAPI_JSON ?= $(REPO_ROOT)/openapi.json

generate: clean
	python3 -m openapi_python_client generate --path $(OPENAPI_JSON) --meta none --overwrite

clean:
	rm -rf plural_rest_api_client

install:
	pip install -e ".[dev]"
