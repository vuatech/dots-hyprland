log()   { printf '\e[32m[LOG]\e[0m %s\n' "$@"; }
warn()  { printf '\e[33m[WARN]\e[0m %s\n' "$@" >&2; }
err()   { printf '\e[31m[ERROR]\e[0m %s\n' "$@" >&2; return 1; }

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
REPO_ROOT="$( cd "$SCRIPT_DIR/../.." >/dev/null 2>&1 && pwd )"
BUILD_BASE="${REPO_ROOT}/sdist/openmandriva"

DEPS=(
    starship
    breeze-plus
    fonts-oft-space-grotesk
    fonts-ttf-gabarito-git
    fonts-ttf-material-symbols-variable-git
    fonts-ttf-readex-pro
    fonts-ttf-rubik-vf
    fonts-ttf-twemoji
    wtype
    hyprshot
    darkly
    illogical-impulse
)

install_packaging_tools() {
    x sudo dnf install -y packaging-tools
    x command -v abb >/dev/null || { err "abb still missing after install"; return 1; }
    x log "Packaging tools installed."
}
showfun install_packaging_tools
v install_packaging_tools

install_build_deps() {
    for proj in "${DEPS[@]}"; do
        local spec="${BUILD_BASE}/${proj}/${proj}.spec"
        local dir="${BUILD_BASE}/${proj}"
        [[ -f "$spec" ]] || { err "Spec not found: $spec"; continue; }
        log "Installing build-deps for $proj ..."
        x sudo dnf builddep -y "$spec"
    done
}
showfun install_build_deps
v install_build_deps

build_all() {
    for proj in "${DEPS[@]}"; do
        local spec="${BUILD_BASE}/${proj}/${proj}.spec"
        local dir="${BUILD_BASE}/${proj}"
        [[ -f "$spec" ]] || { err "Spec not found: $spec"; continue; }
        log "Building $proj ..."
        x cd "$dir"
        x abb build
    done
}
showfun build_all
v build_all

install_or_reinstall_rpms() {
    local rpms=( "$@" )
    (( ${#rpms[@]} )) || { warn "No RPMs passed to install_or_reinstall_rpms – skipping."; return 0; }

    local pkg_names=()
    for r in "${rpms[@]}"; do
        local name
        name=$(rpm -qp --queryformat '%{NAME}' "$r" 2>/dev/null) \
            || { err "Failed to query package name for $r"; return 1; }
        pkg_names+=( "$name" )
    done

    local to_install=()
    local to_reinstall=()
    for i in "${!pkg_names[@]}"; do
        local pkg="${pkg_names[i]}"
        local rpm_file="${rpms[i]}"

        if rpm -q --quiet "$pkg" 2>/dev/null; then
            to_reinstall+=( "$rpm_file" )
            log "Package $pkg already installed – will reinstall."
        else
            to_install+=( "$rpm_file" )
            log "Package $pkg not installed – will install."
        fi
    done

    local rc=0

    if (( ${#to_install[@]} )); then
        log "Installing ${#to_install[@]} new package(s)..."
        if ! sudo dnf install -y "${to_install[@]}"; then
            err "dnf install failed for new packages."
            rc=1
        fi
    fi

    if (( ${#to_reinstall[@]} )); then
        log "Re-installing ${#to_reinstall[@]} existing package(s)..."
        if ! sudo dnf reinstall -y "${to_reinstall[@]}"; then
            err "dnf reinstall failed for existing packages."
            rc=1
        fi
    fi

    return $rc
}

install_built_rpms() {
    local failed=0

    for proj in "${DEPS[@]}"; do
        local rpm_dir="${BUILD_BASE}/${proj}/RPMS"
        [[ -d "$rpm_dir" ]] || { warn "No RPMS dir for $proj – skipping install"; continue; }

        # Gather all binary RPMs (exclude .src.rpm)
        mapfile -d '' rpms < <(find "$rpm_dir" -type f -name "*.rpm" ! -name "*.src.rpm" -print0)
        (( ${#rpms[@]} )) || { warn "No binary RPMs for $proj – skipping install"; continue; }

        log "Found ${#rpms[@]} RPM(s) for $proj – deciding install/reinstall..."

        printf "\n=== Next command: install_or_reinstall_rpms for %s ===\n" "$proj"
        read -p "Execute? (y/e/s/yesforall) [y]: " ans
        case "$ans" in
            ""|y|Y) ;;
            e|E) err "User aborted."; return 1;;
            s|S) warn "Skipping install for $proj (not recommended)"; continue;;
            yesforall|YESFORALL) export YESFORALL=1 ;;
            *) warn "Invalid answer – treating as skip."; continue;;
        esac

        if [[ $YESFORALL == 1 ]]; then
            log "YESFORALL active – auto-running install/reinstall for $proj"
        fi

        if ! install_or_reinstall_rpms "${rpms[@]}"; then
            err "Failed to install/reinstall RPMs for $proj"
            ((failed++))
        else
            log "$proj RPMs processed successfully."
        fi
    done

    (( failed == 0 )) && log "All built RPMs installed/reinstalled." || err "$failed project(s) failed to install."
    return $(( failed != 0 ))
}
showfun install_built_rpms
v install_built_rpms

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # Script is being executed → run the whole pipeline
    install_packaging_tools
    install_build_deps
    build_all
    install_built_rpms
    log "All projects processed successfully."
fi
