# pandoc-watch


## Goal

A simple watcher used to call the `pandoc` command with the provided arguments when a file/folder modification is detected.

## Details

`pandoc-watch`is a simple script used to perform the pandoc compilation based on the provided arguments.

It's written in python and uses the `watchdog` module to catch file/folder events.

`pandoc` is a general purpose compiler used to convert files from one markup format into another. For more information, please refer to pandoc website : [http://johnmacfarlane.net/pandoc](http://johnmacfarlane.net/pandoc)

## Installation

First things first, intall the `watchdog` module with `pip` through the following command:

    $ pip install watchdog

Then clone the repository wherever you want and add it to your path: 

    $ git clone git@github.com:dloureiro/pandoc-watch.git
    $ export PATH=$(pwd):$PATH

Simple as that!

You sure need to have a functionnal installation of `pandoc` on your machine and it should  be available in the `PATH`

You can download it from John Mac Farlane dedicated website : [http://johnmacfarlane.net/pandoc](http://johnmacfarlane.net/pandoc)

## How to use `pandoc-watch`

`pandoc-watch` mainly adds an extra argument to the `pandoc` standard options : `-e,--exclude` used to exclude:

 * file extensions
 * folders 
 
from the monitoring when watching for file or folder changes.

Aside from this option, the remaining is passed to the `pandoc` executable without modification.

### Default exclusions

If no exclusion option is provided the default value is `.pdf,.tex,doc,bin,common`. This default values fit my needs and can be modified if necessary.

### Excluding file extensions from the monitoring

To add file extensions to the excluded extensions, call `pandoc-watch` as follow:

    pandoc-watch -e ".pdf,.tex" ...

This commande will exclude all files with `pdf` or `tex` extensions from the monitoring.

### Excluding folders from the monitoring

To exclude folders from the monitoring, call `pandoc-watch` as follow:

    pandoc-watch -e "bin,common"

## License

`pandoc-watch`is provided under the AGPL v3.0 license.

Please refer to the `COPYING` file for detail information.
