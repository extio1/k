// Copyright (c) Runtime Verification, Inc. All Rights Reserved.
package org.kframework.compile;

import org.kframework.attributes.Att;
import org.kframework.definition.Module;
import org.kframework.definition.Rule;
import org.kframework.definition.Sentence;

/**
 * Propagate macro, macro-rec, alias, and alias-rec labels from productions to rules that only
 * contain that klabel on the LHS This prepares rules for macro expansion in ExpandMacros. There is
 * one exception: simplification rules are meant to be used for the haskell backend and macros
 * should not be propagated to these rules.
 */
public record PropagateMacro(Module m) {

  public Sentence propagate(Sentence s) {
    if (s instanceof Rule
        && m.ruleLhsHasMacroKLabel((Rule) s)
        && !s.att().contains(Att.SIMPLIFICATION())) {
      Att macroAtt = m.attributesFor().apply(m.matchKLabel((Rule) s));
      return Rule.apply(
          ((Rule) s).body(),
          ((Rule) s).requires(),
          ((Rule) s).ensures(),
          s.att().add(macroAtt.getMacro().get()));
    }
    return s;
  }
}
