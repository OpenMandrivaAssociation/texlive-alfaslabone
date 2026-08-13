%global tl_name alfaslabone
%global tl_revision 77682
%global tl_version 0.0.1

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	The Alfa Slab One font face with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/alfaslabone
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alfaslabone.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alfaslabone.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The alfaslabone package supports the Alfa Slab One font face for LaTeX.
There is only a Regular font face. It's useful for book-chapter
headlines.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from alfaslabone:
Map AlphaSlabOne.map
TL_DROPIN_EOF
