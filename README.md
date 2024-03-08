<h1 align="center">Tilde Terminal Reddit Viewer (TTRV)</h1>
<p>Forked from Original source/development at: <a href="https://github.com/michael-lazar/rtv">RTV</a></p>

<p align="center">
A text-based interface (TUI) to view and interact with Reddit from your terminal.<br>
</p>

<p align="center">
<img alt="title image" src="https://github.com/tildeclub/ttrv/raw/master/resources/title_image.png"/>
</p>

<p align="center">
</p>

## Table of Contents

* [Demo](#demo)  
* [Installation](#installation)  
* [Usage](#usage)  
* [Settings](#settings)
* [Themes](#themes)
* [FAQ](#faq)  
* [Contributing](#contributing)  
* [License](#license)  

## Demo

<p align="center">
<img alt="title image" src="https://github.com/tildeclub/ttrv/raw/master/resources/demo.gif"/>
</p>

## Installation

### PyPI package

TTRV is available on [PyPI](https://pypi.python.org/pypi/ttrv/) and can be installed with pip:

```bash
$ pip install ttrv
```

### From source

```bash
$ git clone https://github.com/tildeclub/ttrv.git
$ cd ttrv/
$ python setup.py install
```

### Windows

TTRV is not supported on Windows but you can enable Windows subsystem for Linux, download your preferred Linux distribution from Microsoft Store and access it from there.

To open links on Edge, paste the line below to ``{HOME}/.bashrc`` 
```
export BROWSER='/mnt/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
```

## Usage

To run the program, type:

```bash
$ ttrv --help
```

### Controls

Move the cursor using either the arrow keys or *Vim* style movement:

- Press <kbd>▲</kbd> and <kbd>▼</kbd> to scroll through submissions
- Press <kbd>▶</kbd> to view the selected submission and <kbd>◀</kbd> to return
- Press <kbd>space-bar</kbd> to expand/collapse comments
- Press <kbd>u</kbd> to login (this requires a web browser for [OAuth](https://github.com/reddit-archive/reddit/wiki/oauth2))
- Press <kbd>?</kbd> to open the help screen

Press <kbd>/</kbd> to open the navigation prompt, where you can type things like:

- ``/front``
- ``/r/commandprompt+linuxmasterrace``
- ``/r/programming/controversial``
- ``/u/me``
- ``/u/multi-mod/m/art``
- ``/domain/github.com``

See [CONTROLS](CONTROLS.md) for the full list of commands.

## Settings

### Configuration File

Configuration files are stored in the ``{HOME}/.config/ttrv/`` directory.

Check out [ttrv.cfg](ttrv/templates/ttrv.cfg) for the full list of configurable options. You can clone this file into your home directory by running:

```bash
$ ttrv --copy-config
```

### Viewing Media Links

You can use [mailcap](https://en.wikipedia.org/wiki/Media_type#Mailcap) to configure how TTRV will open different types of links.

<p align="center">
<img alt="title image" src="https://github.com/tildeclub/ttrv/raw/master/resources/mailcap.gif"/>
</p>

A mailcap file allows you to associate different MIME media types, like ``image/jpeg`` or ``video/mp4``, with shell commands. This feature is disabled by default because it takes a few extra steps to configure. To get started, copy the default mailcap template to your home directory.

```bash
$ ttrv --copy-mailcap
```

This template contains examples for common MIME types that work with popular reddit websites like *imgur*, *youtube*, and *gfycat*. Open the mailcap template and follow the [instructions](ttrv/templates/mailcap) listed inside.

Once you've setup your mailcap file, enable it by launching ttrv with the ``ttrv --enable-media`` flag (or set it in your **ttrv.cfg**)

### Environment Variables

The default programs that TTRV interacts with can be configured through environment variables:

<table>
  <tr>
  <td><strong>$TTRV_EDITOR</strong></td>
  <td>A program used to compose text submissions and comments, e.g. <strong>vim</strong>, <strong>emacs</strong>, <strong>gedit</strong>
  <br/> <em>If not specified, will fallback to $VISUAL and $EDITOR in that order.</em></td>
  </tr>
  <tr>
  <td><strong>$TTRV_BROWSER</strong></td>
  <td>A program used to open links to external websites, e.g. <strong>firefox</strong>, <strong>google-chrome</strong>, <strong>w3m</strong>, <strong>lynx</strong>
  <br/> <em>If not specified, will fallback to $BROWSER, or your system's default browser.</em></td>
  </tr>
  <tr>
  <td><strong>$TTRV_URLVIEWER</strong></td>
  <td>A tool used to extract hyperlinks from blocks of text, e.g. <a href=https://github.com/sigpipe/urlview>urlview</a>, <a href=https://github.com/firecat53/urlscan>urlscan</a>
  <br/> <em>If not specified, will fallback to urlview if it is installed.</em></td>
  </tr>
</table>

### Clipboard

TTRV supports copying submission links to the OS clipboard. On macOS this is supported out of the box.
On Linux systems you will need to install either [xsel](http://www.vergenet.net/~conrad/software/xsel/) or [xclip](https://sourceforge.net/projects/xclip/).

## Themes

Themes can be used to customize the look and feel of TTRV

<table>
  <tr>
    <td align="center">
      <p><strong>Solarized Dark</strong></p>
      <img src="https://github.com/tildeclub/ttrv/raw/master/resources/theme_solarized_dark.png"></img>
    </td>
    <td align="center">
      <p><strong>Solarized Light</strong></p>
      <img src="https://github.com/tildeclub/ttrv/raw/master/resources/theme_solarized_light.png"></img>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p><strong>Papercolor</strong></p>
      <img src="https://github.com/tildeclub/ttrv/raw/master/resources/theme_papercolor.png"></img>
    </td>
    <td align="center">
      <p><strong>Molokai</strong></p>
      <img src="https://github.com/tildeclub/ttrv/raw/master/resources/theme_molokai.png"></img>
    </td>
  </tr>
</table>

You can list all installed themes with the ``--list-themes`` command, and select one with ``--theme``. You can save your choice permanently in your [ttrv.cfg](ttrv/templates/ttrv.cfg) file. You can also use the <kbd>F2</kbd> & <kbd>F3</kbd> keys inside of TTRV to cycle through all available themes.

For instructions on writing and installing your own themes, see [THEMES.md](THEMES.md).

## FAQ

<details>
 <summary>Why am I getting an error during installation/when launching ttrv?</summary>
 
  > If your distro ships with an older version of python 2.7 or python-requests,
  > you may experience SSL errors or other package incompatibilities. The
  > easiest way to fix this is to install ttrv using python 3. If you
  > don't already have pip3, see http://stackoverflow.com/a/6587528 for setup
  > instructions. Then do
  >
  > ```bash
  > $ sudo pip uninstall ttrv
  > $ sudo pip3 install -U ttrv
  > ```

</details>
<details>
  <summary>Why do I see garbled text like <em>M-b~@M-"</em> or <em>^@</em>?</summary>
 
  > This type of text usually shows up when python is unable to render
  > unicode properly.
  >    
  > 1. Try starting TTRV in ascii-only mode with ``ttrv --ascii``
  > 2. Make sure that the terminal/font that you're using supports unicode
  > 3. Try [setting the LOCALE to utf-8](https://perlgeek.de/en/article/set-up-a-clean-utf8-environment)
  > 4. Your python may have been built against the wrong curses library,
  >    see [here](stackoverflow.com/questions/19373027) and
  >    [here](https://bugs.python.org/issue4787) for more information

</details>
<details>
 <summary>How do I run the code directly from the repository?</summary>
 
  > This project is structured to be run as a python *module*. This means that
  > you need to launch it using python's ``-m`` flag. See the example below, which
  > assumes that you have cloned the repository into the directory **~/ttrv_project**.
  >
  > ```bash
  > $ cd ~/ttrv_project
  > $ python3 -m ttrv
  > ```

</details>

## Contributing
All feedback and suggestions are welcome, just post an issue!

Before writing any code, please read the [Contributor Guidelines](CONTRIBUTING.rst).

## License
This project is distributed under the [MIT](LICENSE) license.
   
