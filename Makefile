install:
	@read -p "requirements.txt file: " file ; \
	pip install -r file

build:
	python -m build

upload: repo
	@read -p "Repo: " repo ; \
	twine upload dist/* -r $$repo --config-file .pypirc

clean:
	rm -rf __pycache__