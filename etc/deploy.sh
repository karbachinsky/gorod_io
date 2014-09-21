#!/bin/bash

# Deployment script for gorod.io 
#
# Author: I. Karbachinsky

set -e
set -o pipefail
set -x


# production serverhost="81.222.134.119"
host="localhost"
port=2222
# ssh user
ssh_user="gorodin"
# app directory path
app_dir="/home/g/gorodin/gorod.in"

ssh_opts="-p $port"
ssh_key=""

#read -s -p "ssh password: " password


#if [ -z "$password" ]; then
#    echo "Plese specify ssh password! ./deploy.sh *******" >&2 
#    exit 1
#fi


execute_remote() {
    host=$1
    command=$2
    error_message=$3
    # Message used in local mode
    local_error_message=$4
    return_error_code=$5

    if [[ -z "$host" || -z "$command" ]]; then
        return 1
    fi

    server=`echo "$host" | sed "s/.*@//g"`

    # GOVNOKOD
    command="~/env.sh; $command"

    if [ "$server" != "localhost" ]; then
        sshpass -p $password ssh $ssh_opts $ssh_key "$ssh_user"@"$host" "$command"
    else
        eval $command
    fi

    local RETURN_VALUE="$?"
    if [ "$RETURN_VALUE" != 0 ] ; then
        if [[ "$server_name" != "localhost" || -z "$local_error_message" ]]; then
            if [ ! -z "$error_message" ]; then
                echo "$error_message" >&2
            fi
        else
            echo "$local_error_message" >&2
        fi

        if [ "$return_error_code" != "1" ]; then
            exit $RETURN_VALUE
        else
            return $RETURN_VALUE
        fi
    fi

    return 0    
}


# Updating files
execute_remote $host  "cd $app_dir; git reset --hard; git clean -f -d"
execute_remote $host  "cd $app_dir; git pull origin"

# Updating settings.py
execute_remote $host "cd $app_dir; cp settings.py.production settings.py"

# Updating db
#execute_remote $host "cd $app_dir; ./manage.py schemamigration gorod --auto"
#execute_remote $host "cd $app_dir; ./manage.py migrate gorod"

# Updating static
execute_remote $host "cd $app_dir; ./manage.py collectstatic"


# Restart wsgi
execute_remote $host "cd $app_dir; touch index.wsgi"

