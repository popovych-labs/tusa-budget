.PHONY: run

run:
	uvicorn --factory backend.src.main:app_factory --reload --reload-include *.html --reload-include *.js --log-level debug