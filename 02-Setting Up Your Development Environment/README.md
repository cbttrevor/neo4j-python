## Learning Objective

Before we get started with code, you'll need to make sure that you have the appropriate tools installed on your system.
For a graphical coding interface, we'll use [Microsoft Visual Studio Code](https://code.visualstudio.com) (VSCode).
Of course, because this skill is focused on Python, you'll need a Python runtime.
Instead of installing Python directly onto our developer workstation, we'll use Docker Desktop to spin up a Python container.

The `remote-containers` extension for Visual Studio Code allows you to run VSCode against a container development environment.

Launch neo4j graph database engine in a Docker container:

```
docker run --interactive --tty --detach --publish 7687:7687 --publish 7474:7474 --volume $HOME/neo4j/data:/data --volume $HOME/neo4j/logs:/logs --volume $HOME/neo4j/import:/var/lib/neo4j/import --volume $HOME/neo4j/plugins:/plugins neo4j
```

Spin up a Python container with Docker:

```
docker run --detach --interactive --tty --name neo4jpython python bash
```

Next, install the `neo4j` Python module

```
pip3 install neo4j
```