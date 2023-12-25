#!/bin/bash -eEu

pip install -U kubernator==1.0.9

cat <<'EOF'

***************************************
PHASE 1
***************************************

EOF
TEST_PHASE=1 kubernator -v TRACE apply --yes

cat <<'EOF'

***************************************
PHASE 2
***************************************

EOF
TEST_PHASE=2 kubernator -v TRACE apply --yes