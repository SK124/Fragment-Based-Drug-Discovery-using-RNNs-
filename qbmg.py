{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "QBMG.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "mount_file_id": "1GnI2v4oO7M4w2FsSsfXmv44MMbSNtHYn",
      "authorship_tag": "ABX9TyPoojveiJKTL+09Dj94SZE1",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/gist/SK124/aa4b928c0349dc1e16879ef7b641e990/qbmg.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZowR9VejxtNz",
        "outputId": "7ad65284-1140-40f5-d329-e43a7660df6f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        }
      },
      "source": [
        "\"\"\" Imports neccesary for installing RDkit \"\"\"\n",
        "\n",
        "#!wget -c https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh\n",
        "!cp '/content/drive/My Drive/Miniconda3-latest-Linux-x86_64.sh' /content/\n",
        "!chmod +x Miniconda3-latest-Linux-x86_64.sh\n",
        "!time bash ./Miniconda3-latest-Linux-x86_64.sh -b -f -p /usr/local\n",
        "!time conda install -q -y -c conda-forge rdkit\n",
        "%matplotlib inline\n",
        "import matplotlib.pyplot as plt\n",
        "import sys\n",
        "import os\n",
        "sys.path.append('/usr/local/lib/python3.7/site-packages/rdkit')\n",
        "%cd /usr/local/lib/python3.7/site-packages/"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "PREFIX=/usr/local\n",
            "Unpacking payload ...\n",
            "Collecting package metadata (current_repodata.json): - \b\b\\ \b\b| \b\bdone\n",
            "Solving environment: - \b\b\\ \b\bdone\n",
            "\n",
            "## Package Plan ##\n",
            "\n",
            "  environment location: /usr/local\n",
            "\n",
            "  added / updated specs:\n",
            "    - _libgcc_mutex==0.1=main\n",
            "    - ca-certificates==2020.1.1=0\n",
            "    - certifi==2020.4.5.1=py37_0\n",
            "    - cffi==1.14.0=py37he30daa8_1\n",
            "    - chardet==3.0.4=py37_1003\n",
            "    - conda-package-handling==1.6.1=py37h7b6447c_0\n",
            "    - conda==4.8.3=py37_0\n",
            "    - cryptography==2.9.2=py37h1ba5d50_0\n",
            "    - idna==2.9=py_1\n",
            "    - ld_impl_linux-64==2.33.1=h53a641e_7\n",
            "    - libedit==3.1.20181209=hc058e9b_0\n",
            "    - libffi==3.3=he6710b0_1\n",
            "    - libgcc-ng==9.1.0=hdf63c60_0\n",
            "    - libstdcxx-ng==9.1.0=hdf63c60_0\n",
            "    - ncurses==6.2=he6710b0_1\n",
            "    - openssl==1.1.1g=h7b6447c_0\n",
            "    - pip==20.0.2=py37_3\n",
            "    - pycosat==0.6.3=py37h7b6447c_0\n",
            "    - pycparser==2.20=py_0\n",
            "    - pyopenssl==19.1.0=py37_0\n",
            "    - pysocks==1.7.1=py37_0\n",
            "    - python==3.7.7=hcff3b4d_5\n",
            "    - readline==8.0=h7b6447c_0\n",
            "    - requests==2.23.0=py37_0\n",
            "    - ruamel_yaml==0.15.87=py37h7b6447c_0\n",
            "    - setuptools==46.4.0=py37_0\n",
            "    - six==1.14.0=py37_0\n",
            "    - sqlite==3.31.1=h62c20be_1\n",
            "    - tk==8.6.8=hbc83047_0\n",
            "    - tqdm==4.46.0=py_0\n",
            "    - urllib3==1.25.8=py37_0\n",
            "    - wheel==0.34.2=py37_0\n",
            "    - xz==5.2.5=h7b6447c_0\n",
            "    - yaml==0.1.7=had09818_2\n",
            "    - zlib==1.2.11=h7b6447c_3\n",
            "\n",
            "\n",
            "The following NEW packages will be INSTALLED:\n",
            "\n",
            "  _libgcc_mutex      pkgs/main/linux-64::_libgcc_mutex-0.1-main\n",
            "  ca-certificates    pkgs/main/linux-64::ca-certificates-2020.1.1-0\n",
            "  certifi            pkgs/main/linux-64::certifi-2020.4.5.1-py37_0\n",
            "  cffi               pkgs/main/linux-64::cffi-1.14.0-py37he30daa8_1\n",
            "  chardet            pkgs/main/linux-64::chardet-3.0.4-py37_1003\n",
            "  conda              pkgs/main/linux-64::conda-4.8.3-py37_0\n",
            "  conda-package-han~ pkgs/main/linux-64::conda-package-handling-1.6.1-py37h7b6447c_0\n",
            "  cryptography       pkgs/main/linux-64::cryptography-2.9.2-py37h1ba5d50_0\n",
            "  idna               pkgs/main/noarch::idna-2.9-py_1\n",
            "  ld_impl_linux-64   pkgs/main/linux-64::ld_impl_linux-64-2.33.1-h53a641e_7\n",
            "  libedit            pkgs/main/linux-64::libedit-3.1.20181209-hc058e9b_0\n",
            "  libffi             pkgs/main/linux-64::libffi-3.3-he6710b0_1\n",
            "  libgcc-ng          pkgs/main/linux-64::libgcc-ng-9.1.0-hdf63c60_0\n",
            "  libstdcxx-ng       pkgs/main/linux-64::libstdcxx-ng-9.1.0-hdf63c60_0\n",
            "  ncurses            pkgs/main/linux-64::ncurses-6.2-he6710b0_1\n",
            "  openssl            pkgs/main/linux-64::openssl-1.1.1g-h7b6447c_0\n",
            "  pip                pkgs/main/linux-64::pip-20.0.2-py37_3\n",
            "  pycosat            pkgs/main/linux-64::pycosat-0.6.3-py37h7b6447c_0\n",
            "  pycparser          pkgs/main/noarch::pycparser-2.20-py_0\n",
            "  pyopenssl          pkgs/main/linux-64::pyopenssl-19.1.0-py37_0\n",
            "  pysocks            pkgs/main/linux-64::pysocks-1.7.1-py37_0\n",
            "  python             pkgs/main/linux-64::python-3.7.7-hcff3b4d_5\n",
            "  readline           pkgs/main/linux-64::readline-8.0-h7b6447c_0\n",
            "  requests           pkgs/main/linux-64::requests-2.23.0-py37_0\n",
            "  ruamel_yaml        pkgs/main/linux-64::ruamel_yaml-0.15.87-py37h7b6447c_0\n",
            "  setuptools         pkgs/main/linux-64::setuptools-46.4.0-py37_0\n",
            "  six                pkgs/main/linux-64::six-1.14.0-py37_0\n",
            "  sqlite             pkgs/main/linux-64::sqlite-3.31.1-h62c20be_1\n",
            "  tk                 pkgs/main/linux-64::tk-8.6.8-hbc83047_0\n",
            "  tqdm               pkgs/main/noarch::tqdm-4.46.0-py_0\n",
            "  urllib3            pkgs/main/linux-64::urllib3-1.25.8-py37_0\n",
            "  wheel              pkgs/main/linux-64::wheel-0.34.2-py37_0\n",
            "  xz                 pkgs/main/linux-64::xz-5.2.5-h7b6447c_0\n",
            "  yaml               pkgs/main/linux-64::yaml-0.1.7-had09818_2\n",
            "  zlib               pkgs/main/linux-64::zlib-1.2.11-h7b6447c_3\n",
            "\n",
            "\n",
            "Preparing transaction: / \b\b- \b\b\\ \b\bdone\n",
            "Executing transaction: / \b\b- \b\b\\ \b\b| \b\b/ \b\b- \b\b\\ \b\b| \b\b/ \b\b- \b\b\\ \b\bdone\n",
            "installation finished.\n",
            "WARNING:\n",
            "    You currently have a PYTHONPATH environment variable set. This may cause\n",
            "    unexpected behavior when running the Python interpreter in Miniconda3.\n",
            "    For best results, please verify that your PYTHONPATH only points to\n",
            "    directories of packages that are compatible with the Python interpreter\n",
            "    in Miniconda3: /usr/local\n",
            "\n",
            "real\t0m29.081s\n",
            "user\t0m11.913s\n",
            "sys\t0m3.755s\n",
            "Collecting package metadata (current_repodata.json): ...working... done\n",
            "Solving environment: ...working... done\n",
            "\n",
            "## Package Plan ##\n",
            "\n",
            "  environment location: /usr/local\n",
            "\n",
            "  added / updated specs:\n",
            "    - rdkit\n",
            "\n",
            "\n",
            "The following packages will be downloaded:\n",
            "\n",
            "    package                    |            build\n",
            "    ---------------------------|-----------------\n",
            "    boost-1.72.0               |   py37h9de70de_0         316 KB  conda-forge\n",
            "    boost-cpp-1.72.0           |       h7b93d67_2        16.3 MB  conda-forge\n",
            "    bzip2-1.0.8                |       h516909a_2         396 KB  conda-forge\n",
            "    ca-certificates-2020.6.20  |       hecda079_0         145 KB  conda-forge\n",
            "    cairo-1.16.0               |    h3fc0475_1005         1.5 MB  conda-forge\n",
            "    certifi-2020.6.20          |   py37hc8dfbb8_0         151 KB  conda-forge\n",
            "    conda-4.8.3                |   py37hc8dfbb8_1         3.0 MB  conda-forge\n",
            "    fontconfig-2.13.1          |    h1056068_1002         365 KB  conda-forge\n",
            "    freetype-2.10.2            |       he06d7ca_0         905 KB  conda-forge\n",
            "    glib-2.65.0                |       h3eb4bd4_0         2.9 MB\n",
            "    icu-67.1                   |       he1b5a44_0        12.9 MB  conda-forge\n",
            "    jpeg-9d                    |       h516909a_0         266 KB  conda-forge\n",
            "    lcms2-2.11                 |       hbd6801e_0         431 KB  conda-forge\n",
            "    libblas-3.8.0              |      17_openblas          11 KB  conda-forge\n",
            "    libcblas-3.8.0             |      17_openblas          11 KB  conda-forge\n",
            "    libgfortran-ng-7.5.0       |      hdf63c60_13         1.7 MB  conda-forge\n",
            "    libiconv-1.15              |    h516909a_1006         2.0 MB  conda-forge\n",
            "    liblapack-3.8.0            |      17_openblas          11 KB  conda-forge\n",
            "    libopenblas-0.3.10         |pthreads_hb3c22a3_4         7.8 MB  conda-forge\n",
            "    libpng-1.6.37              |       hed695b0_1         308 KB  conda-forge\n",
            "    libtiff-4.1.0              |       hc7e4089_6         668 KB  conda-forge\n",
            "    libuuid-2.32.1             |    h14c3975_1000          26 KB  conda-forge\n",
            "    libwebp-base-1.1.0         |       h516909a_3         845 KB  conda-forge\n",
            "    libxcb-1.13                |    h14c3975_1002         396 KB  conda-forge\n",
            "    libxml2-2.9.10             |       h72b56ed_2         1.3 MB  conda-forge\n",
            "    lz4-c-1.9.2                |       he1b5a44_1         226 KB  conda-forge\n",
            "    numpy-1.19.1               |   py37h8960a57_0         5.2 MB  conda-forge\n",
            "    olefile-0.46               |             py_0          31 KB  conda-forge\n",
            "    openssl-1.1.1g             |       h516909a_1         2.1 MB  conda-forge\n",
            "    pandas-1.1.0               |   py37h3340039_0        10.5 MB  conda-forge\n",
            "    pcre-8.44                  |       he1b5a44_0         261 KB  conda-forge\n",
            "    pillow-7.2.0               |   py37h718be6c_1         675 KB  conda-forge\n",
            "    pixman-0.38.0              |    h516909a_1003         594 KB  conda-forge\n",
            "    pthread-stubs-0.4          |    h14c3975_1001           5 KB  conda-forge\n",
            "    pycairo-1.19.1             |   py37h01af8b0_3          77 KB  conda-forge\n",
            "    python-dateutil-2.8.1      |             py_0         220 KB  conda-forge\n",
            "    python_abi-3.7             |          1_cp37m           4 KB  conda-forge\n",
            "    pytz-2020.1                |     pyh9f0ad1d_0         227 KB  conda-forge\n",
            "    rdkit-2020.03.4            |   py37hdd87690_0        24.6 MB  conda-forge\n",
            "    tk-8.6.10                  |       hed695b0_0         3.2 MB  conda-forge\n",
            "    xorg-kbproto-1.0.7         |    h14c3975_1002          26 KB  conda-forge\n",
            "    xorg-libice-1.0.10         |       h516909a_0          57 KB  conda-forge\n",
            "    xorg-libsm-1.2.3           |    h84519dc_1000          25 KB  conda-forge\n",
            "    xorg-libx11-1.6.10         |       h516909a_0         918 KB  conda-forge\n",
            "    xorg-libxau-1.0.9          |       h14c3975_0          13 KB  conda-forge\n",
            "    xorg-libxdmcp-1.1.3        |       h516909a_0          18 KB  conda-forge\n",
            "    xorg-libxext-1.3.4         |       h516909a_0          51 KB  conda-forge\n",
            "    xorg-libxrender-0.9.10     |    h516909a_1002          31 KB  conda-forge\n",
            "    xorg-renderproto-0.11.1    |    h14c3975_1002           8 KB  conda-forge\n",
            "    xorg-xextproto-7.3.0       |    h14c3975_1002          27 KB  conda-forge\n",
            "    xorg-xproto-7.0.31         |    h14c3975_1007          72 KB  conda-forge\n",
            "    zstd-1.4.5                 |       h6597ccf_2         712 KB  conda-forge\n",
            "    ------------------------------------------------------------\n",
            "                                           Total:       104.2 MB\n",
            "\n",
            "The following NEW packages will be INSTALLED:\n",
            "\n",
            "  boost              conda-forge/linux-64::boost-1.72.0-py37h9de70de_0\n",
            "  boost-cpp          conda-forge/linux-64::boost-cpp-1.72.0-h7b93d67_2\n",
            "  bzip2              conda-forge/linux-64::bzip2-1.0.8-h516909a_2\n",
            "  cairo              conda-forge/linux-64::cairo-1.16.0-h3fc0475_1005\n",
            "  fontconfig         conda-forge/linux-64::fontconfig-2.13.1-h1056068_1002\n",
            "  freetype           conda-forge/linux-64::freetype-2.10.2-he06d7ca_0\n",
            "  glib               pkgs/main/linux-64::glib-2.65.0-h3eb4bd4_0\n",
            "  icu                conda-forge/linux-64::icu-67.1-he1b5a44_0\n",
            "  jpeg               conda-forge/linux-64::jpeg-9d-h516909a_0\n",
            "  lcms2              conda-forge/linux-64::lcms2-2.11-hbd6801e_0\n",
            "  libblas            conda-forge/linux-64::libblas-3.8.0-17_openblas\n",
            "  libcblas           conda-forge/linux-64::libcblas-3.8.0-17_openblas\n",
            "  libgfortran-ng     conda-forge/linux-64::libgfortran-ng-7.5.0-hdf63c60_13\n",
            "  libiconv           conda-forge/linux-64::libiconv-1.15-h516909a_1006\n",
            "  liblapack          conda-forge/linux-64::liblapack-3.8.0-17_openblas\n",
            "  libopenblas        conda-forge/linux-64::libopenblas-0.3.10-pthreads_hb3c22a3_4\n",
            "  libpng             conda-forge/linux-64::libpng-1.6.37-hed695b0_1\n",
            "  libtiff            conda-forge/linux-64::libtiff-4.1.0-hc7e4089_6\n",
            "  libuuid            conda-forge/linux-64::libuuid-2.32.1-h14c3975_1000\n",
            "  libwebp-base       conda-forge/linux-64::libwebp-base-1.1.0-h516909a_3\n",
            "  libxcb             conda-forge/linux-64::libxcb-1.13-h14c3975_1002\n",
            "  libxml2            conda-forge/linux-64::libxml2-2.9.10-h72b56ed_2\n",
            "  lz4-c              conda-forge/linux-64::lz4-c-1.9.2-he1b5a44_1\n",
            "  numpy              conda-forge/linux-64::numpy-1.19.1-py37h8960a57_0\n",
            "  olefile            conda-forge/noarch::olefile-0.46-py_0\n",
            "  pandas             conda-forge/linux-64::pandas-1.1.0-py37h3340039_0\n",
            "  pcre               conda-forge/linux-64::pcre-8.44-he1b5a44_0\n",
            "  pillow             conda-forge/linux-64::pillow-7.2.0-py37h718be6c_1\n",
            "  pixman             conda-forge/linux-64::pixman-0.38.0-h516909a_1003\n",
            "  pthread-stubs      conda-forge/linux-64::pthread-stubs-0.4-h14c3975_1001\n",
            "  pycairo            conda-forge/linux-64::pycairo-1.19.1-py37h01af8b0_3\n",
            "  python-dateutil    conda-forge/noarch::python-dateutil-2.8.1-py_0\n",
            "  python_abi         conda-forge/linux-64::python_abi-3.7-1_cp37m\n",
            "  pytz               conda-forge/noarch::pytz-2020.1-pyh9f0ad1d_0\n",
            "  rdkit              conda-forge/linux-64::rdkit-2020.03.4-py37hdd87690_0\n",
            "  xorg-kbproto       conda-forge/linux-64::xorg-kbproto-1.0.7-h14c3975_1002\n",
            "  xorg-libice        conda-forge/linux-64::xorg-libice-1.0.10-h516909a_0\n",
            "  xorg-libsm         conda-forge/linux-64::xorg-libsm-1.2.3-h84519dc_1000\n",
            "  xorg-libx11        conda-forge/linux-64::xorg-libx11-1.6.10-h516909a_0\n",
            "  xorg-libxau        conda-forge/linux-64::xorg-libxau-1.0.9-h14c3975_0\n",
            "  xorg-libxdmcp      conda-forge/linux-64::xorg-libxdmcp-1.1.3-h516909a_0\n",
            "  xorg-libxext       conda-forge/linux-64::xorg-libxext-1.3.4-h516909a_0\n",
            "  xorg-libxrender    conda-forge/linux-64::xorg-libxrender-0.9.10-h516909a_1002\n",
            "  xorg-renderproto   conda-forge/linux-64::xorg-renderproto-0.11.1-h14c3975_1002\n",
            "  xorg-xextproto     conda-forge/linux-64::xorg-xextproto-7.3.0-h14c3975_1002\n",
            "  xorg-xproto        conda-forge/linux-64::xorg-xproto-7.0.31-h14c3975_1007\n",
            "  zstd               conda-forge/linux-64::zstd-1.4.5-h6597ccf_2\n",
            "\n",
            "The following packages will be UPDATED:\n",
            "\n",
            "  ca-certificates     pkgs/main::ca-certificates-2020.1.1-0 --> conda-forge::ca-certificates-2020.6.20-hecda079_0\n",
            "  certifi              pkgs/main::certifi-2020.4.5.1-py37_0 --> conda-forge::certifi-2020.6.20-py37hc8dfbb8_0\n",
            "  conda                       pkgs/main::conda-4.8.3-py37_0 --> conda-forge::conda-4.8.3-py37hc8dfbb8_1\n",
            "  openssl              pkgs/main::openssl-1.1.1g-h7b6447c_0 --> conda-forge::openssl-1.1.1g-h516909a_1\n",
            "  tk                         pkgs/main::tk-8.6.8-hbc83047_0 --> conda-forge::tk-8.6.10-hed695b0_0\n",
            "\n",
            "\n",
            "Preparing transaction: ...working... done\n",
            "Verifying transaction: ...working... done\n",
            "Executing transaction: ...working... done\n",
            "\n",
            "real\t0m37.696s\n",
            "user\t0m31.591s\n",
            "sys\t0m3.763s\n",
            "/usr/local/lib/python3.7/site-packages\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PrfKBJmAezj-",
        "outputId": "6c07f573-9d75-4fd3-c2fc-88ccb78f8758",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "source": [
        "%cd /usr/local/lib/python3.7/site-packages/\n",
        "import re\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import random\n",
        "import pickle\n",
        "import sys\n",
        "import time\n",
        "import torch\n",
        "import torch.nn as nn\n",
        "import torch.nn.functional as F\n",
        "from torch.utils.data import Dataset\n",
        "from torch.utils.data import DataLoader\n",
        "from rdkit import Chem\n",
        "from rdkit.Chem import DataStructs\n",
        "from rdkit.Chem import AllChem\n",
        "from rdkit.Chem import RDConfig\n",
        "from tqdm import tqdm"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/site-packages\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "k1vhytV4e1nx",
        "outputId": "46b82bf7-d28e-499f-8d19-476d2b22e603",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 219
        }
      },
      "source": [
        "%cd /content/\n",
        "path='/content/drive/My Drive/De NovoDrug/full_data_final.csv'\n",
        "df=pd.read_csv(path)\n",
        "df.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/content\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>col</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>CC(C)(C)c1ccc2occ(CC(=O)Nc3ccccc3F)c2c1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>C[C@@H]1CC(Nc2cncc(-c3nncn3C)c2)C[C@@H](C)C1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>N#Cc1ccc(-c2ccc(O[C@@H](C(=O)N3CCCC3)c3ccccc3)...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>CCOC(=O)[C@@H]1CCCN(C(=O)c2nc(-c3ccc(C)cc3)n3c...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>N#CC1=C(SCC(=O)Nc2cccc(Cl)c2)N=C([O-])[C@H](C#...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                                                 col\n",
              "0            CC(C)(C)c1ccc2occ(CC(=O)Nc3ccccc3F)c2c1\n",
              "1       C[C@@H]1CC(Nc2cncc(-c3nncn3C)c2)C[C@@H](C)C1\n",
              "2  N#Cc1ccc(-c2ccc(O[C@@H](C(=O)N3CCCC3)c3ccccc3)...\n",
              "3  CCOC(=O)[C@@H]1CCCN(C(=O)c2nc(-c3ccc(C)cc3)n3c...\n",
              "4  N#CC1=C(SCC(=O)Nc2cccc(Cl)c2)N=C([O-])[C@H](C#..."
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0AwPndlDe4op"
      },
      "source": [
        "def csv2txt(dataframe):\n",
        "   \" Writes the CSV File to text file \" \n",
        "   with open('drug.txt','w') as f:\n",
        "       for i in range(len(dataframe)):\n",
        "           text=dataframe['col'][i]\n",
        "           f.write(text+'\\n')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9aKXrtGRk49c"
      },
      "source": [
        "csv2txt(df)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XR76a4aAlZHp"
      },
      "source": [
        "\n",
        "def txt2list(fname):\n",
        "  \" Takes the molecules in text file to and store it in list \"\n",
        "  smiles = []\n",
        "  with open(fname, 'r') as f:\n",
        "     for line in f:\n",
        "         smiles.append(line.split()[0])\n",
        "  return smiles"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Gky6vDq9lbla"
      },
      "source": [
        "smiles=txt2list('drug.txt')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9Hqoxco-ln9t",
        "outputId": "96516b92-efd5-4ac9-893b-cfa26fdefc5a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "source": [
        "len(smiles)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "100000"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XhZ4007lmBfH"
      },
      "source": [
        "\n",
        "def replace_halogen(string):\n",
        "    \"\"\"Regex to replace Br and Cl with single letters\"\"\"\n",
        "    br = re.compile('Br')\n",
        "    cl = re.compile('Cl')\n",
        "    string = br.sub('R', string)\n",
        "    string = cl.sub('L', string)\n",
        "\n",
        "    return string\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zeFfZcUIeol0"
      },
      "source": [
        "def construct_vocabulary(smiles_list,fname):\n",
        "    \"\"\"Returns all the characters present in a text file.\n",
        "       Uses regex to find characters/tokens of the format '[x]'.\"\"\"\n",
        "    add_chars = set()\n",
        "    for i, smiles in enumerate(smiles_list):\n",
        "        regex = '(\\[[^\\[\\]]{1,10}])'\n",
        "\n",
        "        \"\"\"\n",
        "        Regex Explaination : \\ signifies a special sequence inside a specific set [] of characters for eg.([...CC[NH+]COCN...]) so \\[...] , which can contain [NH+] like molecules inside it which is taken care by  the ... as explained in the following  \n",
        "        To capture such [NH+],[C@@H],[...] molecules, ^ (start with operator) is used, which is to say such a token is going to start, inside which we give the \\[\\] to denote a specific sequence which will start with a '[' and end with ']' ie.[NH+] or [C@@H], here \\ is used to say escape the inbetween enitities(C@@H,NH+) ie dont split them\n",
        "        There can be numbers 1,2....10 to denote begining of rings within the sequence like CCCcc1n.... to capture these numbers {1,10} ie all numbers between 1 to 10, is used\n",
        "        INPUT SMILE ----> 'CCC[C@@H][NH3+][O+][O-][OH+][P+]COCCCcc1nnn' \n",
        "        char_list = ['CCC','[C@@H]','[NH3+]','[O+]','[O-]','[OH+]','[P+]','COCCCcc1nnn']\n",
        "         \n",
        "        \"\"\"\n",
        "        smiles = replace_halogen(smiles)\n",
        "        char_list = re.split(regex, smiles)\n",
        "        for char in char_list:\n",
        "        \"There are characters like [NH+] which need to considered as single token rather than '[', 'N','H','+',']'\"\n",
        "            if char.startswith('['):\n",
        "                add_chars.add(char)\n",
        "\n",
        "            else:\n",
        "            \"chars inside charlist need to be split as well i.e. COCCCcc1nnn need to split into tokens like 'C','O','1','c','n' \"\n",
        "                chars = [unit for unit in char]\n",
        "                [add_chars.add(unit) for unit in chars]\n",
        "\n",
        "    print(\"Number of characters: {}\".format(len(add_chars)))\n",
        "    with open(fname, 'w') as f:\n",
        "        for char in add_chars:\n",
        "            f.write(char + \"\\n\")\n",
        "    return add_chars\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "f6hRPcn6fn_M",
        "outputId": "ec9998a3-0146-4125-b704-1360c369f5a4",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        }
      },
      "source": [
        "construct_vocabulary(smiles,'vocab.txt')"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Number of characters: 58\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'#',\n",
              " '(',\n",
              " ')',\n",
              " '-',\n",
              " '/',\n",
              " '1',\n",
              " '2',\n",
              " '3',\n",
              " '4',\n",
              " '5',\n",
              " '6',\n",
              " '7',\n",
              " '=',\n",
              " 'C',\n",
              " 'F',\n",
              " 'I',\n",
              " 'L',\n",
              " 'N',\n",
              " 'O',\n",
              " 'P',\n",
              " 'R',\n",
              " 'S',\n",
              " '[C@@H]',\n",
              " '[C@@]',\n",
              " '[C@H]',\n",
              " '[C@]',\n",
              " '[CH-]',\n",
              " '[CH2-]',\n",
              " '[N+]',\n",
              " '[N-]',\n",
              " '[NH+]',\n",
              " '[NH-]',\n",
              " '[NH2+]',\n",
              " '[NH3+]',\n",
              " '[O+]',\n",
              " '[O-]',\n",
              " '[OH+]',\n",
              " '[P+]',\n",
              " '[P@@H]',\n",
              " '[P@@]',\n",
              " '[P@]',\n",
              " '[PH2]',\n",
              " '[S+]',\n",
              " '[S-]',\n",
              " '[S@@]',\n",
              " '[S@]',\n",
              " '[SH+]',\n",
              " '[n+]',\n",
              " '[n-]',\n",
              " '[nH+]',\n",
              " '[nH]',\n",
              " '[o+]',\n",
              " '[s+]',\n",
              " '\\\\',\n",
              " 'c',\n",
              " 'n',\n",
              " 'o',\n",
              " 's'}"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 49
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BjdQRfjjZctN"
      },
      "source": [
        "class Vocabulary(object):\n",
        "    \"\"\"A class for handling encoding/decoding from SMILES to an array of indices\"\"\"\n",
        "    def __init__(self, init_from_file=None, max_length=100):\n",
        "        \"E and G are used to signify ending and begining of seqeunce\"\n",
        "        self.special_tokens = ['E', 'G']\n",
        "        \"Other tokens frmo SMILES grammer need to be added\"\n",
        "        self.additional_chars = set()\n",
        "        self.chars = self.special_tokens\n",
        "        self.vocab_size = len(self.chars)\n",
        "        self.vocab = dict(zip(self.chars, range(len(self.chars)))) \n",
        "       # self.vocab = dict((c, i+1) for i, c in enumerate(self.chars))\n",
        "        self.reversed_vocab = {v: k for k, v in self.vocab.items()}\n",
        "       #self.reversed_vocab = {v+1: k for k, v in self.vocab.items()} \n",
        "        self.max_length = max_length\n",
        "        if init_from_file: \n",
        "        \" vocab.txt file which contains all the tokens is given as a input which initiates the vocabulary for the language model\"   \n",
        "          self.init_from_file(init_from_file)\n",
        "\n",
        "    def encode(self, char_list):\n",
        "        \"\"\"Takes a list of characters (eg '[C@@H]') and encodes to array of indices\"\"\"\n",
        "        smiles_matrix = np.zeros(len(char_list), dtype=np.float32)\n",
        "        for i, char in enumerate(char_list):\n",
        "          \"2D Matrix : All the tokens are converted from SMILES to integers\"\n",
        "            smiles_matrix[i] = self.vocab[char]\n",
        "        return smiles_matrix\n",
        "\n",
        "    def decode(self, matrix):\n",
        "        \"\"\"Takes an array of indices and returns the corresponding SMILES\"\"\"\n",
        "        chars = []\n",
        "        for i in matrix:\n",
        "            \"If E token which is the End token is reached, the process terminates\"\n",
        "            if i == self.vocab['E']: break\n",
        "            chars.append(self.reversed_vocab[i])\n",
        "        smiles = \"\".join(chars)\n",
        "        smiles = smiles.replace(\"L\", \"Cl\").replace(\"R\", \"Br\")\n",
        "        return smiles\n",
        "\n",
        "    def tokenize(self, smiles):\n",
        "        \"\"\"Takes a SMILES and return a list of characters/tokens\"\"\"\n",
        "        regex = '(\\[[^\\[\\]]{1,10}\\])'\n",
        "        smiles = replace_halogen(smiles)\n",
        "        char_list = re.split(regex, smiles)\n",
        "        tokenized = []\n",
        "        \"SMILES Sequence needs to be converted to tokens for preprocessing, this is the same code we had in Vocabulary class\"\n",
        "        for char in char_list:\n",
        "            if char.startswith('['):\n",
        "                tokenized.append(char)\n",
        "            else:\n",
        "                chars = [unit for unit in char]\n",
        "                [tokenized.append(unit) for unit in chars]\n",
        "        \"E token is added to signify the ending of a token\"\n",
        "        tokenized.append('E')\n",
        "        return tokenized\n",
        "\n",
        "    def add_characters(self, chars):\n",
        "        \"\"\"Adds characters to the vocabulary\"\"\"\n",
        "        for char in chars:\n",
        "            self.additional_chars.add(char)\n",
        "        char_list = list(self.additional_chars)\n",
        "        char_list.sort()\n",
        "        self.chars = char_list + self.special_tokens\n",
        "        self.vocab_size = len(self.chars)\n",
        "        self.vocab = dict(zip(self.chars, range(len(self.chars))))\n",
        "        self.reversed_vocab = {v: k for k, v in self.vocab.items()}\n",
        "\n",
        "\n",
        "    def init_from_file(self, file):\n",
        "        \"\"\"Takes a file containing \\n separated characters to initialize the vocabulary\"\"\"\n",
        "        with open(file, 'r') as f:\n",
        "          \"All characters from vocab.txt file which has all the unique tokens is taken and added to the Vocabukary of the model\"  \n",
        "            chars = f.read().split()\n",
        "        self.add_characters(chars)\n",
        "\n",
        "    def __len__(self):\n",
        "        return len(self.chars)\n",
        "\n",
        "    def __str__(self):\n",
        "        return \"Vocabulary containing {} tokens: {}\".format(len(self), self.chars)\n",
        "\n",
        "class MolData(Dataset):\n",
        "    \"\"\"Custom PyTorch Dataset that takes a file containing SMILES.\n",
        "        Args:\n",
        "                fname : path to a file containing \\n separated SMILES.\n",
        "                voc   : a Vocabulary instance\n",
        "        Returns:\n",
        "                A custom PyTorch dataset for training the Prior.\n",
        "    \"\"\"\n",
        "    def __init__(self, fname, voc):\n",
        "        self.voc = voc\n",
        "        self.smiles = []\n",
        "        with open(fname, 'r') as f:\n",
        "            for line in f:\n",
        "                self.smiles.append(line.split()[0])\n",
        "\n",
        "    def __getitem__(self, i): \n",
        "        mol = self.smiles[i]\n",
        "        tokenized = self.voc.tokenize(mol)\n",
        "        encoded = self.voc.encode(tokenized)\n",
        "        return Variable(encoded)\n",
        "\n",
        "    def __len__(self):\n",
        "        return len(self.smiles)\n",
        "\n",
        "    def __str__(self):\n",
        "        return \"Dataset containing {} structures.\".format(len(self))\n",
        "\n",
        "    @classmethod\n",
        "    def collate_fn(cls, arr):\n",
        "        \"\"\"Function to take a list of encoded sequences and turn them into a batch\"\"\"\n",
        "        max_length = max([seq.size(0) for seq in arr])\n",
        "        \"\"\" For every batch lets say 64, 64 sequences will be taken an the maximum length of the sequence from that batch woul be max_length \n",
        "        and the shorter seqeunces will be padded till the max_length before passing it to the GRU \"\"\"\n",
        "        collated_arr = Variable(torch.zeros(len(arr), max_length))\n",
        "        for i, seq in enumerate(arr):\n",
        "            collated_arr[i, :seq.size(0)] = seq\n",
        "        return collated_arr\n",
        "\n",
        "\n",
        "def Variable(tensor):\n",
        "    \"\"\"Wrapper for torch.autograd.Variable that also accepts\n",
        "       numpy arrays directly and automatically assigns it to\n",
        "       the GPU.\"\"\"\n",
        "    if isinstance(tensor, np.ndarray):\n",
        "        tensor = torch.from_numpy(tensor)\n",
        "    if torch.cuda.is_available():\n",
        "        return torch.autograd.Variable(tensor).cuda()\n",
        "    return torch.autograd.Variable(tensor)\n",
        "\n",
        "def decrease_learning_rate(optimizer, decrease_by=0.01):\n",
        "    \"\"\"Multiplies the learning rate of the optimizer by 1 - decrease_by\"\"\"\n",
        "    for param_group in optimizer.param_groups:\n",
        "        param_group['lr'] *= (1 - decrease_by)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aNkqMdZZZtGX"
      },
      "source": [
        "class GRU(nn.Module):\n",
        "    \"\"\" Implements a three layer GRU cell including an embedding layer\n",
        "       and an output linear layer back to the size of the vocabulary\"\"\"\n",
        "    def __init__(self, voc_size):\n",
        "        super(GRU, self).__init__()\n",
        "        self.embedding = nn.Embedding(voc_size, 128)\n",
        "        self.gru_1 = nn.GRUCell(128, 512)\n",
        "        self.gru_2 = nn.GRUCell(512, 512)\n",
        "        self.gru_3 = nn.GRUCell(512, 512)\n",
        "        self.linear = nn.Linear(512, voc_size)\n",
        "\n",
        "    def forward(self, x, h):\n",
        "        x = self.embedding(x)\n",
        "        h_out = Variable(torch.zeros(h.size()))\n",
        "        x = h_out[0] = self.gru_1(x, h[0])\n",
        "        x = h_out[1] = self.gru_2(x, h[1])\n",
        "        x = h_out[2] = self.gru_3(x, h[2])\n",
        "        x = self.linear(x)\n",
        "        return x, h_out\n",
        "\n",
        "    def init_h(self, batch_size):\n",
        "        # Initial cell state is zero\n",
        "        return Variable(torch.zeros(3, batch_size, 512))\n",
        "\n",
        "class RNN():\n",
        "    \"\"\"Implements the Prior and Agent RNN. Needs a Vocabulary instance in\n",
        "    order to determine size of the vocabulary and index of the END token\"\"\"\n",
        "    def __init__(self, voc):\n",
        "        self.rnn = GRU(voc.vocab_size)\n",
        "        if torch.cuda.is_available():\n",
        "            self.rnn.cuda()\n",
        "        self.voc = voc\n",
        "\n",
        "    def likelihood(self, target):\n",
        "        \"\"\"\n",
        "            Retrieves the likelihood of a given sequence\n",
        "            Args:\n",
        "                target: (batch_size * sequence_lenght) A batch of sequences\n",
        "            Outputs:\n",
        "                log_probs : (batch_size) Log likelihood for each example*\n",
        "               \n",
        "        \"\"\"\n",
        "        batch_size, seq_length = target.size()\n",
        "        start_token = Variable(torch.zeros(batch_size, 1).long())\n",
        "        start_token[:] = self.voc.vocab['G'] \n",
        "        x = torch.cat((start_token, target[:, :-1]), 1) # G (beginning token) is added to each sequence in the batch.\n",
        "        h = self.rnn.init_h(batch_size) # hidden state is also initalized as per batch size\n",
        "        log_probs = Variable(torch.zeros(batch_size)) #Variable to store log_probabilities \n",
        "\n",
        "        for step in range(seq_length):\n",
        "          \"\"\" for every step from 1 to sequnce length, we pass the GRU, Seqeunce based on the timestep and hidden state and get logits and \n",
        "          hidden state after taking that step\n",
        "          logits is a vector of 'D' dimension where D = voc_size with scores on what should be the next token, which is converted to \n",
        "          log_probs using log_softmax and sent to the NLL Loss function which compares the next predicted word by RNN and Ground Truth and calculates \n",
        "          the loss per sequence per timestep which is accumalted under log_probs and returns total loss after end time step \"\"\"\n",
        "            logits, h = self.rnn(x[:, step], h)\n",
        "            log_prob = F.log_softmax(logits)\n",
        "            log_probs += NLLLoss(log_prob, target[:, step])\n",
        "        return log_probs\n",
        "\n",
        "    def sample(self, batch_size, max_length=150):\n",
        "        \"\"\"\n",
        "            Sample a batch of sequences\n",
        "            Args:\n",
        "                batch_size : Number of sequences to sample \n",
        "                max_length:  Maximum length of the sequences\n",
        "            Outputs:\n",
        "            seqs: (batch_size, seq_length) The sampled sequences.\n",
        "            log_probs : (batch_size) Log likelihood for each sequence.\n",
        "            \n",
        "        \"\"\"\n",
        "        start_token = Variable(torch.zeros(batch_size).long())\n",
        "        start_token[:] = self.voc.vocab['G']\n",
        "        h = self.rnn.init_h(batch_size)\n",
        "        x = start_token\n",
        "\n",
        "        sequences = []\n",
        "        log_probs = Variable(torch.zeros(batch_size))\n",
        "        finished = torch.zeros(batch_size).byte()\n",
        "        if torch.cuda.is_available():\n",
        "            finished = finished.cuda()\n",
        "\n",
        "        for step in range(max_length):\n",
        "          \"\"\" After language model learns the semantic syntax, we need to check its perfomance which is why we sample from it.\n",
        "          The code here is exactly similar to the code in likeilhood function \"\"\" \n",
        "            logits, h = self.rnn(x, h)\n",
        "            prob = F.softmax(logits)\n",
        "            log_prob = F.log_softmax(logits)\n",
        "            \"\"\" torch.multinomial returns a tensor where each row contains 1 index sampled from the multinomial probability distribution \n",
        "            located in the corresponding row of tensor input.\n",
        "            \"\"\"\n",
        "            x = torch.multinomial(prob,1).view(-1)\n",
        "            sequences.append(x.view(-1, 1))\n",
        "            log_probs +=  NLLLoss(log_prob, x)\n",
        "\n",
        "            x = Variable(x.data)\n",
        "            \"\"\" Sampling terminates when E token is spit out of GRU \"\"\"\n",
        "            EOS_sampled = (x == self.voc.vocab['E']).data\n",
        "            finished = torch.ge(finished + EOS_sampled, 1)\n",
        "            if torch.prod(finished) == 1: break\n",
        "\n",
        "        sequences = torch.cat(sequences, 1)\n",
        "        return sequences.data, log_probs\n",
        "\n",
        "def NLLLoss(inputs, targets):\n",
        "    \"\"\"\n",
        "        Custom Negative Log Likelihood loss that returns loss per example,\n",
        "        rather than for the entire batch.\n",
        "        Args:\n",
        "            inputs : (batch_size, num_classes) *Log probabilities of each class*\n",
        "            targets: (batch_size) *Target class index*\n",
        "        Outputs:\n",
        "            loss : (batch_size) *Loss for each example*\n",
        "    \"\"\"\n",
        "\n",
        "    if torch.cuda.is_available():\n",
        "        target_expanded = torch.zeros(inputs.size()).cuda()\n",
        "    else:\n",
        "        target_expanded = torch.zeros(inputs.size())\n",
        "\n",
        "    target_expanded.scatter_(1, targets.contiguous().view(-1, 1).data, 1.0)\n",
        "    loss = Variable(target_expanded) * inputs\n",
        "    loss = torch.sum(loss, 1)\n",
        "    return loss"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WwU9EPsproH2"
      },
      "source": [
        "\" Using the log-softmax will punish bigger mistakes in likelihood space higher.\""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oivqMAeefprT",
        "outputId": "e2230255-e5ce-43e1-c168-1f905b449976",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 69
        }
      },
      "source": [
        "def pretrain(restore_from = None):\n",
        "    \"\"\"Trains the Prior RNN\"\"\"\n",
        "\n",
        "    voc = Vocabulary(init_from_file=\"vocab.txt\")\n",
        "    moldata = MolData(\"drug.txt\", voc)\n",
        "    data = DataLoader(moldata, batch_size=128, shuffle=True, drop_last=True,\n",
        "                      collate_fn=MolData.collate_fn)\n",
        "    \n",
        "    Prior = RNN(voc)\n",
        "    \n",
        "    # Can restore from a saved RNN\n",
        "    if restore_from:\n",
        "        Prior.rnn.load_state_dict(torch.load(restore_from))\n",
        "\n",
        "    optimizer = torch.optim.Adam(Prior.rnn.parameters(), lr = 0.001)\n",
        "    for epoch in range(1, 51):\n",
        "        # When training on a few million compounds, this model converges\n",
        "        # in a few of epochs or even faster. If model sized is increased\n",
        "        # its probably a good idea to check loss against an external set of\n",
        "        # validation SMILES to make sure we dont overfit too much.\n",
        "        for step, batch in tqdm(enumerate(data), total=len(data)):\n",
        "\n",
        "            # Sample from DataLoader\n",
        "            seqs = batch.long()\n",
        "\n",
        "            # Calculate loss\n",
        "            log_p= Prior.likelihood(seqs)\n",
        "            loss = - log_p.mean()\n",
        "\n",
        "            # Calculate gradients and take a step\n",
        "            optimizer.zero_grad()\n",
        "            loss.backward()\n",
        "            optimizer.step()\n",
        "\n",
        "            # Every 500 steps we decrease learning rate and print some information\n",
        "            if step % 500 == 0 and step != 0:\n",
        "                #decrease_learning_rate(optimizer, decrease_by=0.003)\n",
        "                decrease_learning_rate(optimizer, decrease_by=0.001)\n",
        "            if step % 30 == 0 and step != 0:\n",
        "                tqdm.write(\"*\" * 50)\n",
        "                tqdm.write(\"Epoch {:3d}   step {:3d}    loss: {:5.2f}\\n\".format(epoch, step, loss.data))\n",
        "                seqs, likelihood = Prior.sample(100)\n",
        "                valid = 0\n",
        "                f = open('test_output.txt', 'a')\n",
        "                for i, seq in enumerate(seqs.cpu().numpy()):\n",
        "                        smile = voc.decode(seq)\n",
        "                        if Chem.MolFromSmiles(smile):\n",
        "                           valid += 1\n",
        "                           f.write(smile + \"\\n\")\n",
        "                           if i < 10:\n",
        "                             tqdm.write(smile)\n",
        "                f.close()\n",
        "                tqdm.write(\"\\n{:>4.1f}% valid SMILES\".format(100 * valid / len(seqs)))\n",
        "                tqdm.write(\"*\" * 50 + \"\\n\")               \n",
        "        # Save the Prior\n",
        "        torch.save(Prior.rnn.state_dict(), \"50_epoch.ckpt\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "#     smiles_file = sys.argv[1]\n",
        "    smiles_file = '/content/drug.txt'\n",
        "    print(\"Reading smiles...\")\n",
        "    smiles_list = smiles\n",
        "    print(\"Constructing vocabulary...\")\n",
        "    voc_chars = construct_vocabulary(smiles_list, \"vocab.txt\")\n",
        "   # ds.write_smiles_to_file(smiles_list, \"./mols_filtered.smi\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Reading smiles...\n",
            "Constructing vocabulary...\n",
            "Number of characters: 58\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ax2lOdbUnOmk",
        "outputId": "67ae64a4-cc74-42f8-bae5-669cd1c8f3fb",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        }
      },
      "source": [
        "pretrain(restore_from = None)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  0%|          | 0/781 [00:00<?, ?it/s]\u001b[A\u001b[A\u001b[A/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:52: UserWarning: Implicit dimension choice for log_softmax has been deprecated. Change the call to include dim=X as an argument.\n",
            "\n",
            "\n",
            "\n",
            "  0%|          | 1/781 [00:00<02:27,  5.28it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  0%|          | 2/781 [00:00<02:24,  5.38it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  0%|          | 3/781 [00:00<02:16,  5.68it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  1%|          | 4/781 [00:00<02:12,  5.87it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  1%|          | 5/781 [00:00<02:12,  5.86it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  1%|          | 6/781 [00:01<02:11,  5.91it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "58\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  1%|          | 7/781 [00:01<02:06,  6.10it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  1%|          | 8/781 [00:01<02:02,  6.31it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "58\n",
            "66\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  1%|          | 9/781 [00:01<02:03,  6.23it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  1%|▏         | 10/781 [00:01<02:05,  6.15it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "58\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  1%|▏         | 11/781 [00:01<02:02,  6.29it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  2%|▏         | 12/781 [00:01<02:03,  6.23it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  2%|▏         | 13/781 [00:02<02:05,  6.11it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  2%|▏         | 14/781 [00:02<02:06,  6.09it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "66\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  2%|▏         | 15/781 [00:02<02:04,  6.14it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  2%|▏         | 16/781 [00:02<02:06,  6.03it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "66\n",
            "58\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  2%|▏         | 17/781 [00:02<02:03,  6.18it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  2%|▏         | 18/781 [00:02<02:01,  6.28it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  2%|▏         | 19/781 [00:03<02:02,  6.21it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  3%|▎         | 20/781 [00:03<02:07,  5.98it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "66\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  3%|▎         | 21/781 [00:03<02:15,  5.60it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  3%|▎         | 22/781 [00:03<02:09,  5.87it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "57\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  3%|▎         | 23/781 [00:03<02:09,  5.86it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  3%|▎         | 24/781 [00:03<02:07,  5.96it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  3%|▎         | 25/781 [00:04<02:07,  5.92it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  3%|▎         | 26/781 [00:04<02:07,  5.91it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "67\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  3%|▎         | 27/781 [00:04<02:11,  5.72it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  4%|▎         | 28/781 [00:04<02:13,  5.64it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  4%|▎         | 29/781 [00:04<02:15,  5.55it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "69\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:00<?, ?it/s]\n",
            "  7%|▋         | 53/781 [32:54<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            "  4%|▍         | 30/781 [00:05<02:23,  5.24it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:00<?, ?it/s]\n",
            "  7%|▋         | 53/781 [32:54<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            "  4%|▍         | 30/781 [00:05<02:23,  5.24it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [01:44<02:07,  5.87it/s]\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "**************************************************\n",
            "Epoch   1   step  30    loss: 75.11\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:80: UserWarning: Implicit dimension choice for softmax has been deprecated. Change the call to include dim=X as an argument.\n",
            "/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:81: UserWarning: Implicit dimension choice for log_softmax has been deprecated. Change the call to include dim=X as an argument.\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:01<?, ?it/s]\n",
            "  7%|▋         | 53/781 [32:54<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            "  4%|▍         | 30/781 [00:05<02:23,  5.24it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:01<?, ?it/s]\n",
            "  7%|▋         | 53/781 [32:54<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            "  4%|▍         | 30/781 [00:05<02:23,  5.24it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [01:44<02:07,  5.87it/s]\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  4%|▍         | 31/781 [00:05<03:43,  3.35it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            " 0.0% valid SMILES\n",
            "**************************************************\n",
            "\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  4%|▍         | 32/781 [00:05<03:30,  3.56it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  4%|▍         | 33/781 [00:06<03:06,  4.01it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "66\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  4%|▍         | 34/781 [00:06<02:49,  4.40it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  4%|▍         | 35/781 [00:06<02:30,  4.95it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "56\n",
            "66\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  5%|▍         | 36/781 [00:06<02:25,  5.14it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  5%|▍         | 37/781 [00:06<02:19,  5.32it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  5%|▍         | 38/781 [00:06<02:13,  5.57it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  5%|▍         | 39/781 [00:07<02:05,  5.90it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "57\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  5%|▌         | 40/781 [00:07<02:04,  5.97it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  5%|▌         | 41/781 [00:07<02:04,  5.95it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "67\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  5%|▌         | 42/781 [00:07<02:02,  6.03it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  6%|▌         | 43/781 [00:07<01:59,  6.17it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n",
            "57\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  6%|▌         | 44/781 [00:07<01:58,  6.22it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  6%|▌         | 45/781 [00:07<01:57,  6.25it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  6%|▌         | 46/781 [00:08<01:57,  6.25it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  6%|▌         | 47/781 [00:08<01:56,  6.28it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  6%|▌         | 48/781 [00:08<01:56,  6.32it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  6%|▋         | 49/781 [00:08<01:57,  6.24it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  6%|▋         | 50/781 [00:08<02:00,  6.08it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  7%|▋         | 51/781 [00:08<02:00,  6.08it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  7%|▋         | 52/781 [00:09<02:00,  6.05it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  7%|▋         | 53/781 [00:09<01:57,  6.19it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  7%|▋         | 54/781 [00:09<01:55,  6.29it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  7%|▋         | 55/781 [00:09<01:54,  6.35it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "58\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  7%|▋         | 56/781 [00:09<01:57,  6.19it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  7%|▋         | 57/781 [00:09<02:01,  5.96it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "69\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  7%|▋         | 58/781 [00:10<02:05,  5.76it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  8%|▊         | 59/781 [00:10<02:11,  5.47it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  8%|▊         | 60/781 [00:10<02:11,  5.47it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "66\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:06<?, ?it/s]\n",
            "  7%|▋         | 53/781 [32:59<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            "  8%|▊         | 60/781 [00:10<02:11,  5.47it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:06<?, ?it/s]\n",
            "  7%|▋         | 53/781 [32:59<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            "  8%|▊         | 60/781 [00:10<02:11,  5.47it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [01:49<02:07,  5.87it/s]\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "**************************************************\n",
            "Epoch   1   step  60    loss: 55.24\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:06<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:00<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            "  8%|▊         | 60/781 [00:11<02:11,  5.47it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:06<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:00<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            "  8%|▊         | 60/781 [00:11<02:11,  5.47it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [01:49<02:07,  5.87it/s]\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  8%|▊         | 61/781 [00:11<03:51,  3.11it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            " 0.0% valid SMILES\n",
            "**************************************************\n",
            "\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  8%|▊         | 62/781 [00:11<03:24,  3.52it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  8%|▊         | 63/781 [00:11<02:57,  4.04it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "67\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  8%|▊         | 64/781 [00:11<02:40,  4.46it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  8%|▊         | 65/781 [00:11<02:34,  4.65it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "68\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  8%|▊         | 66/781 [00:12<02:29,  4.78it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  9%|▊         | 67/781 [00:12<02:28,  4.82it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  9%|▊         | 68/781 [00:12<02:26,  4.88it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  9%|▉         | 69/781 [00:12<02:17,  5.19it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  9%|▉         | 70/781 [00:12<02:10,  5.46it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  9%|▉         | 71/781 [00:12<02:05,  5.67it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "58\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  9%|▉         | 72/781 [00:13<02:03,  5.76it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "  9%|▉         | 73/781 [00:13<02:02,  5.79it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "66\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "  9%|▉         | 74/781 [00:13<02:00,  5.87it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 10%|▉         | 75/781 [00:13<01:57,  6.03it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 10%|▉         | 76/781 [00:13<01:56,  6.04it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 10%|▉         | 77/781 [00:13<01:58,  5.92it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "56\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 10%|▉         | 78/781 [00:14<01:54,  6.16it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 10%|█         | 79/781 [00:14<01:55,  6.10it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 10%|█         | 80/781 [00:14<01:56,  6.02it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 10%|█         | 81/781 [00:14<01:54,  6.11it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 10%|█         | 82/781 [00:14<01:54,  6.11it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 11%|█         | 83/781 [00:14<01:56,  6.01it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "55\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 11%|█         | 84/781 [00:15<01:57,  5.95it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 11%|█         | 85/781 [00:15<01:54,  6.07it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 11%|█         | 86/781 [00:15<01:53,  6.14it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 11%|█         | 87/781 [00:15<01:51,  6.24it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 11%|█▏        | 88/781 [00:15<01:51,  6.22it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 11%|█▏        | 89/781 [00:15<01:55,  6.00it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:11<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:05<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 12%|█▏        | 90/781 [00:16<01:54,  6.04it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:11<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:05<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 12%|█▏        | 90/781 [00:16<01:54,  6.04it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [01:55<02:07,  5.87it/s]\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "**************************************************\n",
            "Epoch   1   step  90    loss: 47.77\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:12<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:05<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 12%|█▏        | 90/781 [00:16<01:54,  6.04it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:12<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:05<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 12%|█▏        | 90/781 [00:16<01:54,  6.04it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [01:55<02:07,  5.87it/s]\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 12%|█▏        | 91/781 [00:16<03:16,  3.52it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            " 3.0% valid SMILES\n",
            "**************************************************\n",
            "\n",
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 12%|█▏        | 92/781 [00:16<03:00,  3.81it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 12%|█▏        | 93/781 [00:17<02:39,  4.32it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 12%|█▏        | 94/781 [00:17<02:31,  4.54it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 12%|█▏        | 95/781 [00:17<02:25,  4.71it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 12%|█▏        | 96/781 [00:17<02:20,  4.88it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 12%|█▏        | 97/781 [00:17<02:20,  4.86it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 13%|█▎        | 98/781 [00:18<02:17,  4.98it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 13%|█▎        | 99/781 [00:18<02:09,  5.25it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 13%|█▎        | 100/781 [00:18<02:05,  5.43it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "66\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 13%|█▎        | 101/781 [00:18<02:01,  5.62it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 13%|█▎        | 102/781 [00:18<01:57,  5.77it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 13%|█▎        | 103/781 [00:18<01:54,  5.94it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 13%|█▎        | 104/781 [00:18<01:54,  5.91it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 13%|█▎        | 105/781 [00:19<01:53,  5.97it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 14%|█▎        | 106/781 [00:19<01:50,  6.13it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "58\n",
            "66\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 14%|█▎        | 107/781 [00:19<01:52,  5.98it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 14%|█▍        | 108/781 [00:19<01:52,  6.00it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 14%|█▍        | 109/781 [00:19<01:52,  5.96it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 14%|█▍        | 110/781 [00:19<01:49,  6.12it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n",
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 14%|█▍        | 111/781 [00:20<01:52,  5.97it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 14%|█▍        | 112/781 [00:20<01:53,  5.90it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 14%|█▍        | 113/781 [00:20<01:50,  6.04it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 15%|█▍        | 114/781 [00:20<01:50,  6.05it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 15%|█▍        | 115/781 [00:20<01:48,  6.16it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 15%|█▍        | 116/781 [00:20<01:46,  6.22it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 15%|█▍        | 117/781 [00:21<01:48,  6.10it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 15%|█▌        | 118/781 [00:21<01:47,  6.19it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "58\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 15%|█▌        | 119/781 [00:21<01:47,  6.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 15%|█▌        | 120/781 [00:21<01:48,  6.11it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:17<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:11<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 15%|█▌        | 120/781 [00:21<01:48,  6.11it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:17<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:11<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 15%|█▌        | 120/781 [00:21<01:48,  6.11it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:00<02:07,  5.87it/s]\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "**************************************************\n",
            "Epoch   1   step 120    loss: 44.67\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:17<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:11<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 15%|█▌        | 120/781 [00:22<01:48,  6.11it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:17<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:11<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 15%|█▌        | 120/781 [00:22<01:48,  6.11it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:01<02:07,  5.87it/s]\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 15%|█▌        | 121/781 [00:22<03:11,  3.44it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            " 8.0% valid SMILES\n",
            "**************************************************\n",
            "\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 16%|█▌        | 122/781 [00:22<03:02,  3.62it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 16%|█▌        | 123/781 [00:22<02:45,  3.98it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 16%|█▌        | 124/781 [00:22<02:35,  4.23it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 16%|█▌        | 125/781 [00:23<02:30,  4.36it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 16%|█▌        | 126/781 [00:23<02:25,  4.49it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "67\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\r 16%|█▋        | 127/781 [00:23<02:24,  4.53it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 16%|█▋        | 128/781 [00:23<02:12,  4.93it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 17%|█▋        | 129/781 [00:23<02:03,  5.30it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 17%|█▋        | 130/781 [00:23<01:57,  5.56it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 17%|█▋        | 131/781 [00:24<01:54,  5.70it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 17%|█▋        | 132/781 [00:24<01:52,  5.76it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 17%|█▋        | 133/781 [00:24<01:51,  5.80it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 17%|█▋        | 134/781 [00:24<01:54,  5.65it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 17%|█▋        | 135/781 [00:24<01:57,  5.51it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 17%|█▋        | 136/781 [00:25<02:01,  5.32it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 18%|█▊        | 137/781 [00:25<01:57,  5.49it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 18%|█▊        | 138/781 [00:25<01:53,  5.68it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 18%|█▊        | 139/781 [00:25<01:48,  5.90it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "58\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 18%|█▊        | 140/781 [00:25<01:46,  6.01it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 18%|█▊        | 141/781 [00:25<01:45,  6.09it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 18%|█▊        | 142/781 [00:26<01:45,  6.05it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 18%|█▊        | 143/781 [00:26<01:52,  5.65it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 18%|█▊        | 144/781 [00:26<01:56,  5.47it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n",
            "58\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 19%|█▊        | 145/781 [00:26<01:52,  5.64it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 19%|█▊        | 146/781 [00:26<01:49,  5.81it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 19%|█▉        | 147/781 [00:26<01:47,  5.89it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 19%|█▉        | 148/781 [00:27<01:45,  6.03it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 19%|█▉        | 149/781 [00:27<01:44,  6.02it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 19%|█▉        | 150/781 [00:27<01:42,  6.17it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "57\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:23<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:16<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 19%|█▉        | 150/781 [00:27<01:42,  6.17it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:23<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:16<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 19%|█▉        | 150/781 [00:27<01:42,  6.17it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:06<02:07,  5.87it/s]\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "**************************************************\n",
            "Epoch   1   step 150    loss: 41.71\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:23<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:17<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 19%|█▉        | 150/781 [00:27<01:42,  6.17it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:23<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:17<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 19%|█▉        | 150/781 [00:27<01:42,  6.17it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:23<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:17<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 19%|█▉        | 150/781 [00:27<01:42,  6.17it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:23<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:17<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 19%|█▉        | 150/781 [00:27<01:42,  6.17it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:06<02:07,  5.87it/s]\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 19%|█▉        | 151/781 [00:27<03:07,  3.36it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "CC[C@H](OC)C(=O)N1CCCN(Cc1ccc(F)cc1)CC1\n",
            "CCCOCC(=O)[O-]\n",
            "\n",
            " 7.0% valid SMILES\n",
            "**************************************************\n",
            "\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 19%|█▉        | 152/781 [00:28<02:57,  3.55it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 20%|█▉        | 153/781 [00:28<02:35,  4.03it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 20%|█▉        | 154/781 [00:28<02:20,  4.46it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 20%|█▉        | 155/781 [00:28<02:08,  4.86it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "57\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 20%|█▉        | 156/781 [00:28<01:58,  5.29it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 20%|██        | 157/781 [00:29<01:56,  5.34it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "67\n",
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 20%|██        | 158/781 [00:29<02:01,  5.14it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 20%|██        | 159/781 [00:29<02:01,  5.13it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 20%|██        | 160/781 [00:29<02:00,  5.14it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 21%|██        | 161/781 [00:29<02:03,  5.02it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 21%|██        | 162/781 [00:30<01:56,  5.30it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 21%|██        | 163/781 [00:30<01:56,  5.30it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 21%|██        | 164/781 [00:30<01:51,  5.52it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 21%|██        | 165/781 [00:30<01:48,  5.69it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 21%|██▏       | 166/781 [00:30<01:45,  5.85it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 21%|██▏       | 167/781 [00:30<01:43,  5.91it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 22%|██▏       | 168/781 [00:31<01:41,  6.04it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 22%|██▏       | 169/781 [00:31<01:40,  6.07it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 22%|██▏       | 170/781 [00:31<01:41,  6.04it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 22%|██▏       | 171/781 [00:31<01:39,  6.16it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 22%|██▏       | 172/781 [00:31<01:40,  6.03it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 22%|██▏       | 173/781 [00:31<01:41,  5.98it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 22%|██▏       | 174/781 [00:32<01:42,  5.92it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "68\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 22%|██▏       | 175/781 [00:32<01:41,  5.98it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 23%|██▎       | 176/781 [00:32<01:39,  6.08it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "57\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 23%|██▎       | 177/781 [00:32<01:38,  6.10it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 23%|██▎       | 178/781 [00:32<01:39,  6.08it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 23%|██▎       | 179/781 [00:32<01:38,  6.08it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 23%|██▎       | 180/781 [00:33<01:38,  6.08it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:28<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:22<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 23%|██▎       | 180/781 [00:33<01:38,  6.08it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:28<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:22<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 23%|██▎       | 180/781 [00:33<01:38,  6.08it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:12<02:07,  5.87it/s]\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "**************************************************\n",
            "Epoch   1   step 180    loss: 38.12\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:29<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:22<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 23%|██▎       | 180/781 [00:33<01:38,  6.08it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:29<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:22<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 23%|██▎       | 180/781 [00:33<01:38,  6.08it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:12<02:07,  5.87it/s]\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 23%|██▎       | 181/781 [00:33<02:51,  3.49it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            " 8.0% valid SMILES\n",
            "**************************************************\n",
            "\n",
            "58\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 23%|██▎       | 182/781 [00:33<02:33,  3.89it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 23%|██▎       | 183/781 [00:33<02:16,  4.38it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 24%|██▎       | 184/781 [00:34<02:10,  4.58it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 24%|██▎       | 185/781 [00:34<02:07,  4.66it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 24%|██▍       | 186/781 [00:34<02:03,  4.80it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 24%|██▍       | 187/781 [00:34<01:54,  5.19it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 24%|██▍       | 188/781 [00:34<01:47,  5.49it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 24%|██▍       | 189/781 [00:35<01:45,  5.62it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 24%|██▍       | 190/781 [00:35<01:42,  5.79it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "69\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 24%|██▍       | 191/781 [00:35<01:43,  5.68it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 25%|██▍       | 192/781 [00:35<01:42,  5.74it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 25%|██▍       | 193/781 [00:35<01:40,  5.87it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 25%|██▍       | 194/781 [00:35<01:38,  5.96it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 25%|██▍       | 195/781 [00:36<01:38,  5.95it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 25%|██▌       | 196/781 [00:36<01:36,  6.09it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 25%|██▌       | 197/781 [00:36<01:34,  6.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 25%|██▌       | 198/781 [00:36<01:35,  6.13it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "58\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 25%|██▌       | 199/781 [00:36<01:33,  6.24it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 26%|██▌       | 200/781 [00:36<01:32,  6.28it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "66\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 26%|██▌       | 201/781 [00:37<01:40,  5.75it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 26%|██▌       | 202/781 [00:37<01:39,  5.84it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 26%|██▌       | 203/781 [00:37<01:36,  6.02it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 26%|██▌       | 204/781 [00:37<01:37,  5.92it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 26%|██▌       | 205/781 [00:37<01:37,  5.88it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 26%|██▋       | 206/781 [00:37<01:38,  5.83it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "68\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 27%|██▋       | 207/781 [00:38<01:38,  5.84it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 27%|██▋       | 208/781 [00:38<01:37,  5.90it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "68\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 27%|██▋       | 209/781 [00:38<01:38,  5.83it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 27%|██▋       | 210/781 [00:38<01:38,  5.77it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "66\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:34<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:27<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 27%|██▋       | 210/781 [00:38<01:38,  5.77it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:34<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:27<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 27%|██▋       | 210/781 [00:38<01:38,  5.77it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:17<02:07,  5.87it/s]\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "**************************************************\n",
            "Epoch   1   step 210    loss: 36.86\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:34<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:28<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 27%|██▋       | 210/781 [00:39<01:38,  5.77it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:34<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:28<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 27%|██▋       | 210/781 [00:39<01:38,  5.77it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:17<02:07,  5.87it/s]\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 27%|██▋       | 211/781 [00:39<02:45,  3.45it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "11.0% valid SMILES\n",
            "**************************************************\n",
            "\n",
            "66\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 27%|██▋       | 212/781 [00:39<02:30,  3.78it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 27%|██▋       | 213/781 [00:39<02:13,  4.25it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 27%|██▋       | 214/781 [00:39<02:02,  4.63it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 28%|██▊       | 215/781 [00:39<01:53,  4.98it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "58\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 28%|██▊       | 216/781 [00:39<01:45,  5.35it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 28%|██▊       | 217/781 [00:40<01:41,  5.54it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 28%|██▊       | 218/781 [00:40<01:38,  5.69it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 28%|██▊       | 219/781 [00:40<01:38,  5.70it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "66\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 28%|██▊       | 220/781 [00:40<01:39,  5.62it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 28%|██▊       | 221/781 [00:40<01:37,  5.73it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "58\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 28%|██▊       | 222/781 [00:40<01:33,  5.97it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 29%|██▊       | 223/781 [00:41<01:31,  6.09it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 29%|██▊       | 224/781 [00:41<01:31,  6.09it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 29%|██▉       | 225/781 [00:41<01:30,  6.17it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 29%|██▉       | 226/781 [00:41<01:31,  6.07it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 29%|██▉       | 227/781 [00:41<01:31,  6.03it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 29%|██▉       | 228/781 [00:41<01:30,  6.10it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 29%|██▉       | 229/781 [00:42<01:30,  6.11it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 29%|██▉       | 230/781 [00:42<01:28,  6.20it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 30%|██▉       | 231/781 [00:42<01:27,  6.27it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 30%|██▉       | 232/781 [00:42<01:29,  6.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 30%|██▉       | 233/781 [00:42<01:29,  6.14it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "57\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 30%|██▉       | 234/781 [00:42<01:27,  6.28it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 30%|███       | 235/781 [00:43<01:28,  6.15it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 30%|███       | 236/781 [00:43<01:28,  6.17it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 30%|███       | 237/781 [00:43<01:27,  6.22it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 30%|███       | 238/781 [00:43<01:29,  6.07it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 31%|███       | 239/781 [00:43<01:30,  5.97it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "67\n",
            "66\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:39<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:33<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 31%|███       | 240/781 [00:44<01:30,  5.96it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:39<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:33<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "68\n",
            "**************************************************\n",
            "Epoch   1   step 240    loss: 35.98\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\r 31%|███       | 240/781 [00:44<01:30,  5.96it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:39<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:33<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 31%|███       | 240/781 [00:44<01:30,  5.96it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:39<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:33<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 31%|███       | 240/781 [00:44<01:30,  5.96it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:40<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:33<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 31%|███       | 240/781 [00:44<01:30,  5.96it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:40<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:33<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 31%|███       | 240/781 [00:44<01:30,  5.96it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:23<02:07,  5.87it/s]\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 31%|███       | 241/781 [00:44<02:42,  3.32it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "O=C(c1ccccc1C[S@@](=O)c1ccccc1)C(=O)c1ccc(F)cc1\n",
            "CN(Cc1cccc(F)c1)c1c(N)c2ccccc2n1C\n",
            "\n",
            "17.0% valid SMILES\n",
            "**************************************************\n",
            "\n",
            "66\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 31%|███       | 242/781 [00:44<02:34,  3.48it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 31%|███       | 243/781 [00:44<02:20,  3.83it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "66\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 31%|███       | 244/781 [00:45<02:04,  4.31it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "57\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 31%|███▏      | 245/781 [00:45<01:53,  4.71it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 31%|███▏      | 246/781 [00:45<01:45,  5.07it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 32%|███▏      | 247/781 [00:45<01:41,  5.25it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 32%|███▏      | 248/781 [00:45<01:35,  5.57it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "58\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 32%|███▏      | 249/781 [00:45<01:35,  5.58it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 32%|███▏      | 250/781 [00:46<01:33,  5.67it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "66\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 32%|███▏      | 251/781 [00:46<01:30,  5.87it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 32%|███▏      | 252/781 [00:46<01:30,  5.86it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "67\n",
            "58\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 32%|███▏      | 253/781 [00:46<01:28,  5.95it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 33%|███▎      | 254/781 [00:46<01:30,  5.82it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "69\n",
            "67\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 33%|███▎      | 255/781 [00:47<01:31,  5.74it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 33%|███▎      | 256/781 [00:47<01:29,  5.86it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "66\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 33%|███▎      | 257/781 [00:47<01:29,  5.87it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 33%|███▎      | 258/781 [00:47<01:27,  5.97it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 33%|███▎      | 259/781 [00:47<01:29,  5.82it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 33%|███▎      | 260/781 [00:47<01:27,  5.94it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 33%|███▎      | 261/781 [00:48<01:26,  6.03it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 34%|███▎      | 262/781 [00:48<01:27,  5.90it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "66\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 34%|███▎      | 263/781 [00:48<01:25,  6.09it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 34%|███▍      | 264/781 [00:48<01:23,  6.16it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 34%|███▍      | 265/781 [00:48<01:24,  6.08it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 34%|███▍      | 266/781 [00:48<01:25,  5.99it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "66\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 34%|███▍      | 267/781 [00:49<01:26,  5.97it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 34%|███▍      | 268/781 [00:49<01:26,  5.94it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "66\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 34%|███▍      | 269/781 [00:49<01:24,  6.09it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 35%|███▍      | 270/781 [00:49<01:23,  6.12it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:45<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:38<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 35%|███▍      | 270/781 [00:49<01:23,  6.12it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:45<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:38<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 35%|███▍      | 270/781 [00:49<01:23,  6.12it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:28<02:07,  5.87it/s]\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "**************************************************\n",
            "Epoch   1   step 270    loss: 35.44\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:45<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:39<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 35%|███▍      | 270/781 [00:49<01:23,  6.12it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:45<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:39<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 35%|███▍      | 270/781 [00:50<01:23,  6.12it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:45<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:39<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 35%|███▍      | 270/781 [00:50<01:23,  6.12it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:45<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:39<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 35%|███▍      | 270/781 [00:50<01:23,  6.12it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:45<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:39<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 35%|███▍      | 270/781 [00:50<01:23,  6.12it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:28<02:07,  5.87it/s]\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 35%|███▍      | 271/781 [00:50<02:37,  3.24it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "CO/C(/[NH3+])CCC(=O)NCc1ccccc1\n",
            "CSCCCCN1CCC[C@@H](c2ccc(Br)cc2)CCC1\n",
            "CC[C@]1(C)CCCCC[C@@H]1O\n",
            "\n",
            "27.0% valid SMILES\n",
            "**************************************************\n",
            "\n",
            "67\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 35%|███▍      | 272/781 [00:50<02:35,  3.28it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 35%|███▍      | 273/781 [00:50<02:15,  3.74it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 35%|███▌      | 274/781 [00:50<02:02,  4.12it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 35%|███▌      | 275/781 [00:50<01:54,  4.43it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "71\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 35%|███▌      | 276/781 [00:51<01:46,  4.75it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 35%|███▌      | 277/781 [00:51<01:39,  5.07it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 36%|███▌      | 278/781 [00:51<01:34,  5.32it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 36%|███▌      | 279/781 [00:51<01:31,  5.48it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 36%|███▌      | 280/781 [00:51<01:30,  5.56it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 36%|███▌      | 281/781 [00:51<01:27,  5.73it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 36%|███▌      | 282/781 [00:52<01:27,  5.71it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 36%|███▌      | 283/781 [00:52<01:26,  5.79it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 36%|███▋      | 284/781 [00:52<01:24,  5.90it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 36%|███▋      | 285/781 [00:52<01:23,  5.96it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "69\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 37%|███▋      | 286/781 [00:52<01:26,  5.74it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 37%|███▋      | 287/781 [00:53<01:25,  5.77it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "66\n",
            "67\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 37%|███▋      | 288/781 [00:53<01:27,  5.65it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 37%|███▋      | 289/781 [00:53<01:25,  5.72it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n",
            "68\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 37%|███▋      | 290/781 [00:53<01:25,  5.72it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 37%|███▋      | 291/781 [00:53<01:24,  5.83it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 37%|███▋      | 292/781 [00:53<01:24,  5.81it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 38%|███▊      | 293/781 [00:54<01:23,  5.83it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "66\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 38%|███▊      | 294/781 [00:54<01:21,  5.94it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 38%|███▊      | 295/781 [00:54<01:22,  5.88it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "67\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 38%|███▊      | 296/781 [00:54<01:21,  5.92it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 38%|███▊      | 297/781 [00:54<01:21,  5.95it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 38%|███▊      | 298/781 [00:54<01:21,  5.96it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 38%|███▊      | 299/781 [00:55<01:19,  6.10it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:50<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:44<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 38%|███▊      | 300/781 [00:55<01:19,  6.05it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:50<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:44<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 38%|███▊      | 300/781 [00:55<01:19,  6.05it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:34<02:07,  5.87it/s]\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n",
            "**************************************************\n",
            "Epoch   1   step 300    loss: 34.26\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:51<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:44<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 38%|███▊      | 300/781 [00:55<01:19,  6.05it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:51<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:44<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 38%|███▊      | 300/781 [00:55<01:19,  6.05it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:51<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:44<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 38%|███▊      | 300/781 [00:55<01:19,  6.05it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:51<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:44<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 38%|███▊      | 300/781 [00:55<01:19,  6.05it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:51<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:44<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 38%|███▊      | 300/781 [00:55<01:19,  6.05it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:51<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:45<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 38%|███▊      | 300/781 [00:55<01:19,  6.05it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:34<02:07,  5.87it/s]\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 39%|███▊      | 301/781 [00:55<02:17,  3.49it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "COc1cccc(/CC[NH2+][C@H](C)NC(=O)N[C@@H]2C[C@H](SC)C2)c1\n",
            "Cl[C@@H]([C@H]1CC[C@]1(C)O[C@@H]1CCCO1)N1CCN(c2ccccc2)CC1\n",
            "CC1=C(C(=O)N(CCNC(=O)N2CCCCC2)CO1)C[C@@H](O)C(C)(C)C\n",
            "CC[C@H](C)SC(=O)N1CCN(S(=O)(=O)c2cccc(Br)c2)CC1\n",
            "\n",
            "28.0% valid SMILES\n",
            "**************************************************\n",
            "\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 39%|███▊      | 302/781 [00:56<02:13,  3.58it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 39%|███▉      | 303/781 [00:56<02:02,  3.89it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 39%|███▉      | 304/781 [00:56<01:53,  4.19it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 39%|███▉      | 305/781 [00:56<01:43,  4.59it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 39%|███▉      | 306/781 [00:56<01:35,  4.97it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 39%|███▉      | 307/781 [00:56<01:30,  5.23it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 39%|███▉      | 308/781 [00:57<01:26,  5.46it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 40%|███▉      | 309/781 [00:57<01:24,  5.61it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 40%|███▉      | 310/781 [00:57<01:19,  5.93it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "56\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 40%|███▉      | 311/781 [00:57<01:18,  5.97it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 40%|███▉      | 312/781 [00:57<01:18,  5.99it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 40%|████      | 313/781 [00:57<01:20,  5.82it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 40%|████      | 314/781 [00:58<01:25,  5.48it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 40%|████      | 315/781 [00:58<01:27,  5.30it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "69\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 40%|████      | 316/781 [00:58<01:30,  5.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 41%|████      | 317/781 [00:58<01:26,  5.36it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 41%|████      | 318/781 [00:58<01:24,  5.46it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 41%|████      | 319/781 [00:59<01:21,  5.64it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 41%|████      | 320/781 [00:59<01:18,  5.84it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 41%|████      | 321/781 [00:59<01:15,  6.07it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "58\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 41%|████      | 322/781 [00:59<01:15,  6.08it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 41%|████▏     | 323/781 [00:59<01:14,  6.12it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 41%|████▏     | 324/781 [00:59<01:16,  5.97it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 42%|████▏     | 325/781 [01:00<01:18,  5.79it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "57\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 42%|████▏     | 326/781 [01:00<01:20,  5.67it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 42%|████▏     | 327/781 [01:00<01:22,  5.49it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 42%|████▏     | 328/781 [01:00<01:24,  5.36it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 42%|████▏     | 329/781 [01:00<01:22,  5.46it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "66\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:56<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:50<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 42%|████▏     | 330/781 [01:01<01:24,  5.35it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "                                       "
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "**************************************************\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:56<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:50<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 42%|████▏     | 330/781 [01:01<01:24,  5.35it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:40<02:07,  5.87it/s]\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "Epoch   1   step 330    loss: 34.38\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:56<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:50<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 42%|████▏     | 330/781 [01:01<01:24,  5.35it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:56<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:50<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 42%|████▏     | 330/781 [01:01<01:24,  5.35it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:57<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:50<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 42%|████▏     | 330/781 [01:01<01:24,  5.35it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [35:57<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:50<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 42%|████▏     | 330/781 [01:01<01:24,  5.35it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:40<02:07,  5.87it/s]\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 42%|████▏     | 331/781 [01:01<02:11,  3.43it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "COc1ccccc1CNC(=O)NC[S@](=O)c1ccc(OC2CC2)o1\n",
            "O=C(\\c1ccc(Cl)cc1)N(C)c1ccccc1Cl\n",
            "\n",
            "26.0% valid SMILES\n",
            "**************************************************\n",
            "\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 43%|████▎     | 332/781 [01:01<02:13,  3.36it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 43%|████▎     | 333/781 [01:02<01:59,  3.74it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 43%|████▎     | 334/781 [01:02<01:50,  4.05it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 43%|████▎     | 335/781 [01:02<01:43,  4.33it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "55\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 43%|████▎     | 336/781 [01:02<01:32,  4.81it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 43%|████▎     | 337/781 [01:02<01:26,  5.12it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 43%|████▎     | 338/781 [01:02<01:21,  5.46it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 43%|████▎     | 339/781 [01:03<01:18,  5.60it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 44%|████▎     | 340/781 [01:03<01:17,  5.72it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 44%|████▎     | 341/781 [01:03<01:15,  5.86it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "66\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 44%|████▍     | 342/781 [01:03<01:15,  5.81it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 44%|████▍     | 343/781 [01:03<01:14,  5.86it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 44%|████▍     | 344/781 [01:03<01:14,  5.89it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 44%|████▍     | 345/781 [01:04<01:15,  5.81it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 44%|████▍     | 346/781 [01:04<01:14,  5.84it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 44%|████▍     | 347/781 [01:04<01:12,  5.98it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "67\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 45%|████▍     | 348/781 [01:04<01:15,  5.76it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\r 45%|████▍     | 349/781 [01:04<01:20,  5.38it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 45%|████▍     | 350/781 [01:05<01:22,  5.21it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 45%|████▍     | 351/781 [01:05<01:23,  5.13it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 45%|████▌     | 352/781 [01:05<01:23,  5.14it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 45%|████▌     | 353/781 [01:05<01:22,  5.22it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "58\n",
            "58\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 45%|████▌     | 354/781 [01:05<01:21,  5.21it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 45%|████▌     | 355/781 [01:06<01:21,  5.26it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "66\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 46%|████▌     | 356/781 [01:06<01:21,  5.23it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 46%|████▌     | 357/781 [01:06<01:21,  5.21it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 46%|████▌     | 358/781 [01:06<01:23,  5.08it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 46%|████▌     | 359/781 [01:06<01:22,  5.10it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:02<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:56<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 46%|████▌     | 360/781 [01:07<01:23,  5.05it/s]"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "**************************************************\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:02<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:56<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 46%|████▌     | 360/781 [01:07<01:23,  5.05it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:02<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:56<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 46%|████▌     | 360/781 [01:07<01:23,  5.05it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:46<02:07,  5.87it/s]"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "Epoch   1   step 360    loss: 32.83\n",
            "\n",
            "O=S(=O)(Cc1cncc2cccn12)Cc1ncnc2ccs12\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:02<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:56<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 46%|████▌     | 360/781 [01:07<01:23,  5.05it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:02<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:56<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 46%|████▌     | 360/781 [01:07<01:23,  5.05it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:02<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:56<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 46%|████▌     | 360/781 [01:07<01:23,  5.05it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:03<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:56<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 46%|████▌     | 360/781 [01:07<01:23,  5.05it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:03<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:56<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 46%|████▌     | 360/781 [01:07<01:23,  5.05it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:03<?, ?it/s]\n",
            "  7%|▋         | 53/781 [33:56<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 46%|████▌     | 360/781 [01:07<01:23,  5.05it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:46<02:07,  5.87it/s]\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 46%|████▌     | 361/781 [01:07<02:09,  3.25it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "CCOc1ccc(Cl)cc1NCC[NH+](C)C\n",
            "CC[C@H](C)CCNC(=O)N[C@H](C)Cc1cccc([N+](=O)[O-])c1\n",
            "O=C(c1ccc(OCc2ccccc2)cc1)n1nnc(OC)c1C\n",
            "Oc1ccc(OCC(=O)NNc2ccc(Cl)c(C)c2)cc1Cl\n",
            "\n",
            "43.0% valid SMILES\n",
            "**************************************************\n",
            "\n",
            "67\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 46%|████▋     | 362/781 [01:07<02:10,  3.21it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 46%|████▋     | 363/781 [01:08<01:53,  3.70it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "67\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 47%|████▋     | 364/781 [01:08<01:40,  4.16it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 47%|████▋     | 365/781 [01:08<01:29,  4.66it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 47%|████▋     | 366/781 [01:08<01:22,  5.04it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 47%|████▋     | 367/781 [01:08<01:17,  5.36it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "67\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 47%|████▋     | 368/781 [01:08<01:16,  5.40it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 47%|████▋     | 369/781 [01:09<01:13,  5.64it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 47%|████▋     | 370/781 [01:09<01:11,  5.75it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 48%|████▊     | 371/781 [01:09<01:08,  5.98it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "58\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 48%|████▊     | 372/781 [01:09<01:07,  6.01it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 48%|████▊     | 373/781 [01:09<01:06,  6.16it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 48%|████▊     | 374/781 [01:09<01:06,  6.10it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 48%|████▊     | 375/781 [01:10<01:07,  5.99it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 48%|████▊     | 376/781 [01:10<01:11,  5.64it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 48%|████▊     | 377/781 [01:10<01:14,  5.42it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "58\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 48%|████▊     | 378/781 [01:10<01:14,  5.41it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 49%|████▊     | 379/781 [01:10<01:15,  5.32it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "67\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 49%|████▊     | 380/781 [01:11<01:19,  5.03it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 49%|████▉     | 381/781 [01:11<01:20,  4.95it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 49%|████▉     | 382/781 [01:11<01:21,  4.89it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "66\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 49%|████▉     | 383/781 [01:11<01:17,  5.16it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 49%|████▉     | 384/781 [01:11<01:13,  5.42it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 49%|████▉     | 385/781 [01:11<01:09,  5.72it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "56\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 49%|████▉     | 386/781 [01:12<01:09,  5.71it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 50%|████▉     | 387/781 [01:12<01:12,  5.41it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "68\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 50%|████▉     | 388/781 [01:12<01:17,  5.10it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 50%|████▉     | 389/781 [01:12<01:12,  5.40it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:08<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:02<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 50%|████▉     | 390/781 [01:13<01:09,  5.61it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:08<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:02<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 50%|████▉     | 390/781 [01:13<01:09,  5.61it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:51<02:07,  5.87it/s]\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "**************************************************\n",
            "Epoch   1   step 390    loss: 32.01\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:08<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:02<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 50%|████▉     | 390/781 [01:13<01:09,  5.61it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:08<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:02<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 50%|████▉     | 390/781 [01:13<01:09,  5.61it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:08<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:02<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 50%|████▉     | 390/781 [01:13<01:09,  5.61it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:08<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:02<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 50%|████▉     | 390/781 [01:13<01:09,  5.61it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:08<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:02<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 50%|████▉     | 390/781 [01:13<01:09,  5.61it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:08<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:02<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 50%|████▉     | 390/781 [01:13<01:09,  5.61it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:52<02:07,  5.87it/s]\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 50%|█████     | 391/781 [01:13<01:52,  3.46it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "Cc1csc(CSCC(=O)NC[C@H]2C[C@H]2C)c1O\n",
            "CC(C)CCN(C)C(=O)c1ccc(OC(=O)OCCc2ccccc2Cl)cc1\n",
            "CC[C@H](NC(=O)c1cccc(NC(=O)c2ccc(Cl)cc2)c1)C(C)C\n",
            "CCN1C(=O)c2ccccc2N[C@H]1C[C@H]1CCCN1c1ccccc1\n",
            "\n",
            "38.0% valid SMILES\n",
            "**************************************************\n",
            "\n",
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 50%|█████     | 392/781 [01:13<01:51,  3.50it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 50%|█████     | 393/781 [01:13<01:36,  4.00it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "58\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 50%|█████     | 394/781 [01:14<01:26,  4.48it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 51%|█████     | 395/781 [01:14<01:18,  4.95it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 51%|█████     | 396/781 [01:14<01:13,  5.25it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 51%|█████     | 397/781 [01:14<01:10,  5.44it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 51%|█████     | 398/781 [01:14<01:06,  5.73it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 51%|█████     | 399/781 [01:14<01:05,  5.84it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 51%|█████     | 400/781 [01:14<01:04,  5.95it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 51%|█████▏    | 401/781 [01:15<01:06,  5.69it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 51%|█████▏    | 402/781 [01:15<01:09,  5.47it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 52%|█████▏    | 403/781 [01:15<01:07,  5.57it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 52%|█████▏    | 404/781 [01:15<01:05,  5.73it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 52%|█████▏    | 405/781 [01:15<01:04,  5.84it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "68\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 52%|█████▏    | 406/781 [01:16<01:06,  5.62it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 52%|█████▏    | 407/781 [01:16<01:05,  5.75it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 52%|█████▏    | 408/781 [01:16<01:05,  5.73it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 52%|█████▏    | 409/781 [01:16<01:03,  5.89it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 52%|█████▏    | 410/781 [01:16<01:02,  5.94it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 53%|█████▎    | 411/781 [01:16<01:00,  6.10it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 53%|█████▎    | 412/781 [01:17<01:00,  6.07it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 53%|█████▎    | 413/781 [01:17<01:05,  5.66it/s]"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 53%|█████▎    | 414/781 [01:17<01:07,  5.46it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "58\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 53%|█████▎    | 415/781 [01:17<01:05,  5.60it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 53%|█████▎    | 416/781 [01:17<01:02,  5.85it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 53%|█████▎    | 417/781 [01:17<01:01,  5.91it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "68\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 54%|█████▎    | 418/781 [01:18<01:06,  5.42it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 54%|█████▎    | 419/781 [01:18<01:08,  5.32it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 54%|█████▍    | 420/781 [01:18<01:10,  5.15it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "67\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:14<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:08<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 54%|█████▍    | 420/781 [01:18<01:10,  5.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:14<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:08<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 54%|█████▍    | 420/781 [01:18<01:10,  5.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:57<02:07,  5.87it/s]\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "**************************************************\n",
            "Epoch   1   step 420    loss: 34.63\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:14<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:08<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 54%|█████▍    | 420/781 [01:19<01:10,  5.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:14<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:08<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 54%|█████▍    | 420/781 [01:19<01:10,  5.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:14<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:08<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 54%|█████▍    | 420/781 [01:19<01:10,  5.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [02:57<02:07,  5.87it/s]\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 54%|█████▍    | 421/781 [01:19<01:48,  3.32it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "CN(C(=O)[C@H](C)c1ccc(F)cc1Cl)C(=O)Nc1nnc(-c2ccc3c(c2)OCO3)o1\n",
            "\n",
            "35.0% valid SMILES\n",
            "**************************************************\n",
            "\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 54%|█████▍    | 422/781 [01:19<01:45,  3.41it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 54%|█████▍    | 423/781 [01:19<01:33,  3.83it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 54%|█████▍    | 424/781 [01:19<01:21,  4.37it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 54%|█████▍    | 425/781 [01:19<01:14,  4.78it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 55%|█████▍    | 426/781 [01:20<01:10,  5.02it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 55%|█████▍    | 427/781 [01:20<01:10,  5.03it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 55%|█████▍    | 428/781 [01:20<01:10,  4.99it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 55%|█████▍    | 429/781 [01:20<01:07,  5.23it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 55%|█████▌    | 430/781 [01:20<01:04,  5.47it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 55%|█████▌    | 431/781 [01:20<01:01,  5.70it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 55%|█████▌    | 432/781 [01:21<01:00,  5.80it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 55%|█████▌    | 433/781 [01:21<00:57,  6.02it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 56%|█████▌    | 434/781 [01:21<00:58,  5.93it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 56%|█████▌    | 435/781 [01:21<00:56,  6.12it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 56%|█████▌    | 436/781 [01:21<00:55,  6.17it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 56%|█████▌    | 437/781 [01:21<00:56,  6.06it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n",
            "58\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 56%|█████▌    | 438/781 [01:22<00:56,  6.10it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 56%|█████▌    | 439/781 [01:22<00:55,  6.12it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 56%|█████▋    | 440/781 [01:22<00:56,  6.04it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 56%|█████▋    | 441/781 [01:22<00:54,  6.21it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "58\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 57%|█████▋    | 442/781 [01:22<00:55,  6.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 57%|█████▋    | 443/781 [01:22<00:55,  6.11it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 57%|█████▋    | 444/781 [01:23<00:57,  5.87it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 57%|█████▋    | 445/781 [01:23<00:56,  5.94it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 57%|█████▋    | 446/781 [01:23<00:55,  6.01it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 57%|█████▋    | 447/781 [01:23<00:54,  6.10it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 57%|█████▋    | 448/781 [01:23<00:54,  6.13it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 57%|█████▋    | 449/781 [01:23<00:53,  6.25it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:19<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:13<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 58%|█████▊    | 450/781 [01:24<00:57,  5.78it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n",
            "**************************************************\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "  0%|          | 0/781 [36:19<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:13<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 58%|█████▊    | 450/781 [01:24<00:57,  5.78it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [03:03<02:07,  5.87it/s]\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "Epoch   1   step 450    loss: 31.90\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:20<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:13<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 58%|█████▊    | 450/781 [01:24<00:57,  5.78it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:20<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:13<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 58%|█████▊    | 450/781 [01:24<00:57,  5.78it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:20<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:13<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 58%|█████▊    | 450/781 [01:24<00:57,  5.78it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:20<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:13<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 58%|█████▊    | 450/781 [01:24<00:57,  5.78it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:20<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:13<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 58%|█████▊    | 450/781 [01:24<00:57,  5.78it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:20<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:13<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 58%|█████▊    | 450/781 [01:24<00:57,  5.78it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:20<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:13<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 58%|█████▊    | 450/781 [01:24<00:57,  5.78it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:20<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:13<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 58%|█████▊    | 450/781 [01:24<00:57,  5.78it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [03:03<02:07,  5.87it/s]\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 58%|█████▊    | 451/781 [01:24<01:48,  3.05it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "O=C(Nc1ccccc1)NCC1CCCC1\n",
            "O=C(c1cc[n+]s1)C(=S)Nc1ccc(NC2CC2)cc1\n",
            "[NH3+]c1cnc(SSc2ncccc2C(=O)NCc2ccc(Cl)cc2)cc1\n",
            "CC([NH3+])CCNC(=O)c1ccc(C)c(Cl)c1\n",
            "C[C@H]1Sc2ccccc2C[C@H]1C(=O)N[C@@H](CC)C(=O)Nc1ccc(C(C)C)cc1\n",
            "CS(=O)(=O)NC[C@H]1Cc2ccccc2C1\n",
            "\n",
            "48.0% valid SMILES\n",
            "**************************************************\n",
            "\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 58%|█████▊    | 452/781 [01:25<01:49,  3.00it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 58%|█████▊    | 453/781 [01:25<01:32,  3.56it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "58\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 58%|█████▊    | 454/781 [01:25<01:21,  4.03it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 58%|█████▊    | 455/781 [01:25<01:12,  4.52it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 58%|█████▊    | 456/781 [01:25<01:06,  4.89it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 59%|█████▊    | 457/781 [01:25<01:01,  5.23it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 59%|█████▊    | 458/781 [01:26<01:00,  5.33it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 59%|█████▉    | 459/781 [01:26<01:01,  5.21it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 59%|█████▉    | 460/781 [01:26<01:03,  5.05it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 59%|█████▉    | 461/781 [01:26<01:03,  5.04it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 59%|█████▉    | 462/781 [01:26<01:02,  5.10it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 59%|█████▉    | 463/781 [01:27<01:01,  5.15it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "58\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 59%|█████▉    | 464/781 [01:27<01:02,  5.07it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 60%|█████▉    | 465/781 [01:27<01:01,  5.10it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "58\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 60%|█████▉    | 466/781 [01:27<00:57,  5.44it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 60%|█████▉    | 467/781 [01:27<00:55,  5.65it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 60%|█████▉    | 468/781 [01:27<00:54,  5.70it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 60%|██████    | 469/781 [01:28<00:54,  5.74it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "66\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 60%|██████    | 470/781 [01:28<00:52,  5.93it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 60%|██████    | 471/781 [01:28<00:51,  5.97it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 60%|██████    | 472/781 [01:28<00:52,  5.94it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 61%|██████    | 473/781 [01:28<00:51,  5.99it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 61%|██████    | 474/781 [01:28<00:51,  5.99it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 61%|██████    | 475/781 [01:29<00:50,  6.09it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n",
            "66\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 61%|██████    | 476/781 [01:29<00:50,  6.04it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 61%|██████    | 477/781 [01:29<00:50,  5.97it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 61%|██████    | 478/781 [01:29<00:51,  5.93it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 61%|██████▏   | 479/781 [01:29<00:49,  6.14it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "58\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:25<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:19<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 61%|██████▏   | 480/781 [01:30<00:48,  6.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:25<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:19<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 61%|██████▏   | 480/781 [01:30<00:48,  6.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [03:08<02:07,  5.87it/s]\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "**************************************************\n",
            "Epoch   1   step 480    loss: 30.16\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:25<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:19<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 61%|██████▏   | 480/781 [01:30<00:48,  6.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:25<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:19<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 61%|██████▏   | 480/781 [01:30<00:48,  6.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:25<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:19<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 61%|██████▏   | 480/781 [01:30<00:48,  6.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:25<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:19<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 61%|██████▏   | 480/781 [01:30<00:48,  6.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:25<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:19<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 61%|██████▏   | 480/781 [01:30<00:48,  6.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:25<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:19<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 61%|██████▏   | 480/781 [01:30<00:48,  6.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:26<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:19<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 61%|██████▏   | 480/781 [01:30<00:48,  6.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:26<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:19<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 61%|██████▏   | 480/781 [01:30<00:48,  6.15it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [03:09<02:07,  5.87it/s]\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 62%|██████▏   | 481/781 [01:30<01:22,  3.65it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "[NH3+]CCc1noc(c2cccc(C(=O)[O-])c2)n1\n",
            "CC1(CC)CCN(C(=O)CCc2cccc(OCc3ccccc3)c2N)c1=O\n",
            "C[C@H]1CCC[C@@H]1NC(=O)C(=O)OC(C)(C)C1CCCCCCC1\n",
            "CCC1=[NH+]C(C)(C(=O)[O-])CC1\n",
            "COCCc1nnc(C2CC2)o1\n",
            "O=C(CCN1CCc2ccccc21)N(C)CC1CC1\n",
            "\n",
            "53.0% valid SMILES\n",
            "**************************************************\n",
            "\n",
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 62%|██████▏   | 482/781 [01:30<01:26,  3.46it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 62%|██████▏   | 483/781 [01:30<01:14,  4.00it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "67\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 62%|██████▏   | 484/781 [01:31<01:07,  4.38it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 62%|██████▏   | 485/781 [01:31<01:00,  4.86it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "58\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 62%|██████▏   | 486/781 [01:31<00:56,  5.18it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 62%|██████▏   | 487/781 [01:31<00:54,  5.43it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 62%|██████▏   | 488/781 [01:31<00:51,  5.68it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 63%|██████▎   | 489/781 [01:31<00:50,  5.77it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 63%|██████▎   | 490/781 [01:32<00:52,  5.50it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 63%|██████▎   | 491/781 [01:32<00:54,  5.37it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 63%|██████▎   | 492/781 [01:32<00:53,  5.44it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 63%|██████▎   | 493/781 [01:32<00:52,  5.46it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 63%|██████▎   | 494/781 [01:32<00:50,  5.69it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 63%|██████▎   | 495/781 [01:33<00:47,  6.00it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "56\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 64%|██████▎   | 496/781 [01:33<00:48,  5.87it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 64%|██████▎   | 497/781 [01:33<00:48,  5.90it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "66\n",
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 64%|██████▍   | 498/781 [01:33<00:48,  5.80it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 64%|██████▍   | 499/781 [01:33<00:48,  5.87it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "57\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 64%|██████▍   | 500/781 [01:33<00:46,  6.07it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 64%|██████▍   | 501/781 [01:34<00:48,  5.74it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "70\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 64%|██████▍   | 502/781 [01:34<00:50,  5.55it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 64%|██████▍   | 503/781 [01:34<00:47,  5.86it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "57\n",
            "58\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 65%|██████▍   | 504/781 [01:34<00:46,  6.01it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 65%|██████▍   | 505/781 [01:34<00:45,  6.00it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "66\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 65%|██████▍   | 506/781 [01:34<00:46,  5.91it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 65%|██████▍   | 507/781 [01:35<00:46,  5.87it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "67\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 65%|██████▌   | 508/781 [01:35<00:46,  5.85it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 65%|██████▌   | 509/781 [01:35<00:46,  5.90it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "64\n",
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:31<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:25<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 65%|██████▌   | 510/781 [01:35<00:46,  5.84it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:31<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:25<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 65%|██████▌   | 510/781 [01:35<00:46,  5.84it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [03:14<02:07,  5.87it/s]\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n",
            "**************************************************\n",
            "Epoch   1   step 510    loss: 30.83\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:31<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:25<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 65%|██████▌   | 510/781 [01:35<00:46,  5.84it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:31<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:25<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 65%|██████▌   | 510/781 [01:35<00:46,  5.84it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:31<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:25<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 65%|██████▌   | 510/781 [01:36<00:46,  5.84it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:31<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:25<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 65%|██████▌   | 510/781 [01:36<00:46,  5.84it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:31<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:25<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 65%|██████▌   | 510/781 [01:36<00:46,  5.84it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:31<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:25<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 65%|██████▌   | 510/781 [01:36<00:46,  5.84it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [03:14<02:07,  5.87it/s]\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 65%|██████▌   | 511/781 [01:36<01:13,  3.65it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "Cn1ccn1CC(=O)NC[C@H]1CCC[C@@H]1N2C(=O)c1ccc(C)c(OC)c12\n",
            "COCC(N)=C/C(=O)C1=C(C)C(=O)N(c2ccccc2)C1=O\n",
            "O=C(CC1(O)NC[C@H]1c1cc(Cl)ccc1Cl)N1CC[NH+](C)CC1\n",
            "Cc1ccc(NN(C(=O)c2ccccc2F)[C@@H]2CCC[C@@H]2C)cc1\n",
            "\n",
            "45.0% valid SMILES\n",
            "**************************************************\n",
            "\n",
            "58\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 66%|██████▌   | 512/781 [01:36<01:13,  3.67it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 66%|██████▌   | 513/781 [01:36<01:04,  4.16it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "61\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 66%|██████▌   | 514/781 [01:36<00:58,  4.59it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 66%|██████▌   | 515/781 [01:36<00:53,  4.96it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 66%|██████▌   | 516/781 [01:37<00:51,  5.19it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 66%|██████▌   | 517/781 [01:37<00:49,  5.33it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "66\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 66%|██████▋   | 518/781 [01:37<00:47,  5.54it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 66%|██████▋   | 519/781 [01:37<00:45,  5.78it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "60\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 67%|██████▋   | 520/781 [01:37<00:44,  5.88it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 67%|██████▋   | 521/781 [01:37<00:45,  5.76it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n",
            "63\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 67%|██████▋   | 522/781 [01:38<00:44,  5.78it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 67%|██████▋   | 523/781 [01:38<00:44,  5.76it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "66\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 67%|██████▋   | 524/781 [01:38<00:44,  5.77it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 67%|██████▋   | 525/781 [01:38<00:43,  5.88it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "59\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 67%|██████▋   | 526/781 [01:38<00:42,  6.00it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 67%|██████▋   | 527/781 [01:38<00:42,  5.99it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "66\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 68%|██████▊   | 528/781 [01:39<00:42,  5.91it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 68%|██████▊   | 529/781 [01:39<00:41,  6.13it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "56\n",
            "60\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 68%|██████▊   | 530/781 [01:39<00:41,  6.10it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 68%|██████▊   | 531/781 [01:39<00:40,  6.16it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "62\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 68%|██████▊   | 532/781 [01:39<00:40,  6.19it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 68%|██████▊   | 533/781 [01:39<00:40,  6.14it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "62\n",
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 88%|██████▊   | 534/781 [01:40<00:41,  5.99it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 89%|██████▊   | 535/781 [01:40<00:39,  6.17it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n",
            "61\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 89%|██████▊   | 536/781 [01:40<00:39,  6.19it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 90%|██████▉   | 537/781 [01:40<00:39,  6.14it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "65\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 94%|██████▉   | 538/781 [01:40<00:39,  6.12it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 94%|██████▉   | 539/781 [01:40<00:41,  5.86it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "67\n",
            "64\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:36<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:30<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 95%|██████▉   | 540/781 [01:41<00:43,  5.54it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:36<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:30<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 96%|██████▉   | 540/781 [01:41<00:43,  5.54it/s]"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "59\n",
            "**************************************************\n",
            "Epoch   1   step 540    loss: 31.08\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:37<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:30<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 69%|██████▉   | 540/781 [01:41<00:43,  5.54it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:37<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:30<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 69%|██████▉   | 540/781 [01:41<00:43,  5.54it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:37<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:30<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 69%|██████▉   | 540/781 [01:41<00:43,  5.54it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:37<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:30<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 69%|██████▉   | 540/781 [01:41<00:43,  5.54it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:37<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:30<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 69%|██████▉   | 540/781 [01:41<00:43,  5.54it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:37<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:30<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 69%|██████▉   | 540/781 [01:41<00:43,  5.54it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\n",
            "\n",
            "\n",
            "\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  0%|          | 0/781 [36:37<?, ?it/s]\n",
            "  7%|▋         | 53/781 [34:30<02:00,  6.03it/s]\u001b[A\n",
            "\n",
            "\n",
            " 99%|██████▉   | 540/781 [01:41<00:43,  5.54it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "  4%|▍         | 30/781 [03:20<02:07,  5.87it/s]\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 99%|██████▉   | 541/781 [01:41<01:10,  3.41it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "Cc1ccc(NC(=O)c2c(NC(=O)CCC(C)C)oc(C)c2)CCO1\n",
            "CSCc1nc(N(Cc2ccccc2)S(C)(=O)=O)cc(C)c1OC\n",
            "CC[NH2+][C@H]1CCC[C@H](CC)[C@@H](C)O1\n",
            "COC(=O)[C@H]1CCCN1C(=O)NCc1con(C)c1=O\n",
            "CC[S@](=O)C[C@H](C)Cn1c2ccccc2nc1[C@@H]1CC[C@H](N(C)C)C1\n",
            "\n",
            "90.0% valid SMILES\n",
            "**************************************************\n",
            "\n",
            "65\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "\n",
            " 99%|██████▉   | 542/781 [01:41<01:10,  3.39it/s]\u001b[A\u001b[A\u001b[A\n",
            "\n",
            "\n",
            " 100%|██████▉   | 543/781 [01:42<01:01,  3.85it/s]\u001b[A\u001b[A\u001b[A"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "63\n",
            "63\n"
          ],
          "name": "stdout"
        },
      
    {
      "cell_type": "code",
      "metadata": {
        "id": "me3SKf4HDVb0"
      },
      "source": [
        "mv /content/50_epoch.ckpt '/content/drive/My Drive/De NovoDrug'"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4jePrE7JPkwX"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
