# copyedit

An easy way to edit your clipboard contents!

copyedit is intended to be an alternative to [Text Editor Anywhere](https://www.listary.com/text-editor-anywhere)

## Installation

-   Run `git clone https://github.com/Rayquaza01/copyedit`
-   Run `pip3 install pyperclip` and, if applicable, install the necessary programs for pyperclip to work (see https://pypi.org/project/pyperclip/)

## Usage

-   Run `copyedit.py`.
-   It will ask for a file extension, create a file with your current clipboard contents, and open the file in your editor.
-   When you close your editor, it will copy the contents of the file to your clipboard

## Options

The options are saved in `config.json`.

-   `editor`: The command to run your preferred text editor. The file with the clipboard contents will be passed as an argument. Defaults to `vim`
-   `default_extension`: The default file extension to use. Can be changed while running. Defaults to `txt`
-   `directory`: The directory to save the temporary clipboard files in. Defaults to `~/copyedit`
-   `delete_on_close`: Whether to delete the temporary file after copyedit finishes. Defaults to `false`
