.PHONY: run

run:
	uvicorn --factory backend.src.main:app_factory --host 0.0.0.0 --reload --reload-dir backend --reload-include *.html --log-level debug

tailwind:
	tailwindcss -i frontend\_tailwind.css -o frontend\style.css --watch




compose-up:
	docker compose 	--env-file .\dev.env up

compose-down:
	docker compose 	--env-file .\dev.env down

compose-stop:
	docker compose 	--env-file .\dev.env stop

compose-rm:
	docker compose 	--env-file .\dev.env rm