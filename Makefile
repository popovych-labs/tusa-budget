.PHONY: run

run:
	uvicorn --factory backend.src.main:app_factory --reload --reload-include *.html --reload-include *.js --log-level debug





compose-up:
	docker compose 	--env-file .\dev.env up

compose-down:
	docker compose 	--env-file .\dev.env down

compose-stop:
	docker compose 	--env-file .\dev.env stop