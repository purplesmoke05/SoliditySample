.PHONY: compile test

compile:
	poetry run brownie compile

test:
	poetry run brownie test
