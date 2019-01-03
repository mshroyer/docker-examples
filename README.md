# Docker Examples

This is a collection of Docker usage examples for various development
environments.  It is meant to help me understand how to use Docker for two
different but related purposes:

1. To create production-ready container images.
2. To provide a reproducible and easily-provisioned development environment
   as similar as possible to my production images.

The examples in this repository do not currently cover the topic of providing
images for continuous integration.

## Python

In addition to production images, Python development calls for a container
image in which we can perform interactive development and run unit tests.
Both of these tasks will call for additional, non-production packages to be
installed, such as pytest for testing and jedi for development.
