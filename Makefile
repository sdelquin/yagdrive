build:
	python setup.py sdist bdist_wheel

clean:
	rm -fr build istacpy.egg-info dist

test-publish:
	twine upload --repository testpypi dist/*

publish:
	twine upload dist/*
