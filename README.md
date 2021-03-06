## Welcome to cc_stretch

This repository was created to provide some challenges in the skills necessary for a sysadmin that need programming skills.

#### Operating System to Use

I prefer to use an unix OS to administrate systems, the OS's like linux and FreeBSD provide a lot of tools to connect in ssh sessions, edit files and manipulate data. I usually install FreeBSD in servers and Linux [Fedora](https://getfedora.org/pt_BR/) in the desktop and notebook to produce my work.

The challanges can be resolve by using Windows, but i will not comment about this, sorry!

#### Languages

* Shell
* * We will use shell scripts to create profiles and environment vars file
* Python
* * Python is so much easy to learn and a powerfull language to administrate operating systems like linux, FreeBSD and Windows.

#### Tools

* Ansible
* * We will use ansible to administrate some remote services.
* TMUX
* * TMUX is a tool to create a persist shell session, that do not close when you get out of the terminal.
* [jupyter-notebook](https://jupyter.org/)
* * Jupyter notebook is a powerful tool to teach coding skills, it provide a line of a shell to execute commands and the results step.

### How the hell this repository will works?

For each directory here, a challange will be available to be executed, to participate each person must create a fork of this repository and resolve the challange, making a pull request with of the resolved challange as your way.

Inside directory must contain a jupyter notebook to explain what who create challange define necessary to be executed and a README explain the challange. 

#### First Steps

Bellow have the steps to create a virtual environment aparted of your OS to play with the challange, including the installation of the jupyter notebook.

* Virtualenv

    *INSTALL*
    ```console
    ~ kanazuchi [cc_stretch] (-> master): dnf install python3-virtualenv
    ```
    *Create ENV*
    ```console
    ~ kanazuchi [cc_stretch] (-> master): virtualenv --python python3.6 ´<work directory>´
    ```
    *Activate ENV*
    ```console
    ~ kanazuchi [cc_stretch] (-> master): source bin/activate
    ```

* [TMUX](http://man.openbsd.org/OpenBSD-current/man1/tmux.1)

    We will use tmux to keep a jupyter server up.

    *INSTALL*
    ```console
    ~ kanazuchi [cc_stretch] (-> master): dnf install tmux
    ```
    *Init session*
    ```console
    ~ kanazuchi [cc_stretch] (-> master): tmux new -s jupyter
    ```

    *To get out from session press the keys Cntrl+b*

    *Get in on the open session*
    ```console
    ~ kanazuchi [cc_stretch] (-> master): tmux att
    ```

* Jupyter

    *INSTALL*
    ```console
    ~ kanazuchi [cc_stretch] (-> master): pip install jupyter
    ```

    *Get in on the tmux session*

    ```console
    ~ kanazuchi [cc_stretch] (-> master): jupyter-notebook
    ```
    
    Jupyter notebook will create a local web server in the address http://localhost:8888/tree

    ![jupyter.jpg](https://github.com/kanazux/cc_stretch/blob/master/images/jupyter.jpg)