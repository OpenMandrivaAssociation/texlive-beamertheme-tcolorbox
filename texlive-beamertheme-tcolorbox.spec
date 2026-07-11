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
BuildSystem:	texlive
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

