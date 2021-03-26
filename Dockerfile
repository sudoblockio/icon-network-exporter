
FROM python:3.8 as base

ENV PROJECT_DIR=src
RUN mkdir /$PROJECT_DIR
WORKDIR /$PROJECT_DIR
COPY . .
RUN pip install --upgrade pip && pip install -e /$PROJECT_DIR/

# Add Tini
ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

FROM base as test
COPY requirements_dev.txt .
RUN pip3 install -r requirements_dev.txt

FROM base as prod
ENTRYPOINT ["/tini", "--"]
CMD ["icon-network-exporter"]
