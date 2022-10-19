Name: ruya-kcalc
Version: 1
Release: 1%{?dist}
Summary: Custumize build of Kcalc for RuyaOS
License: GPLv3
URL: https://parmg.sa
Source0: LICENSE
Source1: org.kde.kcalc.desktop
BuildArch: noarch

%description
Custumize build of Kcalc for RuyaOS

%prep
cp %{SOURCE0} .

%install
mkdir -p %{buildroot}/usr/local/share/applications
install -Dp -m 0644 %{SOURCE1} %{buildroot}/usr/local/share/applications

%files
%license LICENSE
/usr/local/share/applications/org.kde.kcalc.desktop

%changelog
* Wed Oct 19 2022 Mosaab Alzoubi <mosaab[AT]parmg[DOT]sa> - 1-1
- Initial
