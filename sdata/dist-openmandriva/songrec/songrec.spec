%global debug_package %{nil}

Name:		songrec
Version:	0.4.3
Release:	1
Source0:	https://github.com/marin-m/SongRec/archive/%{version}/%{name}-%{version}.tar.gz
Summary:	An open-source Shazam client for Linux, written in Rust.
URL:		https://github.com/marin-m/SongRec
License:	GPLv3
Group:		?
BuildRequires:	cargo

%description
%summary

%prep
%autosetup -p1 -n SongRec-%{version}

%build
cargo build --release

%install
install -Dm755 target/release/songrec %{buildroot}%{_bindir}/songrec
install -Dm755 packaging/rootfs/usr/share/applications/com.github.marinm.songrec.desktop %{buildroot}%{_datadir}/applications/com.github.marinm.songrec.desktop
install -Dm755 packaging/rootfs/usr/share/icons/hicolor/scalable/apps/com.github.marinm.songrec.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/com.github.marinm.songrec.svg
install -Dm755 packaging/rootfs/usr/share/metainfo/com.github.marinm.songrec.metainfo.xml %{buildroot}%{_datadir}/metainfo/com.github.marinm.songrec.metainfo.xml
install -d 644 %{buildroot}%{_datadir}/%{name}/translations
cp -ra translations %{buildroot}%{_datadir}/%{name}/translations

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/com.github.marinm.songrec.desktop
%{_datadir}/songrec
%{_iconsdir}/hicolor/scalable/apps/com.github.marinm.songrec.svg
%{_datadir}/metainfo/com.github.marinm.songrec.metainfo.xml
