FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye
ARG USERNAME=vscode
ARG USER_UID=501
ARG USER_GID=20

RUN usermod --uid $USER_UID --gid $USER_GID $USERNAME \
    && chown -R $USER_UID:$USER_GID /home/$USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#    && apt-get -y install --no-install-recommends poetry ruff
RUN pip install poetry ruff
USER vscode
RUN poetry config virtualenvs.in-project true
