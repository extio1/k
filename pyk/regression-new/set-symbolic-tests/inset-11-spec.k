// Copyright (c) Runtime Verification, Inc. All Rights Reserved.
// generated by gen-tests.sh

requires "set-tests.k"

module INSET-11-SPEC
    imports SET-TESTS

    claim <k> inSet ( Y:MyId in ( SetItem(Z:MyId) SET:Set SetItem(X:MyId) ) ) => . </k>

endmodule
