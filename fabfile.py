from fabric.api import run, env, cd

env.hosts = ['0.0.0.0']
env.user = 'ubuntu'
env.key_filename = '../codebase.pem'


BASE_DIR = '/ebs1/code/dhk'


def restart(service):
    run('sudo supervisorctl restart %s' % service)


def manage_py(cmd):
    python_path = BASE_DIR + '/env/bin/python'
    settings_file = '--settings=dhk.settings.production'
    managepy_filepath = BASE_DIR + '/dhk/manage.py'
    run('%s %s %s %s' % (python_path, managepy_filepath, cmd, settings_file))


def pip_install():
    pip_path = BASE_DIR + '/env/bin/pip'
    requirements_filepath = BASE_DIR + '/dhk/requirements.txt'
    run('%s install --quiet -r %s' % (pip_path, requirements_filepath))


def deploy():
    with cd(BASE_DIR + '/dhk'):
        run('git checkout master')
        run('git pull')

    pip_install()
    manage_py('migrate')
    manage_py('collectstatic --noinput')
    restart('gunicorn')
