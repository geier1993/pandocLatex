with import <nixpkgs> {};

stdenv.mkDerivation {
  name = "pandocShell";

  buildInputs = with pkgs; [
    #texlive.combined.scheme-medium
    # texlive full required because of varwidth.sty 
    (texlive.combine {
      inherit (texlive) scheme-full xetex fontspec euenc;
    })
    #texlive.combined.scheme-full
    fontconfig
    lmodern
    python38Packages.python
    python38Packages.pandocfilters
    pandoc
    biber
    haskellPackages.pandoc-citeproc
    #haskellPackages.pandoc-crossref
    #haskellPackages.pandoc-include-code
    #haskellPackages.pandoc-include
    #haskellPackages.pandoc-placetable
    #haskellPackages.pandoc-csv2table
  ];
}
