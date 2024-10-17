Name:		texlive-euflag
Version:	55265
Release:	2
Summary:	A command to reproduce the flag of the European Union
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/euflag
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euflag.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euflag.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euflag.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package implements a command to reproduce the
official flag of the European Union (EU). The flag is
reproduced at 1em high based on the current font size, so it
can be scaled arbitrarily by changing the font size.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/euflag
%{_texmfdistdir}/tex/latex/euflag
%doc %{_texmfdistdir}/doc/latex/euflag

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
