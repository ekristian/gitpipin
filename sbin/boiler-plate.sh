#!/usr/bin/env bash

set -o errexit                                                                  
set -o pipefail                                                                 
set -o nounset                                                                  
__src_cli_call="${BASH_SOURCE[0]}"                                              
__src_location="$(cd "$(dirname "${__src_cli_call}")" && pwd )"                 
__src_absolute="${__src_location}/$(basename "${__src_cli_call}")"              
__src_name="$(basename "${__src_absolute}")"                                    
__src_home="$(cd "$(dirname "${__src_location}")" && pwd)"                      
__src_sessionid=$(echo ${USER}-$(hostname)-${$} | md5sum | awk '{print $1}')

function is-yum-installed () {
    if yum list installed "$@" >/dev/null 2>&1; then
        true
    else
        false
    fi
}
