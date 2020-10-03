# {{cookiecutter.project_name}}

Here should be the description for your project.

## Getting started

You want to know how to get the application running?

```bash
 $ docker build -t {{cookiecutter.project_name}} .
 $ docker run --publish {{cookiecutter.uwsgi_port}}:{{cookiecutter.uwsgi_port}} {{cookiecutter.project_name}}
```

Visit the following address in your browser:  
`http://localhost:{{cookiecutter.uwsgi_port}}/api`

If everything worked as expected, you should see a JSON message.

Happy coding!
