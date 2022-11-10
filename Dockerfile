FROM ruby:2.7.5

ARG GROUP_ID=1000
ARG USER_ID=1000

ARG USERNAME=tito
ARG GROUP=$USERNAME
ARG CODE_DIR=/code

WORKDIR $CODE_DIR
COPY . $CODE_DIR

RUN apt-get update && apt-get -y install build-essential libstdc++-10-dev libgsl0-dev libatlas-base-dev

RUN groupadd -r $GROUP --gid=$GROUP_ID \
    && useradd --create-home -r $USERNAME -g $GROUP --uid=$USER_ID \
    && mkdir -p /etc/sudoers.d/ \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && chown -R $USERNAME:$GROUP $CODE_DIR

RUN bundle config github.https true && bundle install --full-index

USER $USERNAME

COPY --chown=$USERNAME:$GROUP . $CODE_DIR
