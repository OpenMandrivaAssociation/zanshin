Name:           zanshin
Version:        0.5.0
Release:        2
Summary:        Getting Things Done application
Group:          Graphical desktop/KDE
License:        GPLv2+ and LGPLv2+
URL:            https://zanshin.kde.org
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Recommends:     renku

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiCalendar)
BuildRequires:  cmake(KF5AkonadiNotes)
BuildRequires:  cmake(KF5AkonadiSearch)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5KontactInterface)
BuildRequires:  cmake(KF5Ldap)
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
%doc AUTHORS COPYING COPYING.LIB HACKING TODO
%{_kde5_bindir}/%{name}
%{_kde5_bindir}/%{name}-migrator
%{_qt5_plugindir}/kontact_zanshinplugin.so
%{_qt5_plugindir}/krunner_zanshin.so
%{_qt5_plugindir}/zanshin_part.so
%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_kde5_applicationsdir}/org.kde.%{name}.desktop
%{_kde5_datadir}/kxmlgui5/%{name}/
%{_kde5_services}/kontact/zanshin_plugin.desktop
%{_kde5_services}/plasma-runner-zanshin.desktop
%{_kde5_services}/zanshin_part.desktop
%{_kde5_iconsdir}/hicolor/*/apps/%{name}.*

%package -n renku
Summary:        Note taking application
Group:          Graphical desktop/KDE
Recommends:     %{name}

%description -n renku
A note taking application which aims at getting your mind like water.

%files -n renku
%{_kde5_bindir}/renku
%{_qt5_plugindir}/kontact_renkuplugin.so
%{_qt5_plugindir}/renku_part.so
%{_datadir}/metainfo/org.kde.renku.appdata.xml
%{_kde5_applicationsdir}/org.kde.renku.desktop
%{_kde5_datadir}/kxmlgui5/renku/
%{_kde5_services}/kontact/renku_plugin.desktop
%{_kde5_services}/renku_part.desktop
%{_kde5_iconsdir}/hicolor/*/apps/renku.*

#---------------------------------------------------------------))


%prep
%setup -q
%apply_patches

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

%find_lang %{name}

# Make a copy of the icons for renku, to make them installable separately
for file in %{buildroot}%{_kde5_iconsdir}/hicolor/*/apps/%{name}.png; do
  cp $file "$(dirname $file)/renku.png"
done
cp %{buildroot}%{_kde5_iconsdir}/hicolor/scalable/apps/{%{name},renku}.svgz
sed -i 's/Icon=zanshin/Icon=renku/' %{buildroot}%{_kde5_applicationsdir}/org.kde.renku.desktop

