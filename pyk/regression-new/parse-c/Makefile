DEF=c18-translation
EXT=kc
TESTDIR=.
KOMPILE_FLAGS+=--bison-lists --gen-glr-bison-parser
test: test.kore
	$(KPRINT) c18-translation-kompiled test.kore | diff - test.ref

test.kore: test.c kompile
	./c18-translation-kompiled/parser_PGM test.c > test.kore
include ../include/ktest.mak

clean:
	rm -rf test.kore c18-translation-kompiled


KRUN=./cparse
