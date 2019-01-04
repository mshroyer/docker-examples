# Docker Examples

This is a collection of Docker usage examples for various programming
environments.  It is meant to help me understand how to use Docker for two
different but related purposes:

1. To create containers for deployment.
2. To provide a reproducible and easily-provisioned development environment (à
   la Vagrant), as similar as possible to the production environment.

## Python

In addition to deployment images, Python development calls for a an image in
which we can perform interactive development and run unit tests.  Both of
these tasks may require additional, non-production packages to be installed,
such as pytest for testing and jedi for development.

We can use a multi-stage build to satisfy these two purposes.  The first stage
will copy the app's files and install the app's dependencies, and the second
stage will run `setup.py install` to complete the app's installation.  If we
want to do local development, we can build just the first stage:

    $ docker build -t imagename --target work .
    
Then we can run this image with a host workspace mounted as the `/app`
directory, and install the package in development (symlinked) mode:

    $ docker run -it -v "$PWD":/app --name containername imagename /bin/sh
    # python setup.py develop
    # python setup.py test

When we're done developing, we can commit our changes to an image for later
reuse:

    $ docker commit containername imagename
    $ docker container rm containername

At the time of this writing, [elpy](https://elpy.readthedocs.io/en/latest/)
does not directly support using a Python interpreter in a Docker container.
However, PyCharm has plugins to support that workflow.
