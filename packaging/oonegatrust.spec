Name:           oonegatrust
Version:        0.1.0
Release:        1%{?dist}
Summary:        Default-deny sandbox runner isolating stdin, stdout, and network interfaces.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oonegatrust
Source0:        oonegatrust-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oonegatrust is a sovereign, capability-bounded NEGATIVE TRUST written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oonegatrust
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oonegatrust-uninstall

%files
/usr/bin/oonegatrust
/usr/bin/oonegatrust-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
