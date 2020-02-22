# text_based_browser

My solution to the Jetbrains Academy "Text-Based Browser" project.

## Getting started

### Prerequisites

* Python 3
* OSX or a Linux Distro

NOTE: Due to the fact that Nox, which is used to test and lint this project ONLY has PROVISIONAL support for Windows, this
project can ONLY be tested on a Non-Windows system.

### Installing

To get a development environment locally, do the following:

```shell script
# Clone the repo
git clone https://github.com/blanketastronomer/text_based_browser.git

# Switch to the project root
cd text_based_browser

# Checkout the "develop" branch, since that's where you'll be branching your
# changes off of.
git checkout --track origin/develop

# Install all project requirements
pip install -r requirements.txt
```

At this point, to run any tests or linters, you can just use Nox by running:

```shell script
# Run this in the project root directory.
# It will test and lint the code as well as generate all necessary files for
# testing/deploying.
nox
```

### Running the tests

This project uses Nox for running tests.  There are two ways of using it:

1. Running `nox` in your terminal as stated in the previous section
2. Running `nox.sh` (yes, those two are different)

```shell script
# Run all tests/linters, reuse virtualenvs, and rebuild the Github Action
nox

# Run all tests/linters, rebuild virtualenvs, leave Github Action alone
./nox.sh
```

#### Running `nox`

Running `nox` in your terminal WILL (re)generate the Github Action the project uses.  It will also reuse any virtualenvs
created by Nox.  While this is fastest, it can lead to problems if you run it AFTER modifying `noxfile.py`.

#### Running `nox.sh`

Running `nox.sh` will run everything in `noxfile.py`, just like running `nox` in your terminal would do, except that it WILL
NOT (re)generate the Github Action, but WILL (re)generate the virtualenvs used by Nox.  While this method is the slowest, it's
also closest to how things are run via the Github Action when you push your branch.

### Usage

TODO: Write up usage instructions

## Built with

* [flake8](https://gitlab.com/pycqa/flake8)
* [pytest](https://github.com/pytest-dev/pytest)
* [nox](https://github.com/theacodes/nox)

## Contributing

TODO: Write contributing guidelines.

## Authors

* **Nicholas S.** - *Initial work* - [BlanketAstronomer](https://github.com/BlanketAstronomer)

## License

This project is licensed under the MIT License - See the [LICENSE.md](LICENSE.md) file for details.
