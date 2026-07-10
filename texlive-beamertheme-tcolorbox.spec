%global tl_name beamertheme-tcolorbox
%global tl_revision 77380

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	A beamer/ltx-talk inner theme to reproduce standard beamer blocks using tcolo...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamertheme-tcolorbox
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-tcolorbox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-tcolorbox.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(beamer)
Requires:	texlive(tcolorbox)
Requires:	texlive(tikzfill)
Requires:	texlive(tools)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides an inner theme for beamer or ltx-talk which
reproduces standard beamer blocks using tcolorboxes. The look and feel
(rounded/sharp corners, shadows and colours) will automatically adapt to
which other themes are loaded.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-tcolorbox
%dir %{_datadir}/texmf-dist/tex/latex/beamertheme-tcolorbox
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-tcolorbox/DEPENDS.txt
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-tcolorbox/README.md
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-tcolorbox/beamertheme-tcolorbox-doc-settings.sty
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-tcolorbox/beamertheme-tcolorbox-doc.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-tcolorbox/beamertheme-tcolorbox-doc.tex
%{_datadir}/texmf-dist/tex/latex/beamertheme-tcolorbox/beamerinnerthemetcolorbox.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-tcolorbox/talkthemetcolorbox.sty
