dnos-kdev: Kernel tool for dnos

This run kernel debug tools inside a docker container

Options:
--------

-h, --help                      Show this message
-n, --dry-run                   Just print what would be done
-r, --ssh-remote HOST           SSH destination (dnos port 2222)
--extra-args-docker ARGS        Extra arguments for docker run
--extra-args-stap ARGS          Extra arguments for stap
--extra-args-staprun ARGS       Extra arguments for staprun
--extra-args-stapmod ARGS       Extra arguments for stap module

Subcommands:
------------

run
    Run shell command inside the container (default is interactive shell
remote-staprun
    Build stap.ko inside container and run on --ssh-remote
kpatch-build
    Run kpatch-build inside the container

Default is to run an interactive shell
