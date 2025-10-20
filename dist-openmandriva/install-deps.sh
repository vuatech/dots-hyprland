DEPS=(
    illogical-impulse
    starship
    wtype
)

install_packaging_tools() {
    showfun "sudo dnf install -y packaging-tools"
    sudo dnf install -y packaging-tools
    command -v abb >/dev/null || { err "abb still missing after install"; return 1; }
    log "Packaging tools installed."
}
v install_packaging_tools

install_build_deps() {
    for proj in "${DEPS[@]}"; do
        local spec="${proj}/${proj}.spec"
        [[ -f "$spec" ]] || { err "Spec not found: $spec"; continue; }
        log "Installing build-deps for $proj ..."
        showfun "sudo dnf builddep -y \"$spec\""
        sudo dnf builddep -y "$spec"
    done
}
v install_build_deps

build_project() {
    local proj="$1"
    local dir="${proj}"
    local spec="${proj}/${proj}.spec"

    [[ -d "$dir" ]]   || { err "Directory missing: $dir"; return 1; }
    [[ -f "$spec" ]]  || { err "Spec missing: $spec"; return 1; }

    log "Building $proj (local to $dir) ..."

    showfun "cd \"$dir\" && abb build"
    (
        cd "$dir" || exit 1
        abb build
    )
}
build_all() {
    for proj in "${DEPS[@]}"; do
        build_project "$proj"
    done
}
v build_all

install_built_rpms() {
    for proj in "${DEPS[@]}"; do
        local rpm_dir="${proj}/RPMS"
        [[ -d "$rpm_dir" ]] || { warn "No RPMS dir for $proj – skipping install"; continue; }

        mapfile -d '' rpms < <(find "$rpm_dir" -type f -name "*.rpm" ! -name "*.src.rpm" -print0)
        (( ${#rpms[@]} )) || { warn "No binary RPMs for $proj"; continue; }

        log "Installing ${#rpms[@]} binary package(s) for $proj ..."
        local rpm_list=""
        for r in "${rpms[@]}"; do rpm_list+=" \"$r\""; done
        sudo dnf install "${rpms[@]}"
    done
}
v install_built_rpms

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # Script is being executed → run the whole pipeline
    install_packaging_tools
    install_build_deps
    build_all
    install_built_rpms
    log "All projects processed successfully."
fi
