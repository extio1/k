from functools import partial
from typing import Final, Tuple
from unittest import TestCase

from ..cterm import CTerm
from ..kast import KApply, KInner, KVariable

a, b, c = (KApply(label) for label in ['a', 'b', 'c'])
x, y, z = (KVariable(name) for name in ['x', 'y', 'z'])
f, g, h = (partial(KApply.of, label) for label in ['f', 'g', 'h'])


def _as_cterm(term: KInner) -> CTerm:
    return CTerm(KApply('<k>', [term]))


class CTermTest(TestCase):

    def test_cterm_match_and_subst(self):
        # Given
        TEST_DATA: Final[Tuple[Tuple[KInner, KInner], ...]] = (
            (a, a),
            (a, x),
            (f(a), x),
            (f(a), f(a)),
            (f(a), f(x)),
            (f(a, b), f(x, y)),
            (f(a, b, c), f(x, y, z)),
            (f(g(h(a))), f(x)),
            (f(g(h(x))), f(x)),
            (f(a, g(b, h(c))), f(x, y)),
        )

        for i, [term, pattern] in enumerate(TEST_DATA):
            with self.subTest(i=i):
                # When
                subst_cterm = _as_cterm(pattern).match(_as_cterm(term))

                # Then
                self.assertIsNotNone(subst_cterm)
                self.assertEqual(subst_cterm(pattern), term)

    def test_no_cterm_match(self):
        # Given
        TEST_DATA: Final[Tuple[Tuple[KInner, KInner], ...]] = (
            (f(x, x), f(x, a)),
        )

        for i, [term, pattern] in enumerate(TEST_DATA):
            with self.subTest(i=i):
                # When
                subst_cterm = _as_cterm(pattern).match(_as_cterm(term))

                # Then
                self.assertIsNone(subst_cterm)
