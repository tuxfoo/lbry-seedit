from python:3.8 as dev

USER seedit

RUN curl -OL https://github.com/lbryio/lbry-sdk/releases/download/v0.83.0/lbrynet-linux.zip
RUN unzip lbrynet-linux.zip
RUN chmod +x lbrynet
RUN mv lbrynet /usr/local/bin

COPY lbrynet.service /etc/systemd/system/

RUN systemctl enable lbrynet
RUN systemctl start lbrynet
RUN lbrynet settings get && \
    lbrynet settings set wallet_dir /home/seedit/wallet && \
    lbrynet settings set download_dir /home/seedit/downloads && \
    lbrynet settings set data_dir /home/seedit/data && \
    lbrynet settings set max_connections_per_download 10

WORKDIR /home/seedit

from dev as prod

COPY ./core ./

CMD tail -f /dev/null