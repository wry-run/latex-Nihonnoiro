# Traditional colors of Japan - LaTeX theme

A color scheme inspired by the palette of traditional colors of Japan. Includes definitions for hyperlinks via the [hyperref][hyperref] package, and for code listings via the [listings][listings] package.

## Sources

The palette is drawn from [Stefan Imhoff][Hamada-Imhoff]'s collection of Noboyoshi Hamada's books. I appreciate the clear reference to source material. Unfortunately there are a few spelling mistakes (*Resberry Red*), which I have not corrected, and duplicate definitions, e.g. two different hex codes named *Charcoal Gray*.

An alternative source can be found on [wikipedia][wikipedia], which also provides Kanji definitions, and [kidorokujapan][kidorokujapan], which has a more numerous selection.

## Installation

To make this package available to all projects, add the `.sty` files to your `$TEXMFHOME/tex/latex/` folder. See [latex-solarized][latex-solarized] for a thorough explanation.

The following example works in ubuntu 20.04; it assumes you have `kpsewhich` available e.g. by having installed the `texlive` package, and that you wish to clone this repository to the folder defined below as `PATH_TO_CLONE`. Modify this variable according to your needs.

```bash
$ PATH_TO_CLONE=~/Documents/tex/latex-Nihonnoiro/
$ git clone https://github.com/wry-run/latex-Nihonnoiro.git $PATH_TO_CLONE
$ TEXMFHOME=$(kpsewhich -var-value=TEXMFHOME)
$ mkdir -p $TEXMFHOME/tex/latex/
$ ln -s $PATH_TO_CLONE/*sty $TEXMFHOME/tex/latex/
$ ln -s $PATH_TO_CLONE/colors/*sty $TEXMFHOME/tex/latex/
```

## Usage

`\usepackage{Nihonnoiro-dark}` and `\usepackage{Nihonnoiro-dark-listings}`.

## Example

From the [examples/](examples) folder:

![Dark example](images/example-dark.png)

## License

MIT License. See [LICENSE](LICENSE).

## Acknowledgements

This package owes to [latex-solarized][latex-solarized] and [dracula/latex][dracula/latex]. Kudos, and thanks.

The .gitignore is from [github/gitignore][github/gitignore].

## References

[hyperref]: https://ctan.org/pkg/hyperref
[listings]: https://ctan.org/pkg/listings
[dracula/latex]: https://github.com/dracula/latex
[latex-solarized]: https://github.com/jez/latex-solarized
[github/gitignore]: https://github.com/github/gitignore
[Hamada-Imhoff]: https://www.stefanimhoff.de/traditional-colors-of-japan/
[wikipedia]: https://en.wikipedia.org/wiki/Traditional_colors_of_Japan
[kidorokujapan]: http://kidorakujapan.com/know/others_color_2.html
