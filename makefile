BUILD_DEBUG ?= yes
.PHONY: update
version: ;@echo $(MAKE_VERSION) ; uname -a ; python -V ; perl -v
elf: ;@echo "--------------MAKING EXECUTABLES-------------";chmod +x *.sh
update: ;./update.sh ; sleep 3 ; ./clean.sh
hashes: ;@echo "-----------HASHES------------";echo "------------HASHES-----------" > hashes.txt;./generate_hashes.sh >> hashes.txt
tar: ;tar -cvf scripts.tar *.sh *.py *.pl
push: ;@echo "-------------GIT-PUSH-------------";./git-push.sh Scripts
