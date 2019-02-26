
#!/bin/sh

echo "Balandroid v2.0 By Kevin N. Omyonga"

SCRIPT_PATH="./scripts/setup.sh"

read -r -p "Begin the setup?[y/N] " choice
case "$choice" in
[yY][eE][sS]|[yY])
source "$SCRIPT_PATH"
;;
*)
echo "Program Terminated"
;;
esac

