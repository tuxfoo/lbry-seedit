from python:3.8 as dev

RUN useradd -ms /bin/bash seedit

USER seedit
WORKDIR /home/seedit
EXPOSE 5279 3333 4444

ENTRYPOINT ["tail", "-f", "/dev/null"]

from dev as prod

COPY ./core ./

