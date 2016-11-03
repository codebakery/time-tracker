from contextlib import contextmanager
from fabric.api import abort, cd, env, local, prefix, run, settings, sudo, task
from fabric.contrib.console import confirm
from fabric.contrib.files import exists


env.use_ssh_config = True
env.hosts = ['codebakery.io']
env.project_root = '/home/uwsgi/time-tracker'
env.remote = 'origin'
env.branch = 'master'
env.chown_user = 'uwsgi'
env.chown_group = 'uwsgi'
env.requirements = 'requirements.txt'
env.uwsgi_config = '/etc/uwsgi/time-tracker.ini'
env.virtualenv_path = '/home/uwsgi/time-tracker/.env'

env['sudo_prefix'] += '-H '


@contextmanager
def virtualenv():
    with cd(env.project_root):
        with prefix('source {}/bin/activate'.format(env.virtualenv_path)):
            yield


@task
def test():
    with settings(warn_only=True):
        result = local('./manage.py test', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")


@task
def commit():
    local("git add -p && git commit")


@task
def push():
    local("git push")


@task
def prepare_deploy():
    test()
    commit()
    push()


@task
def pull():
    with cd(env.project_root):
        sudo('chown -R {} .'.format(env.user))
        run('git pull {} {}'.format(env.remote, env.branch))
        sudo('chown -R {}:{} .'.format(env.chown_user, env.chown_group))


@task
def collectstatic():
    with virtualenv():
        sudo('./manage.py collectstatic --noinput', user=env.chown_user)


@task
def migrate():
    with virtualenv():
        sudo('./manage.py migrate', user=env.chown_user)


@task
def restart():
    sudo('service uwsgi restart')


@task
def reload():
    sudo('touch {}'.format(env.uwsgi_config))


@task
def requirements():
    with virtualenv():
        sudo('pip install -U -r {}'.format(env.requirements), user=env.chown_user)


@task
def bootstrap():
    with cd('{}/time_tracker/settings'.format(env.project_root)):
        if not exists('local.py'):
            sudo('ln -s production.py local.py', user=env.chown_user)


@task
def createsuperuser():
    with virtualenv():
        sudo('./manage.py createsuperuser', user=env.chown_user)


@task(default=True)
def deploy():
    pull()
    bootstrap()
    requirements()
    collectstatic()
    migrate()
    reload()
