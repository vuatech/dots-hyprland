%global debug_package %{nil}

Name:		wtype
Version:	0.4
Release:	1
Source0:	https://github.com/atx/wtype/archive/v%{version}/%{name}-v%{version}.tar.gz
Summary:	xdotool type for wayland
URL:		https://github.com/atx/wtype
License:	MIT
Group:		Window Manager/Utility
BuildRequires:	meson
BuildSystem:	meson

%description
%summary.
%prep
%autosetup -p1

%files
%{_bindir}/%{name}
%{_mandir}/man1/wtype.1.zst
