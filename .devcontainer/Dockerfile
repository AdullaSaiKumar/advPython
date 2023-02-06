FROM mcr.microsoft.com/devcontainers/python:0-3.11

ENV PYTHONUNBUFFERED 1

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp
RUN pip3 install psycopg2 pandas numpy scipy scikit-learn lxml spacy pandasql sqlalchemy nltk html5lib beautifulsoup4
RUN pip3 porter2stemmer
RUN pip install --upgrade pip
# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

RUN echo 'alias ll="ls -altrh"' >> ~/.bashrc
RUN echo 'export PATH=.:${PATH}' >> ~/.bashrc

# mkdir -p ~/spark3 | cd ~/spark3 | wget https://dlcdn.apache.org/spark/spark-3.3.1/spark-3.3.1-bin-hadoop3.tgz | tar xvzf 

# wget https://javadl.oracle.com/webapps/download/AutoDL?BundleId=247938_0ae14417abb444ebb02b9815e2103550  java.tar.gz | tar xvzf 

