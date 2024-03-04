.PHONY: all dist clean publish

all: dist

dist:
	python3 kadmin/setup.py sdist && python3 kadmin_local/setup.py sdist

publish:
	twine upload dist/*

clean:
	rm -rf build dist
