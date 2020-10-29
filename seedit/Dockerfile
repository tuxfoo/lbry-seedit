## This base image is for running the latest lbrynet-daemon release.
FROM ubuntu:18.04 as prep
LABEL MAINTAINER="leopere [at] nixc [dot] us"
RUN apt-get update && apt-get -y install unzip curl

## Add lbrynet
ARG VERSION=latest
RUN URL=$(curl -Ls https://api.github.com/repos/lbryio/lbry-sdk/releases/$(if [ "${VERSION}" = 'latest' ]; then echo "latest"; else echo "tags/${VERSION}"; fi) | grep browser_download_url | grep lbrynet-linux.zip | cut -d'"' -f4) && echo $URL && curl -L -o /lbrynet.linux.zip $URL


COPY ./core/checkmount.sh /usr/bin/checkmount
RUN unzip /lbrynet.linux.zip -d /lbrynet/ && \
    mv /lbrynet/lbrynet /usr/bin && \
    chmod a+x /usr/bin/checkmount /usr/bin/lbrynet

FROM ubuntu:18.04 as app
COPY --from=prep /usr/bin/checkmount /usr/bin/lbrynet /usr/bin/
RUN adduser lbrynet --gecos GECOS --shell /bin/bash --disabled-password --home /home/lbrynet

RUN apt-get update
RUN apt-get install --yes software-properties-common && \
    add-apt-repository universe && \
    apt-get --fix-broken install  && \
    apt-get update && \
    apt-get install -y wget apt-transport-https && \
    apt-get install -y build-essential && \
    apt-get install --yes libboost-all-dev

RUN apt-get install -y build-essential \
      zlib1g-dev \
      libncurses5-dev \
      libgdbm-dev \
      libnss3-dev \
      libssl-dev \
      libreadline-dev \
      libffi-dev \
      libbz2-dev \
      liblzma-dev \
      nfs-common

# Pull down Python 3.7, build, and install
RUN add-apt-repository ppa:deadsnakes/ppa && \
    add-apt-repository -y ppa:git-core/ppa && \
    apt-get update && \
    apt-get install -y python3.7-dev \
      python3-pip \
      python3.7-venv \
      git \
      man

WORKDIR /home/lbrynet

ADD ./core/requirements.txt ./requirements.txt
COPY ./core/daemon_settings.yml /etc/lbry/daemon_settings.yml
RUN python3.7 -m pip install --upgrade pip
RUN python3.7 -m pip install -r requirements.txt

## Daemon port [Intended for internal use]
## LBRYNET talks to peers on port 3333 [Intended for external use] this port is used to discover other lbrynet daemons with blobs.
## Expose 5566 Reflector port to listen on
## Expose 5279 Port the daemon API will listen on
## the lbryumx aka Wallet port [Intended for internal use]
# EXPOSE 4444 3333 5566 5179 50001 5280 5279

CMD ["/usr/bin/checkmount"]
ENTRYPOINT ["tail", "-F", "/dev/null"]