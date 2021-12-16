SRC = $(wildcard ./*.ipynb)

build: $(SRC)
	nbdev_build_lib
	touch netdata-pandas

version: $(SRC)
	nbdev_bump_version

netdata-pandas: $(SRC)
	nbdev_build_lib
	touch netdata-pandas

docs_serve: docs
	cd docs && bundle exec jekyll serve

docs: $(SRC)
	nbdev_build_docs
	touch docs

test:
	nbdev_test_nbs

bump:
	nbdev_bump_version

release: pypi
	nbdev_bump_version

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist
    
release_on_windows:
	nbdev_build_lib
	nbdev_build_docs
	nbdev_test_nbs
	rmdir /s dist
	python setup.py sdist bdist_wheel
	twine upload --repository pypi dist/*
	nbdev_bump_version

all:
	nbdev_build_lib
	nbdev_build_docs
	nbdev_test_nbs
	rm -rf dist
	python setup.py sdist bdist_wheel
	twine upload --repository pypi dist/*
	nbdev_bump_version
