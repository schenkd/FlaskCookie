FROM python:{{cookiecutter.python_version}}

# establish working folder
WORKDIR /app

# add user and give ownership to workdir
RUN useradd -r -s /bin/bash bob
RUN chown -R bob:bob /app

USER bob

# set home & current env
ENV HOME /app
ENV PATH="/app/.local/bin:${PATH}"

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --user

# add project
ADD . /app

# start wsgi server
ENTRYPOINT ["uwsgi"]
CMD ["--socket", "0.0.0.0:{{cookiecutter.uwsgi_port}}", "--protocol", "http", "-w", "wsgi:app", "--processes", "{{cookiecutter.uwsgi_processes}}", "--threads", "{{cookiecutter.uwsgi_threads}}"]
