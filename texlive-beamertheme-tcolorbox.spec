Name:		texlive-beamertheme-tcolorbox
Version:	67000
Release:	1
Summary:	A beamer inner theme which reproduces standard beamer blocks using tcolorboxes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamertheme-tcolorbox
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-tcolorbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-tcolorbox.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an inner theme for beamer which
reproduces standard beamer blocks using tcolorboxes. The look
and feel (rounded/sharp corners, shadows and colours) will
automatically adapt to which other themes are loaded.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/beamertheme-tcolorbox
%doc %{_texmfdistdir}/doc/latex/beamertheme-tcolorbox

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
