# Scan Segment Decoding

This project contains modules and functions written in Python to receive scan segments from SICK Lidar sensors. Furthermore utilities are included to process and decode scan segments in the MSGPACK format.

## Prerequisites

This project relies on [Poetry](https://python-poetry.org/) for dependency management and execution of the virtual python environment. Detailed installation instructions for each platform can be found [here](https://python-poetry.org/docs/).

## Build and deploy locally with poetry

```
cd <THIS_REPOSITORY>
poetry build
poetry run pytest
cd <OTHER_REPOSITORY>
poetry run pip install <THIS_REPOSITORY>/.
```

where `<OTHER_REPOSITORY>` is the directory where the package depending on the `scansegmentdecoding` module is located and `<THIS_REPOSITORY>` is the location where the `scansegmentdecoding` repository has been checked out.

## Deploy locally with pip
After the package has been built with poetry it can be installed in the global environment.

```
cd <THIS_REPOSITORY>
pip install .
```

where `<THIS_REPOSITORY>` is the location where the `scansegmentdecoding` repository has been checked out.

## Usage

After the package has been installed as described above, it can be included in your python project as follows, depending on which functionality is required:
```
from scansegmentdecoding import msgpackUtil
from scansegmentdecoding import connectionHandler
from scansegmentdecoding import decodeUtil
```

## Dependencies

This module relies on the following dependencies which are downloaded during the build process

| Name               | Version   | License                              | URL                                          |
|--------------------|-----------|--------------------------------------|----------------------------------------------|
| certifi            | 2023.5.7 | [Mozilla Public License 2.0 (MPL 2.0)](https://mozilla.org/MPL/2.0/)       | https://github.com/certifi/python-certifi    |
| charset-normalizer | 3.1.0     | [MIT License](https://spdx.org/licenses/MIT.html)                          | https://github.com/Ousret/charset_normalizer |
| colorama           | 0.4.6     | [BSD-3-Clause License](https://spdx.org/licenses/BSD-3-Clause.html)        | https://github.com/tartley/colorama          |
| coverage           | 7.2.5     | [Apache-2.0 License](http://www.apache.org/licenses/LICENSE-2.0)           | https://github.com/nedbat/coveragepy         |
| exceptiongroup     | 1.1.1     | [MIT License](https://spdx.org/licenses/MIT.html)                          | https://github.com/agronholm/exceptiongroup  |
| idna               | 3.4       | [BSD-3-Clause License](https://spdx.org/licenses/BSD-3-Clause.html)        | https://github.com/kjd/idna                  |
| iniconfig          | 2.0.0     | [MIT License](https://spdx.org/licenses/MIT.html)                          | https://github.com/pytest-dev/iniconfig      |
| msgpack            | 1.0.5     | [Apache-2.0 License](http://www.apache.org/licenses/LICENSE-2.0)           | https://msgpack.org/                         |
| numpy              | 1.24.3    | [BSD-3-Clause License](https://spdx.org/licenses/BSD-3-Clause.html)        | https://www.numpy.org                        |
| packaging          | 23.1      | [Apache-2.0 License](http://www.apache.org/licenses/LICENSE-2.0); [BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html)                | https://github.com/pypa/packaging            |
| pluggy             | 1.0.0     | [MIT License](https://spdx.org/licenses/MIT.html)                          | https://github.com/pytest-dev/pluggy         |
| pytest             | 7.3.1     | [MIT License](https://spdx.org/licenses/MIT.html)                          | https://docs.pytest.org/en/latest/           |
| pytest-cov         | 4.0.0     | [MIT License](https://spdx.org/licenses/MIT.html)                          | https://github.com/pytest-dev/pytest-cov     |
| requests           | 2.30.0    | [Apache-2.0 License](http://www.apache.org/licenses/LICENSE-2.0)           | https://requests.readthedocs.io              |
| tomli              | 2.0.1     | [MIT License](https://spdx.org/licenses/MIT.html)                          | https://github.com/hukkin/tomli              |
| urllib3            | 2.0.2   | [MIT License](https://spdx.org/licenses/MIT.html)                          | https://urllib3.readthedocs.io/              |