ithin
=====

"Thin" chronological sequences of images into groups of similar-enough images.

Installation
------------

Setup a Python virtualenv, then run `pip install -e .`.

Usage
-----

First, use `ithin process` to generate a data file:

```
ithin process -d my_image_directory -o my_data.dat
```

Depending on the number of images and their size, etc., this may take a while.
The data file will a resized copy of each image, so it may be large.

Use `ithin summarize` to see how the images were grouped.

```
ithin summarize -i my_data.dat -o summary.html
```

Open `summary.html` in your browser.

(A future release might include tools for extracting samples of each group, etc.)
