.PHONY: generate generate-go generate-typescript generate-python

generate: generate-go generate-typescript generate-python
	@echo "✓ All clients generated successfully"

generate-go:
	@echo "Generating Go client..."
	@$(MAKE) -C go generate

generate-typescript:
	@echo "Generating TypeScript client..."
	@$(MAKE) -C typescript generate

generate-python:
	@echo "Generating Python client..."
	@$(MAKE) -C python generate
