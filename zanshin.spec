%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:           zanshin
Version:        23.08.4
Release:        2
Summary:        Getting Things Done application
Group:          Graphical desktop/KDE
License:        GPLv2+ and LGPLv2+
URL:            https://zanshin.kde.org
%if 0%{?git}
Source0:	https://invent.kde.org/plasma-mobile/plasma-angelfish/-/archive/v%{version}/plasma-angelfish-v%{version}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiCalendar)
BuildRequires:  cmake(KPim5AkonadiNotes)
BuildRequires:  cmake(KPim5AkonadiSearch)
BuildRequires:  cmake(KPim5IdentityManagement)
BuildRequires:  cmake(KPim5KontactInterface)
BuildRequires:  cmake(KPim5Ldap)
BuildRequires:  cmake(KF5Runner)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
A Getting Things Done application which aims at getting your mind like water.

%files -f %{name}.lang
%{_bindir}/zanshin
%{_bindir}/zanshin-migrator
%{_libdir}/qt5/plugins/kf5/krunner/org.kde.zanshin.so
%{_libdir}/qt5/plugins/pim5/kontact/kontact_zanshinplugin.so
%{_libdir}/qt5/plugins/zanshin_part.so
%{_datadir}/applications/org.kde.zanshin.desktop
%{_datadir}/icons/hicolor/*/apps/zanshin.*
%{_datadir}/kxmlgui5/zanshin/zanshin_part.rc
%{_datadir}/metainfo/org.kde.zanshin.metainfo.xml

#---------------------------------------------------------------


%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name}
