dnos-kdev: Kernel tool for dnos

This run kernel debug tools inside a docker container

Options:
--------

-h, --help                      Show this message
-n, --dry-run                   Just print what would be done
-r, --ssh-remote HOST           SSH destination (dnos port 2222)
-s, --sourcedir SRC             Kernel source dir (only for kpatch)
--use-linux-source-package      Set --sourcedir to unpacked source in /usr/src/
--extra-args-docker ARGS        Extra arguments for docker run
--extra-args-stap ARGS          Extra arguments for stap
--extra-args-staprun ARGS       Extra arguments for staprun
--extra-args-stapmod ARGS       Extra arguments for stap module
--use-ubuntu-stap               Use ubuntu /usr/bin/stap inside docker
--use-upstream-stap             Use upstream /usr/local/bin/stap inside docker.
    This requires updated staprun on remote target
-u, --match-uidgid              Match current uid/gid
--focal                         Use ubuntu focal 20.04
--bionic                        Use ubuntu focal 18.04

Subcommands:
------------

run
    Run shell command inside the container (default is interactive shell)
stap
    Run stap in container with correct -r argument
remote-staprun
    Build stap.ko inside container and run on --ssh-remote
kpatch-build
    Run kpatch-build inside the container
prepare-source
    Prepare kernel given via --sourcedir

Default is to run an interactive shell inside the container.

Subcommands will automatically receive "correct" arguments to reference the
target kernel so `stap` is equivalent to `run stap -r `.

The current working directory is mounted inside the docker container (at
/mnt/cwd) so path references under ./ usually work but not externally.
