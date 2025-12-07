ARG ROS_DISTRO=jazzy
FROM ros:${ROS_DISTRO}-ros-base
ARG ROS_DISTRO=jazzy
ARG USERNAME=USERNAME
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Delete user if it exists in container (e.g Ubuntu Noble: ubuntu)
RUN if id -u $USER_UID ; then userdel `id -un $USER_UID` ; fi

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# add to GPIO GROUP
# Since we are mounting devices directly, group membership is read from INSIDE the CONTAINER
# meaning that we need to have the correct perms on our created user, uid/gid = 1000 just means we can easily save/commit our files
# and retain ownership outside the container
RUN groupadd -g 993 gpio
RUN usermod -aG gpio ${USERNAME}


RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3-pip
RUN apt install python3-libgpiod -y
RUN apt install -y python3-gpiozero

ENV SHELL /bin/bash

# ********************************************************
# * Anything else you want to do like clean up goes here *
# ********************************************************

# [Optional] Set the default user. Omit if you want to keep the default as root.
USER $USERNAME

RUN echo "[ -f /opt/ros/${ROS_DISTRO}/setup.bash ] && source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc
RUN pip3 install RPi.GPIO --no-cache-dir --break-system-packages
RUN sudo apt install -y i2c-tools
RUN sudo apt install python3-smbus2
RUN sudo apt update
RUN sudo apt install -y ros-jazzy-rviz2
RUN sudo apt install -y ros-jazzy-teleop-twist-keyboard


CMD ["/bin/bash"]
