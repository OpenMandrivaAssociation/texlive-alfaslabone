Name:		texlive-alfaslabone
Version:	57452
Release:	2
Summary:	The Alfa Slab One font face with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/alfaslabone
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alfaslabone.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alfaslabone.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The alfaslabone package supports the Alfa Slab One font face
for LaTeX. There is only a Regular font face. It's useful for
book-chapter headlines.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/alfaslabone
%{_texmfdistdir}/fonts/vf/public/alfaslabone
%{_texmfdistdir}/fonts/type1/public/alfaslabone
%{_texmfdistdir}/fonts/tfm/public/alfaslabone
%{_texmfdistdir}/fonts/opentype/public/alfaslabone
%{_texmfdistdir}/fonts/map/dvips/alfaslabone
%{_texmfdistdir}/fonts/enc/dvips/alfaslabone
%doc %{_texmfdistdir}/doc/fonts/alfaslabone

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
