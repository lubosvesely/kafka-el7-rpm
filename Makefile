tarball:
	spectool -g kafka.spec
	tar cvf downstream.tar $(shell git ls-tree --name-only HEAD)
