

.PHONY: test-python
test-python: ## Run tests quickly with the default Python
	docker-compose up -d
	python -m pytest tests

.PHONY: test-helm
test-helm: ## Run tests quickly with the default Helm
	minikube start
	eval $(minikube docker-env)
	docker build -t icon-exporter-local
	cd tests
	go test .


.PHONY: test
test: test-python test-helm


.PHONY: clean-build
clean-build: ## Remove build artifacts
	@echo "+ $@"
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info
	@rm -fr *.pytest_cache

.PHONY: clean-pyc
clean-pyc: ## Remove Python file artifacts
	@echo "+ $@"
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.py[co]' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +

.PHONY: clean
clean: clean-build clean-pyc ## Remove all file artifacts
