FROM python:{{cookiecutter.python_version}}

# add user
RUN useradd -r -s /bin/bash bob

# add project
ADD . /app
RUN chown -R bob:bob /app

USER bob

# set home & current env
ENV HOME /app
WORKDIR /app
ENV PATH="/app/.local/bin:${PATH}"

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt --user

# start wsgi server
ENTRYPOINT ["uwsgi"]
CMD ["--socket", "0.0.0.0:{{cookiecutter.uwsgi_port}}", "--protocol", "http", "-w", "wsgi:app", "--processes", "{{cookiecutter.uwsgi_processes}}", "--threads", "{{cookiecutter.uwsgi_threads}}"]
