FROM python:3.7.2-alpine3.8 AS work
ENV APPDIR /app
WORKDIR $APPDIR
COPY . $APPDIR
RUN rm -rf .eggs *.egg-info .pytest_cache .idea
RUN find $APPDIR -name __pycache__ | xargs rm -rf
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 80

FROM work AS deploy
RUN python setup.py install
CMD ["example_server"]
