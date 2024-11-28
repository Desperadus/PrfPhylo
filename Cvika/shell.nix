{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.iqtree
    pkgs.mrbayes
  ];

  shellHook = ''
    echo "Entering nix-shell"
  '';
}
