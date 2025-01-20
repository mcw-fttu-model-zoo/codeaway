#/bin/bash

set -eo pipefail


main() {
    env pytest models
}

main "$@"
