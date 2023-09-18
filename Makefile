.PHONY: run

run:
	uvicorn --factory backend.src.main:app_factory --host 0.0.0.0 --reload --reload-dir backend --reload-include *.html --log-level debug

tailwind:
	npx tailwindcss -i frontend\_tailwind.css -o frontend\style.css --watch




compose-up:
	docker compose 	--env-file .\dev.env up

compose-down:
	docker compose 	--env-file .\dev.env down

compose-stop:
	docker compose 	--env-file .\dev.env stop

compose-rm:
	docker compose 	--env-file .\dev.env rm


docker-build:
	docker build --target prod -f .\docker\Dockerfile -t tusa_budget .

docker-run:
	docker run --rm -it -p 3000:3000 --name tusa_budget tusa_budget

docker-run-bash:
	docker run --rm -it --name tusa_budget tusa_budget /bin/sh