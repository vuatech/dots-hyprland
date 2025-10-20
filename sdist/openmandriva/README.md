# Install scripts for Open Mandriva
- See also [Install scripts | illogical-impulse](https://ii.clsty.link/en/dev/inst-script/) #Soon

## Current Dependency Installation
Local Specs under `./dist-openmandriva/` are used to install dependencies.

The mechanism is introduced by [Makrennel](https://github.com/Makrennel) in [PR#570](https://github.com/end-4/dots-hyprland/pull/570).

Why is this awesome?
- It makes it possible to control version since some packages may involve breaking changes from time to time.
- It makes the dependency trackable for package manager, so that you always know why you have installed some package.
- As a result, it enables a workable `uninstall.sh` script.

The Spec files contains two forms of dependencies:
- Package name written in dependencies, like a "meta" package.
- Normal Spec files content to build dependencies, e.g. wtype, which does not meet packaging guidelines.
