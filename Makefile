.PHONY: all dist clean publish

all: dist

dist:
	python3 setup.py sdist

publish: dist
	twine upload dist/*

clean:
	rm -rf build dist
