# copyedit

An easy way to edit your clipboard contents!

copyedit is intended to be an alternative to [Text Editor Anywhere](https://www.listary.com/text-editor-anywhere)

`pip3 install git+https://github.com/Rayquaza01/copyedit`

## Usage

-   Run `copyedit.py`.
-   It will ask for a file extension, create a file with your current clipboard contents, and open the file in your editor.
-   When you close your editor, it will copy the contents of the file to your clipboard

## Options

The options are saved in `~/copyedit.json` and can be overridden in a config file per folder.

-   `editor`: The command to run your preferred text editor. The file with the clipboard contents will be passed as an argument. Defaults to `vim`
-   `default_extension`: The default file extension to use. Can be changed while running. Defaults to `txt`
-   `directory`: The directory to save the temporary clipboard files in. Defaults to `~/copyedit`
-   `delete_on_close`: Whether to delete the temporary file after copyedit finishes. Defaults to `false`
