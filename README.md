<p align="center"><img width="750" src="https://i.imgur.com/hcY0ccy.png" alt="Pybacker"></p>

<p align="center">
    <a href="https://github.com/YisusChrist/pybacker/issues">
        <img src="https://img.shields.io/github/issues/YisusChrist/pybacker?color=171b20&label=Issues%20%20&logo=gnubash&labelColor=e05f65&logoColor=ffffff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/pybacker/forks">
        <img src="https://img.shields.io/github/forks/YisusChrist/pybacker?color=171b20&label=Forks%20%20&logo=git&labelColor=f1cf8a&logoColor=ffffff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/pybacker/">
        <img src="https://img.shields.io/github/stars/YisusChrist/pybacker?color=171b20&label=Stargazers&logo=octicon-star&labelColor=70a5eb">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/pybacker/actions">
        <img alt="Tests Passing" src="https://github.com/YisusChrist/pybacker/actions/workflows/github-code-scanning/codeql/badge.svg">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/pybacker/pulls">
        <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/YisusChrist/pybacker?color=0088ff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://opensource.org/license/gpl-2-0/">
        <img alt="License" src="https://img.shields.io/github/license/YisusChrist/pybacker?color=0088ff">
    </a>
</p>

<br>

<p align="center">
    <a href="https://github.com/YisusChrist/pybacker/issues/new/choose">Report Bug</a>
    ·
    <a href="https://github.com/YisusChrist/pybacker/issues/new/choose">Request Feature</a>
    ·
    <a href="https://github.com/YisusChrist/pybacker/discussions">Ask Question</a>
    ·
    <a href="https://github.com/YisusChrist/pybacker/security/policy#reporting-a-vulnerability">Report security bug</a>
</p>

<br>

![Alt](https://repobeats.axiom.co/api/embed/cd9239ab8f98edef7010a72b2a01492ea28060de.svg "Repobeats analytics image")

<br>

`pybacker` is a Python script that allows you to backup your GitHub repositories in a simple and fast way.

<details>
<summary>Table of Contents</summary>

- [Requirements](#requirements)
- [Installation](#installation)
  - [From PyPI](#from-pypi)
  - [Manual installation](#manual-installation)
  - [Uninstall](#uninstall)
- [Usage](#usage)
  - [Example of execution](#example-of-execution)
- [Contributors](#contributors)
  - [How do I contribute to Pybacker?](#how-do-i-contribute-to-pybacker)
- [License](#license)
- [Credits](#credits)

</details>

## Requirements

Here's a breakdown of the packages needed and their versions:

- [poetry](https://pypi.org/project/poetry) - 1.7.1 (_only for manual installation_)
- [requests](https://pypi.org/project/requests) - 2.31.0
- [rich-argparse-plus](https://pypi.org/project/rich-argparse-plus) - 0.3.1.4
- [rich](https://pypi.org/project/rich) - 13.7.0

> [!NOTE]\
> The software has been developed and tested using Python `3.12.1`. The minimum required version to run the software is Python 3.6. Although the software may work with previous versions, it is not guaranteed.

## Installation

### From PyPI

`pybacker` can be installed easily as a PyPI package. Just run the following command:

```bash
pip3 install pybacker
```

> [!IMPORTANT]\
> For best practices and to avoid potential conflicts with your global Python environment, it is strongly recommended to install this program within a virtual environment. Avoid using the --user option for global installations. We highly recommend using [pipx](https://pypi.org/project/pipx) for a safe and isolated installation experience. Therefore, the appropriate command to install `pybacker` would be:
>
> ```bash
> pipx install pybacker
> ```

### Manual installation

If you prefer to install the program manually, follow these steps:

> [!NOTE]\
> This will install the version from the latest commit, not the latest release.

1. Download the latest version of [pybacker](https://github.com/YisusChrist/pybacker) from this repository:

   ```bash
   git clone https://github.com/YisusChrist/pybacker
   cd pybacker
   ```

2. Install the package:

   ```bash
   poetry install
   ```

3. Run the program:

   ```bash
   poetry run pybacker
   ```

### Uninstall

If you installed it from PyPI, you can use the following command:

```bash
pipx uninstall pybacker
```

The program can now be ran from a terminal with the `pybacker` command.

## Usage

> [!NOTE]\
> For more information about the usage of the program, run `pybacker --help` or `pybacker -h`.

![Usage](https://i.imgur.com/LwnSEhr.png)

### Example of execution

![Example](https://i.imgur.com/6Agw47v.png)

## Contributors

<a href="https://github.com/YisusChrist/pybacker/graphs/contributors"><img src="https://contrib.rocks/image?repo=YisusChrist/pybacker" /></a>

### How do I contribute to Pybacker?

Before you participate in our delightful community, please read the [code of conduct](.github/CODE_OF_CONDUCT.md).

I'm far from being an expert and suspect there are many ways to improve – if you have ideas on how to make the configuration easier to maintain (and faster), don't hesitate to fork and send pull requests!

We also need people to test out pull requests. So take a look through [the open issues](https://github.com/YisusChrist/pybacker/issues) and help where you can.

See [Contributing](.github/CONTRIBUTING.md) for more details.

## License

`pybacker` is released under the [GPL-2.0 License](https://opensource.org/license/gpl-2-0).

## Credits

> [!NOTE]\
> Credits to [Julynx](https://github.com/Julynx) for creating the script. I only make improvements in his code based on my preferences to customize it. All the ideas and the base of the script are his.
