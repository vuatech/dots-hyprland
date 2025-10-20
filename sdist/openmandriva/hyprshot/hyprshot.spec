%global debug_package %{nil}

Name:		hyprshot
Version:	1.3.0
Release:	1
Source0:	https://github.com/Gustash/Hyprshot/archive/%{version}/%{name}-%{version}.tar.gz
Summary:	Hyprshot is an utility to easily take screenshots in Hyprland using your mouse.
URL:		https://github.com/Gustash/Hyprshot
License:	GPLv3
Group:		Window Manager/Hyprland/Screenshot

%description
%summary

%prep
%autosetup -p1 -n Hyprshot-%{version}

%install
install -d %{buildroot}%{_bindir}
install -Dm0775 hyprshot %{buildroot}%{_bindir}

%files
%license LICENSE
%{_bindir}/%{name}
