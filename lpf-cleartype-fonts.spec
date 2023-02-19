Name:           lpf-cleartype-fonts
Version:        1.0
Release:        4%{?dist}
Summary:        Bootstrap package building cleartype-fonts using lpf

License:        MIT
URL:            https://github.com/leamas/lpf
Group:          Development/Tools
BuildArch:      noarch
Source0:        cleartype-fonts.spec.in
Source1:        eula.txt
Source2:        61-cleartype-calibri.conf
Source3:        61-cleartype-cambria.conf
Source4:        61-cleartype-candara.conf
Source5:        61-cleartype-consolas.conf
Source6:        61-cleartype-constantia.conf
Source7:        61-cleartype-corbel.conf

BuildRequires:  desktop-file-utils
BuildRequires:  lpf
Requires:       lpf

%global         target_pkg %(t=%{name}; echo ${t#lpf-})


%description
Bootstrap package allowing the lpf system to build the
cleartype-fonts non-redistributable package.


%prep
%setup -cT


%build


%install
# lpf-setup-pkg [-e eula] <topdir> <specfile> [sources...]
/usr/share/lpf/scripts/lpf-setup-pkg -e %{SOURCE1} %{buildroot} %{SOURCE0} \
    %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7}


%post
%lpf_post

%postun
%lpf_postun

%lpf_triggerpostun


%files
%{_datadir}/applications/%{name}.desktop
%{_datadir}/lpf/packages/%{target_pkg}
%attr(775,pkg-build,pkg-build) /var/lib/lpf/packages/%{target_pkg}


%changelog
* Sun Feb 19 2023 Leigh Scott <leigh123linux@gmail.com> - 1.0-4
- Bump

* Sun Nov 07 2021 Sérgio Basto <sergio@serjux.com> - 1.0-3
- retag it again

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 14 2014 Alec Leamas <leamas.alec@gmail.com> - 1.0-1
- New target spec: Updated description, lower config prio.

* Mon Feb 10 2014 Alec Leamas <leamas.alec@gmail.com> - 1.0-1
- Initial release
