#!/usr/bin/env bash
#
# Runs the full Django migration process (https://docs.djangoproject.com/en/1.11/topics/migrations/)

# Load virtual environment
if source ${TWLIGHT_HOME}/bin/virtualenv_activate.sh
then
    # Try to get a db shell
    db_init_wait=0
    db_init_timeout=60
    until echo 'exit' | python ${TWLIGHT_HOME}/manage.py dbshell || [ $db_init_wait -eq $db_init_timeout ]
    do
        >&2 echo "Waiting for DB."
        sleep $(( db_init_wait++ ))
    done

    if [ $db_init_wait -lt $db_init_timeout ]
    then
        >&2 echo "DB up."
    else
        echo "DB timeout."
        exit 1
    fi
else
    exit 1
fi
