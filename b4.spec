Summary:	A tool to work with public-inbox and patch archives
Summary(pl.UTF-8):	Narzędzie do pracy z publiczną skrzynką odbiorczą i archiwami łatek
Name:		b4
Version:	0.5.2
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	https://www.kernel.org/pub/software/devel/b4/%{name}-%{version}.tar.xz
# Source0-md5:	7a11412bc4f4e80d3611df95aa9c8ab8
URL:		https://git.kernel.org/pub/scm/utils/b4/b4.git
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a helper utility to work with patches made available via a
public-inbox archive like lore.kernel.org. It is written to make it
easier to participate in a patch-based workflows, like those used in
the Linux kernel development.

%description -l pl.UTF-8
Narzędzie pomocnicze do pracy z łatkami dostępnymi przez archiwum
publicznej skrzynki odbiorczej, takie jak lore.kernel.org. Zostało
napisane, aby ułatwić uczestniczenie w stylu pracy opartym na łatkach,
jak ten używany przy rozwijaniu jądra Linuksa.

%prep
%setup -q

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/b4
%{py3_sitescriptdir}/b4
%{py3_sitescriptdir}/b4-%{version}-py*.egg-info
