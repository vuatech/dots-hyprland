%global debug_package %{nil}

Name:		darkly
Version:	0.5.23
Release:	1
Source0:	https://github.com/Bali10050/darkly/archive/v%{version}/%{name}-v%{version}.tar.gz
Summary:	A modern style for qt applications
URL:		https://github.com/Bali10050/darkly
License:	GPLv2
Group:		Desktop Environment/KDE/Style

BuildSystem:	cmake

BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(KF5FrameworkIntegration)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6ColorScheme)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6KirigamiPlatform)
BuildRequires:	cmake(KDecoration3)
BuildRequires:	cmake(KF6FrameworkIntegration)
BuildRequires:	cmake(Qt6QmlCompiler)


%description
A modern style for qt applications.

%prep
%autosetup -p1 -n Darkly-%{version}

%files
%{_bindir}/darkly-settings6
%{_libdir}/cmake/Darkly/DarklyConfig.cmake
%{_libdir}/cmake/Darkly/DarklyConfigVersion.cmake
%{_libdir}/plugins/kstyle_config/darklystyleconfig.so
%{_libdir}/plugins/org.kde.kdecoration3.kcm/kcm_darklydecoration.so
%{_libdir}/plugins/org.kde.kdecoration3/org.kde.darkly.so
%{_libdir}/plugins/styles/darkly5.so
%{_libdir}/plugins/styles/darkly6.so
%{_datadir}/applications/darklystyleconfig.desktop
%{_datadir}/applications/kcm_darklydecoration.desktop
%{_datadir}/color-schemes/Darkly.colors
%{_iconsdir}/hicolor/scalable/apps/darkly-settings.svgz
%{_datadir}/kservices6/darklydecorationconfig.desktop
%{_datadir}/kstyle/themes/darkly.themerc
