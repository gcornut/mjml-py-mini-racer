

install:
	pip-compile && pip-sync
	cd mjml-lib; npm install

build:
	(cd mjml-lib; npm run build)
	python -m build